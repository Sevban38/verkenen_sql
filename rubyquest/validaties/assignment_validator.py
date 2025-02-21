import os,sys,re
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.chdir(os.path.dirname(os.path.dirname(__file__)))

import db, ast, builtins
from termcolor import colored

MAX_REPORT_STRING = 100

data = {'results':[], 'active': True}

def assignment_scraper(file_path):
    try:
        with open(file_path, "r") as file:
            tree = ast.parse(file.read(), filename=file_path)
    except Exception as e:
        add_validation_result(txt = '{}:  ' + file_path + ' does not exists', vars=['failed'], color='red')
        return {}
    
    variables = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    if isinstance(node.value, ast.Constant):
                        variables[target.id] = node.value.value
    
    return variables

def database_result(database, query):
    dbconn = db.connect(database, False)
    dbconn.setQuery(query, False)
    dbconn.execute()
    data = dbconn.fetch(False)
    return dbconn._columns, data
   

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    builtins.print(txt.format(*vars))

def add_validation_result(txt:str='{}', vars:list=[], color:str='yellow'):
  data['results'].append({"txt": txt, "vars": vars, "color": color })

def str_type(s):
  return str(s).replace('<class \'','').replace('\'>','')

def str_more(s: str, max: int) -> str:
  if len(s) > max:
      return s[:max] + "..."
  else:
      return s  

def validate(name: str, expect: any, value: any):
  passed = False
  type_expected = type(expect)
  if type(expect) == type(value) and value == expect:
    passed = True
  
  if passed:
    add_validation_result(txt = '{}: ' + name, vars=['success'], color='green')
  else:
    add_validation_result(txt = '{}:  ' + name, vars=['failed'], color='red')
    if type_expected != type(True):
      add_validation_result(txt = '   got:  {}', vars=[str_more(str(value),MAX_REPORT_STRING)])
  
  return passed

def validate_assignment(assigment, filename, query_contains, expected_rowcount=1, expected_columns=-1, expected_firstrowValue=False, functionality_used=['SELECT']):
    add_validation_result(txt='\n{}', vars=[assigment], color='magenta')
    result_data = []
    used_variables = assignment_scraper(filename)
    required_variables = ['database', 'query']

    if len(used_variables) == 0:
       pass
    elif sum([1 if var not in used_variables.keys() else 0 for var in required_variables]) > 0:
      add_validation_result(txt='{}: '+filename, vars=['your file'], color='blue')

      for var in required_variables:
        if var not in used_variables.keys():
          add_validation_result(txt='{}:  missing '+colored(var, color='yellow')+' variable', vars=['failed'], color='red')
    else:
        result_columns, result_data = database_result(used_variables['database'], used_variables['query'])
        add_validation_result(txt='{}: '+used_variables['query'], vars=['your answer'], color='blue')
    
        validate(f'query uses rubyquest.db', 'rubyquest.db', used_variables['database'])
        
        if not isinstance(query_contains, list):
            query_contains = [query_contains]

        for word in query_contains:
            validate(f'query contains "{word}"', True, word in used_variables['query'])
        
        for fnc in functionality_used:
          check = lambda t, q: t.lower() in q.lower()
          
          if '()' in fnc:
             check = lambda t, q: bool(re.search(t.replace('()','(.*)'), q, re.IGNORECASE))

          validate(f'query useses "{fnc.upper()}"', True, check(fnc, used_variables['query']))

        validate(f'query returns {expected_rowcount} row(s)', expected_rowcount, len(result_data))
        
        if isinstance(expected_columns, list): 
            testtxt = str(expected_columns).replace("[",  '"').replace("]",  '"').replace("'",  '')
            validate(f'query returns the column(s) {testtxt}', expected_columns, result_columns)
        elif isinstance(expected_columns, int):
            if expected_columns >= 0:
              validate(f'query returns {expected_columns} column(s)', expected_columns, len(result_columns))

        if expected_firstrowValue:
            if isinstance(expected_firstrowValue, list):
               for value in expected_firstrowValue:
                  validate(f'query returns "{value}" as one of it\'s first row values', True, value in result_data[0].values())
            else:
              result_firstValue = next(iter(result_data[0].values())) if isinstance(result_data, list) and len(result_data) > 0 else False
              validate(f'query returns "{expected_firstrowValue}" as first value', expected_firstrowValue, result_firstValue)

    return result_data

def report():
  builtins.print('\n******** VALIDATION REPORT *********')
  if len(data['results']) == 0 and not data['active']:
    print('No validation results!')
  while len(data['results']) > 0:
    line = data['results'].pop(0)
    print_colorvars(txt=line['txt'],vars=line['vars'], color=line['color'])
  print('')