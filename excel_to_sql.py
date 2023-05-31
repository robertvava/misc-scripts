
import pandas as pd
import sqlite3



def excel_to_sqlite(db_name, excel_file):
    # create a database connection
    conn = sqlite3.connect(db_name)

    # load the excel data into a pandas DataFrame
    df = pd.read_excel(excel_file, engine='openpyxl')

    # write the data from pandas DataFrame to sql table
    df.to_sql('excel_data', conn, if_exists='replace', index=False)

    conn.close()

# example usage:
excel_to_sqlite('my_database.db', 'excel_file.xlsx')