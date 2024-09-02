import boto3
import pyodbc
import pandas as pd
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

def export_csv_file(conn):

    query = "SELECT * FROM EMP"
    df = pd.read_sql_query(query, conn)

    df.to_csv("exported_file.csv", index = False)

def main():
    db_instance = describe_rds_instances()
    print(db_instance)
    connection = check_connection()
    export_csv_file(connection)

if __name__ == "__main__":
    main()