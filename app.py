import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime,date
import os
import time
import sys

st.title("db trial")
st.markdown("DB TRIAL APP")
appdir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
conn = sqlite3.connect(os.path.join(appdir, 'todo.db'))
cursor = conn.cursor()
v1=st.date_input("Last Date: ")
v2=st.text_input("Task: ")
v3=st.text_input("Descrıptıon: ")
v4=datetime.now()
btn=st.button("Rec")
btn2=st.button("Take Records")
if btn:
    cursor.execute("INSERT INTO notesdb (LAST_DATE,TASK,DESCRIPTION,CREATED_AT) VALUES (?,?,?,?)",(v1, v2, v3, v4))
    st.write("Recorded")
if btn2:
    t=cursor.execute('select task,description,last_date from notesdb order by rowid desc limit 5')
    rows=cursor.fetchall()
    st.table(rows)





conn.commit()
conn.close()




