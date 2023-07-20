import streamlit as st

prompt = st.chat_input("Say something")

with st.chat_message("Here is my first Streamlit Chatbot")
st.write(prompt)

#if prompt:
 # conn = st.experimental_connection('snowpark')
  #query = f"select llm_complete('(prompt)')"
  #response = conn.query(query).iloc(0,0)

