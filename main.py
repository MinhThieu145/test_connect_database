# streamlit_app.py

import streamlit as st
import mysql.connector
import pandas as pd

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Form the cursor
c = conn.cursor(buffered=True)

def sql_executor(raw_sql_code):
    c.execute(raw_sql_code)
    data = c.fetchall()
    return data

def main():
    st.title('SQL Playground')

    menu = ['Home', 'About']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.subheader('Home page')
        
        with st.form(key='mysql_query_form'):
            raw_code = st.text_area('SQL Code Here')
            submit_code = st.form_submit_button('Execute')
        
        
        if submit_code:
            st.info('Query Submitted')
            st.write(raw_code)
                
            # Return result
            query_result = sql_executor(raw_code)
            df = pd.DataFrame(query_result, columns = ['checking_date', 'checking_time', 'hour', 'day_of_week', 'date', 'room','status'])
            st.code(df)
            st.write(df.dtypes)
            
    else:
        st.subheader('About')

if __name__ == '__main__':
    main()
