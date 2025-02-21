from assignment_validator import validate_assignment, report

validate_assignment(
    assigment='Met welke query haal je alle personen op uit de database?',
    filename='deel01_vraag01.py', 
    query_contains='person', 
    expected_rowcount=204, 
    expected_columns=11
)

validate_assignment(
    assigment='Met welke query haal je alle steden op uit de database?',
    filename='deel01_vraag02.py', 
    query_contains='city', 
    expected_rowcount=27, 
    expected_columns=3
)

validate_assignment(
    assigment='Met welke query haal je alle opdrachten (taken) op uit de database?',
    filename='deel01_vraag03.py', 
    query_contains='quest', 
    expected_rowcount=73, 
    expected_columns=6
)

validate_assignment(
    assigment='Met welke query haal je alle wezens op uit de database?',
    filename='deel01_vraag04.py', 
    query_contains='creature', 
    expected_rowcount=259, 
    expected_columns=9
)

validate_assignment(
    assigment='Met welke query haal je alleen alle namen van bescherming op uit de database?',
    filename='deel01_vraag05.py', 
    query_contains=['armor','name'], 
    expected_rowcount=23, 
    expected_columns=['name']
)

validate_assignment(
    assigment='Met welke query haal je alleen alle namen en aanvalskracht van wapens op uit de database?',
    filename='deel01_vraag06.py', 
    query_contains=['weapon','name','attack'], 
    expected_rowcount=52, 
    expected_columns=['name','attack']
)

validate_assignment(
    assigment='Met welke query haal je alleen alle namen en gezondheid van alle wezens op uit de database?',
    filename='deel01_vraag07.py', 
    query_contains=['name','health','creature'], 
    expected_rowcount=259, 
    expected_columns=2
)

report()