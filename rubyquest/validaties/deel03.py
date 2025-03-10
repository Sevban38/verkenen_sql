from assignment_validator import validate_assignment, report

validate_assignment(
    assigment='Met welke query laat je alle opdrachten zien die je meer dan 3000 ervaringspunten opleveren?',
    filename='deel03_vraag01.py', 
    query_contains=['quest','experience', '3000'], 
    expected_rowcount=16, 
    expected_columns=6
)

validate_assignment(
    assigment='Met welke query kun je de personen laten zien die meer dan 1800 goud hebben?',
    filename='deel03_vraag02.py', 
    query_contains=['person','gold', '1800'], 
    expected_rowcount=7, 
    expected_columns=11
)

validate_assignment(
    assigment='Met welke query kun je de personen laten zien die minder dan 1850 goud hebben?',
    filename='deel03_vraag03.py', 
    query_contains=['person', 'gold', '1850'],
    expected_rowcount=197, 
    expected_columns=11
)

validate_assignment(
    assigment='Met welke query kun je de personen laten zien die 1300 of meer goud hebben?',
    filename='deel03_vraag04.py', 
    query_contains=['person', 'gold', '1300'],
    expected_rowcount=9, 
    expected_columns=11
)

validate_assignment(
    assigment='Met welke query kun je de wapens laten zien die minder dan 300 kosten?',
    filename='deel03_vraag05.py', 
    query_contains=['weapon','price', '300'], 
    expected_rowcount=19, 
    expected_columns=4
)

validate_assignment(
    assigment='Met welke query kan je nagaan welke opdracht meer geld dan ervaring opleverd?',
    filename='deel03_vraag06.py', 
    query_contains=['quest','gold', 'experience'], 
    expected_columns=6
)

validate_assignment(
    assigment='Met welke query vraag je de namen van de wezens op die gewond zijn?',
    filename='deel03_vraag07.py', 
    query_contains=['creature','name','health','max_health'], 
    expected_columns=['name'],
    expected_firstrowValue='Orc'
)

report()