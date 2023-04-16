import streamlit as st
from tinydb import TinyDB

st.markdown("""
            
            # An experiment to build a database using a form 💻.
            * libirary using in the app . 
            * streamlit 🤩, tinydb 😻.
    
            
            """)

name = st.text_input('Write your name here 🥳:')
gender = st.multiselect('Choose Your gender 💁', ['Male', 'Female'])
age  = st.slider('Your age 🔢: ', min_value=10, max_value=75, value=20)
loacation = st.text_input('Write where do you live 🌍:')
major  = st.multiselect('what is your major 💻: ', ['Computer Science', 'Information Tech', 'Cyber S', 'Networks Eng', 'Other'])
other = st.text_input('for Other : ')
email = st.text_input('Write Your Email 📪: ')


# Here just put the path of the .json file where you want .
db = TinyDB(r'Twitter.json')

# To insert the Data in the DataBase
if st.checkbox('I accept that you can take my data 😉') != 1:
    warn = st.warning('If you want to complete the survy you should agree', icon="⚠️")
    if name and gender and age and loacation and major:
        db.insert({
         "name": name, 
         "gender" : gender, 
         "age" : age, 
         "location" : loacation, 
         "major": major, 
         "other": other,
         "email" : email
     })
st.button('Submit')

