from assignment_validator import validate_assignment, report

validate_assignment(
    assigment='Met welke query kun je de creatures laten zien die voldoen aan ‘Killer Bee’ of ‘Orc’?',
    filename='deel05_vraag01.py', 
    query_contains=['creature','name','Killer Bee','Orc'], 
    functionality_used=['SELECT','WHERE','OR'],
    expected_rowcount=24, 
    expected_columns=9
)

validate_assignment(
    assigment='Met welke query kun je de dieren laten zien die voldoen aan snelheid 6 en verdediging 5?',
    filename='deel05_vraag02.py', 
    query_contains=['animal','speed','6','defense','5'], 
    functionality_used=['SELECT','WHERE','AND'],
    expected_rowcount=15, 
    expected_columns=6
)

validate_assignment(
    assigment='Met welke query kun je het aantal dieren laten zien die voldoen aan ‘Wolf’ of ‘Bear’ of ‘Eagle’?',
    filename='deel05_vraag03.py', 
    query_contains=['animal','type','Wolf','Bear','Eagle'], 
    functionality_used=['SELECT','WHERE','COUNT()'],
    expected_columns=1,
    expected_firstrowValue=47
)

validate_assignment(
    assigment='Met welke query kun je bepalen welke tijger het snelst is?',
    filename='deel05_vraag04.py', 
    query_contains=['animal','type','speed', '1'], 
    functionality_used=['SELECT','ORDER BY','DESC','LIMIT'],
    expected_columns=6,
    expected_firstrowValue=77
)

validate_assignment(
    assigment='Met welke query kun je de personen laten zien waarvoor geldt attack, defense en agility voor alle drie de waarde gelijk aan 10?',
    filename='deel05_vraag05.py', 
    query_contains=['person','attack','defense','agility'], 
    functionality_used=['SELECT','WHERE','AND'],
    expected_rowcount=189, 
    expected_columns=11
)

validate_assignment(
    assigment='Met welke query kun je alle hero’s laten zien met intelligence anders dan 30 of 90?',
    filename='deel05_vraag06.py', 
    query_contains=['hero','intelligence', '30', '90'], 
    functionality_used=['SELECT','WHERE'],
    expected_rowcount=5, 
    expected_columns=8
)

report()