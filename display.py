import streamlit as st
from display_quiz import *
from user_login import *


class Display:
    def __init__(self):
        
        # welcome a user
        # new user or existing user
        # new create a account
        # older user_login
        # input user name
        # input password

            # if user name does not exist, wrong input or create a new user
            # if user password does not exists, create a new password
        UserLogin()

        if st.button("Go to Quiz"):

        # Display quiz
            QuizDis()

if __name__ == "__main__":
    Display()

        