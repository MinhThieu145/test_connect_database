# streamlit_app.py

import streamlit as st
import mysql.connector

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
            df = pd.DataFrame(query_result, columns = ['checking_time_uct','current_hour', 'day_of_week', 'current_room_date', 'room','status'])
            st.dataframe(df)
            
    else:
        st.subheader('About')

if __name__ == '__main__':
    main()
