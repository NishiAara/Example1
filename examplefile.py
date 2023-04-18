import pickle
from pathlib import Path

import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
from streamlit_authenticator import Authenticate

def home():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write('')

    with col2:
        st.write("Genique")

    with col3:
        st.write('')

def dashboard():
    # Render the dashboard page
    st.markdown('<h1 style="text-align: center;">Dashboard</h1>', unsafe_allow_html=True)

# Streamlit app
def app():
    # Set the app title
    # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
    st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")


    # --- USER AUTHENTICATION ---
    names = ["Nishi Aara", "Hemant Gupta"]
    usernames = ["naara", "hgupta"]
    passwords = ['pwd1','pwd2']

    credentials = {"usernames":{}}
            
    for uname,name,pwd in zip(usernames,names,passwords):
        user_dict = {"name": name, "password": pwd}
        credentials["usernames"].update({uname: user_dict})
            
    authenticator = stauth.Authenticate(credentials, "cokkie_name", "random_key", cookie_expiry_days=30)

    name, authentication_status, username = authenticator.login("Login", "main")

    if authentication_status == False:
        st.error("Username/password is incorrect")

    if authentication_status == None:
        st.warning("Please enter your username and password")

    if authentication_status:
        #----SIDEBAR----
        authenticator.logout("Logout", "sidebar")
        st.sidebar.title(f"Welcome {name}")
        
        # Sidebar for navigation
        pages = ['Home', 'Dashboard']
        page = st.sidebar.selectbox('Hello!', pages, index=0)

        # Render the selected page
        if page == 'Home':
            home()
        elif page == 'Dashboard':
            dashboard()

       
if __name__ == '__main__':
    app()
