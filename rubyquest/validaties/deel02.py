from assignment_validator import validate_assignment, report

validate_assignment(
    assigment='Maak een query die alleen de persoon met id 7 laat zien',
    filename='deel02_vraag01.py', 
    query_contains=['person','id','7'], 
    expected_rowcount=1, 
    expected_columns=11
)

validate_assignment(
    assigment='Maak een query die de opdracht(en) terug geef waar je geen geld voor krijgt',
    filename='deel02_vraag02.py', 
    query_contains=['quest','gold', '0'], 
    expected_rowcount=1, 
    expected_columns=6
)

validate_assignment(
    assigment='Met welke query laat je alleen de steden uit regio 1 zien?',
    filename='deel02_vraag03.py', 
    query_contains=['city', 'region', '1'], 
    expected_rowcount=4, 
    expected_columns=3
)

validate_assignment(
    assigment='Met welke query laat je alleen de schapen zien die er in database te vinden zijn?',
    filename='deel02_vraag04.py', 
    query_contains=['animal','type','Sheep'], 
    expected_rowcount=23, 
    expected_columns=6
)

validate_assignment(
    assigment='Met welke query kan je nagaan welke dieren zijn gevangen als huisdier?',
    filename='deel02_vraag05.py', 
    query_contains=['animal','owner', '0'], 
    expected_rowcount=11, 
    expected_columns=6
)

validate_assignment(
    assigment='Met welke query kun je alleen de omschrijving van alle dieren laten zien behalve de schapen?',
    filename='deel02_vraag06.py', 
    query_contains=['animal','type','Sheep'], 
    expected_rowcount=82, 
    expected_columns=['type']
)

report()