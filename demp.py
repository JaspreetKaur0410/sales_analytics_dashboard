from turtle import color
from altair import Orientation
import streamlit as st
import pandas as pd
import plotly.express as px
import time
from streamlit_option_menu import option_menu
from numerize.numerize import numerize

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

#gets the credentials from .aws/credentials
session = boto3.Session(
    aws_access_key_id="AKIA5W6HQPHPOPU2DWF2",
    aws_secret_access_key="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",
    region_name=REGION
)
# client = session.client('rds')
# token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT,passwd=PASSWORD, DBUsername=USER, Region=REGION)
# print("*************"+token)
try:
    conn =  pymysql.connect(host=ENDPOINT, user=USER, passwd=PASSWORD, port=PORT, database=DBNAME)
    cur = conn.cursor()
    cur.execute("""select * from insurance order by id asc""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))  