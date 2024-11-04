import streamlit as st
import psycopg2 as pgsconn
import pandas as pd

@st.cache_resource
def initialize_connection():
    return pgsconn.connect(host = 'localhost', port = '5432', dbname = 'hotel_management', user = 'postgres', password = 'Iris@1234')


conn = initialize_connection()
def exec_query(q):
    with conn.cursor() as c:
        c.execute(q)
        if c.description:
            r = c.fetchall()
            return r
        else:
            return None

q = st.text_input("Enter yor query")

output = pd.DataFrame(exec_query(q))

st.table(output)
st.write(output)