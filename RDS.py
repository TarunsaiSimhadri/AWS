import boto3
import pyodbc
import os
from dotenv import load_dotenv

def describe_rds_instances():
    client = boto3.client('rds', region_name = 'ap-south-1')
    response = client.describe_db_instances()
    for instance in response['DBInstances']:
        print(f"Instance ID: {instance['DBInstanceIdentifier']}")
        print(f"Endpoint: {instance['Endpoint']['Address']}")
        print(f"Port: {instance['Endpoint']['Port']}")
        print()
    return response

load_dotenv()

SERVER = os.getenv("SERVER")
db_name = os.getenv("db_name")
UID = os.getenv("UID")
PASSWD = os.getenv("PASSWD")

def check_connection():

    connection_str = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={db_name};UID={UID};PWD={PASSWD}'
    conn = pyodbc.connect(connection_str)

    return conn

def conn_cursor(conn):

    cursor = conn.cursor()
    return cursor


def create_table(conn, cursor):

    cursor.execute('CREATE TABLE emp(Eid int PRIMARY KEY, Ename VARCHAR(200))')
    conn.commit()

def insert_details(conn, cursor):
      
    query = 'INSERT INTO emp (Eid, Ename) VALUES (?,?)'
    cursor.execute(query, (100, 'tarun'))
    conn.commit()

def update_detils(conn, cursor):

    query = "UPDATE emp SET Ename = 'varun' WHERE Eid = 100"
    cursor.execute(query)
    conn.commit()

def delete_details(conn, cursor):

    cursor.execute('DELETE FROM emp WHERE Eid = 200')
    conn.commit()

def alter_add_col(conn, cursor):
        
    cursor.execute('ALTER TABLE emp ADD email VARCHAR(200)') 
    conn.commit()

def delete_table(conn, cursor):
        
    cursor.execute('DROP TABLE emp')
    conn.commit()


def main():

    instance = describe_rds_instances()
    connection = check_connection()
    print(connection)
    cursor = conn_cursor(connection)
    create_table(connection, cursor)
    # insert_details(connection, cursor)
    # alter_add_col(connection, cursor)
    # delete_table(connection, cursor)
    # update_detils(connection, cursor)
    # delete_table(connection, cursor)

    if connection:
        connection.close()

if __name__ == '__main__':
    main()