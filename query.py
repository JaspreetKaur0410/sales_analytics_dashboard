import streamlit as st
import pymysql
import sys
import boto3
import os

ENDPOINT="database-2.cuzlxxs7vcah.us-east-1.rds.amazonaws.com"
PORT=3306
USER="admin"
REGION="us-east-1"
DBNAME="analytics_db"
PASSWORD="Ja1sitaram"
# os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

# gets the credentials from .aws/credentials
# session = boto3.Session(profile_name='default')
# client = session.client('rds')

# token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

try:
    conn =  pymysql.connect(host=ENDPOINT, user=USER, passwd=PASSWORD, port=PORT, database=DBNAME, ssl_ca='SSLCERTIFICATE')
    cur = conn.cursor()
    cur.execute("""select * from insurance order by id asc""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))               

def view_all_data():
    conn =  pymysql.connect(host=ENDPOINT, user=USER, passwd=PASSWORD, port=PORT, database=DBNAME, ssl_ca='SSLCERTIFICATE')
    cur = conn.cursor()
    cur.execute("""select * from insurance order by id asc""")
    query_results = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    print(query_results)
    return query_results
    
