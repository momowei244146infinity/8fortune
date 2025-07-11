
import streamlit as st
import os
import pandas as pd
import re
from display_quiz import QuizDis


class UserLogin:
    def __init__(self):
        
        # welcome a user
        st.title("Welcome to take the Quiz")
        # new user or existing user
        st.subheader("Please login or create a new account")

        if st.button("Create a new account"):
            self.create_account()
                
        username_input = st.text_input("Username", value="")
        password_input = st.text_input("Password", value="")

        # user does not exists
        if username_input == "":
            pass
        elif self.is_username_exist(username_input):
            if password_input == "":
                st.write("Please enter your password")
            elif self.username_password_match(username_input, password_input):
                st.write(f"Welcome back, {username_input}!")
                button = st.button("Go to Quiz")    
            else:
                st.write("Incorrect password. Please try again.")
        
        else:
            st.write(f"Username {username_input} does not exist. Need to create a new account")
            
    
    @st.dialog("Creat new account")
    def create_account(self):
        # select a new username
        user_input_new = st.text_input("Please Create Your Username", value="")
        if user_input_new == "":
            pass
        elif self.is_username_exist(user_input_new):
            st.write(f"Username {user_input_new} already exists. Please choose another one.")
            #st.rerun(scope="fragment")
        else:
            # create password
            password_input_new = st.text_input("Please Create Your Password", value="")
            if password_input_new == "":
                pass
            elif not self.is_password_valid(password_input_new):
                st.write("Recreate a password. Your password should only contain numbers, character, _ and lenght between 6 and 10 characters.")
            else:
                self._create_user_account(user_input_new, password_input_new)
                if st.button("Go to Quiz"):
                    pass
    
    def _create_user_account(self, user_input_new: str, password_input_new: str):
        df = pd.read_csv("username password.csv", delimiter=",")
        df.loc[len(df)] = [user_input_new, password_input_new]
        # create a new folder for the user
        new_folder_path = os.path.join(os.path.abspath("./users"), user_input_new)
        os.mkdir(new_folder_path)
        df.to_csv("username password.csv", index=False)
        st.write(f"Account created successfully for {user_input_new}!")

    def is_password_valid(self, password: str):
        return bool(re.match(r'^\w+$', password)) and (len(password) >= 6 and len(password) <= 10)

    def is_username_exist(self, username_input: str):
        df = pd.read_csv("username password.csv", delimiter=",")
        return username_input in df['username'].values
    
    def username_password_match(self, username_input: str, password_input: str):
        if self.is_username_exist(username_input):
            df = pd.read_csv("username password.csv", delimiter=",")
            idx = df['username'] == username_input
            correct_password = df.loc[idx, 'password']
            return correct_password.values[0] == password_input
        return False



if __name__ == '__main__':
    UserLogin()

        
        