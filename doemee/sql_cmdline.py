# python basis code voor opdrachten aanmaken eigen database
# deze opdracht moet ingeleverd worden en dient als beoordeling voor het onderdeel sql verkennen
# (c) DaVinci 2025
#
# 
import sqlite3
import os

def list_databases():
    """Lijst alle SQLite-databasebestanden in de huidige directory."""
    return [f for f in os.listdir() if f.endswith('.db')]

def choose_or_create_db():
    """Laat de gebruiker een bestaande database selecteren of een nieuwe aanmaken."""
    databases = list_databases()
    if databases:
        print("Beschikbare databases:")
        for i, db in enumerate(databases, 1):
            print(f"{i}. {db}")
        print(f"{len(databases) + 1}. Nieuwe database aanmaken")
        choice = input(f"Kies een optie (1-{len(databases) + 1}): ")
        if choice.isdigit() and 1 <= int(choice) <= len(databases):
            db_name = databases[int(choice) - 1]
            print(f"Verbinding maken met bestaande database: {db_name}")
        elif choice == str(len(databases) + 1):
            db_name = input("Voer de naam van de nieuwe database in (bijv. studenten.db): ")
            print(f"Nieuwe database {db_name} wordt aangemaakt.")
        else:
            print("Ongeldige keuze, een nieuwe database wordt aangemaakt.")
            db_name = input("Voer de naam van de nieuwe database in (bijv. studenten.db): ")
    else:
        print("Geen bestaande databases gevonden. Een nieuwe database wordt aangemaakt.")
        db_name = input("Voer de naam van de nieuwe database in (bijv. studenten.db): ")
    return db_name

def create_connection(db_name):
    """Creëer een verbinding met de SQLite database."""
    conn = sqlite3.connect(db_name)
    return conn

def check_tables_exist(conn, table_names):
    """Controleer of de opgegeven tabellen aanwezig zijn in de database."""
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    existing_tables = {table[0] for table in cursor.fetchall()}
    table_status = {table: (table in existing_tables) for table in table_names}
    return table_status

def create_table(conn,table):
    """Creëer tabel in de database."""
    cursor = conn.cursor()
    sql_commando = '' 
    if table == "personen":
        sql_commando = '''CREATE TABLE IF NOT EXISTS personen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        length FLOAT
        );
        '''
    elif table == "sporten":
        sql_commando = '''CREATE TABLE IF NOT EXISTS sporten (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
        );
        '''
    cursor.execute(sql_commando)        
    conn.commit()

def add_row(conn, table):
    """Voeg regel toe aan table in de database."""
    cursor = conn.cursor()
    sql_command = ""
    if table == "personen":
        name = input("Naam van de persoon: ")
        sql_command =f"INSERT INTO personen (name) VALUES (\"{name}\");"
        print(sql_command)
        cursor.execute(sql_command)
        print(f"Persoon {name} toegevoegd.")
    # we missen sporten
    if table == "sporten":    
        name = input("Naam van de sport: ")
        sql_command =f"INSERT INTO sporten (name) VALUES (\"{name}\");"
        print(sql_command)
        cursor.execute(sql_command)
        print(f"Sport {name} toegevoegd.")

    conn.commit()

def view_rows(conn,table):
    """Bekijk alle studenten in de database."""
    # we missen verschillen per tabel..... 
    # if table == "personen"
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    if rows:
        print("ID | Naam     ")
        print("--------------")
        for row in rows:
            print(f"{row[0]} | {row[1]} ")
    else:
        print(f"Er zijn geen {table} regels in de database.")

def delete_row(conn, table):
    """Verwijder een student uit de database op basis van het ID."""
    id = int(input(f"ID van de regel in tabel {table} om te verwijderen: "))
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table} WHERE id = ?", (id,))
    conn.commit()
    print(f"Regel met ID {id} verwijderd.")

def menu(conn,db_name,table_name):
    """Menu voor het programma."""
    while True:
        print(f"\n{db_name} Database table {table_name}")
        print(f"1. Voeg toe aan tabel {table_name}")
        print(f"2. Bekijk inhoud tabel {table_name}")
        print(f"3. Verwijder uit tabel {table_name}")
        print("4. Stop")
        choice = input("Kies een optie (1-4): ")

        if choice == '1':
            add_row(conn, table_name)
        elif choice == '2':
            view_rows(conn,table_name)
        elif choice == '3':
            delete_row(conn, table_name)
        elif choice == '4':
            print("Andere tabel kiezen.")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")

table_names = ['personen', 'sporten', 'nog_doen']

if __name__ == '__main__':
    db_name = choose_or_create_db()
    conn = create_connection(db_name)

    table_status = check_tables_exist(conn, table_names)
    print("\nTabelstatus:")
    new_tables = False
    for table, exists in table_status.items():
        status = "aanwezig" if exists else "niet aanwezig"
        print(f"- {table}: {status}")
        if not exists:
            create_table(conn,table)
            print(f"- {table}: created")
            new_tables=True

    # tweede keer opvragen als tabellen zijn bijgemaakt
    if new_tables:
        table_status = check_tables_exist(conn, table_names)
    while True:            
        print("Beschikbare tabellen:")
        i = 1
        for table, exists in table_status.items():
            if exists:
                print(f"{i}. {table}")                
                i +=1
        print(f"{i}. Stoppen")        
        choice = int(input(f"Kies een optie (1-{i}): "))     
           
        if choice == i:
            break
        menu(conn, db_name,table_names[choice-1])

    conn.close()
