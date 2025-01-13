import pyodbc

def get_connection(db_config):
    connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={db_config['SERVER']},{db_config['PORT']};"
        f"DATABASE={db_config['DATABASE']};"
        f"UID={db_config['USER']};"
        f"PWD={db_config['PASSWORD']}"
    )
    return pyodbc.connect(connection_string)
