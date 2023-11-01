import streamlit as st
import pymysql
import sys
import boto3
import os

# ENDPOINT="database-2.cuzlxxs7vcah.us-east-1.rds.amazonaws.com"
# PORT=3306
# USER="admin"
# REGION="us-east-1"
# DBNAME="analytics_db"
# PASSWORD="Ja1sitaram"
# os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

#gets the credentials from .aws/credentials
session = boto3.Session(
    aws_access_key_id=st.secrets["aws_access_key_id"],
    aws_secret_access_key=st.secrets["aws_secret_access_key"],
    region_name=st.secrets["REGION"]
)
# client = session.client('rds')
# token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT,passwd=PASSWORD, DBUsername=USER, Region=REGION)
# print("*************"+token)
try:
    conn =  pymysql.connect(host=st.secrets["ENDPOINT"], user=st.secrets["USER"], passwd=st.secrets["PASSWORD"], port=st.secrets["PORT"], 
                                    database=st.secrets["DBNAME"])
    cur = conn.cursor()
    cur.execute("""select * from insurance order by id asc""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))                  

def view_all_data():
    conn =  pymysql.connect(host=st.secrets["ENDPOINT"], user=st.secrets["USER"], passwd=st.secrets["PASSWORD"], port=st.secrets["PORT"], database=st.secrets["DBNAME"])
    cur = conn.cursor()
    cur.execute("""select * from insurance order by id asc""")
    query_results = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    print(query_results)
    return query_results
    
