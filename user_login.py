
import streamlit as st
import os
import pandas as pd
import re
import itertools
import shutil
from base_data import *


QUIZ = ["pillar_melody", "melody_pillar", "pillar_period", "nobel_man_forward", "nobel_man_backward"]
QUIZ_STATE_FILE_DIC = {
    "pillar_melody" : {"primary_column": "pillar",
                       "primary_column_item_cnt":1,
                       "primary_column_item_src": pillar}, 
    "melody_pillar": {"primary_column": "melody",
                       "primary_column_item_cnt":1,
                       "primary_column_item_src": melody}, 
    "pillar_period": {"primary_column": "pillar_pair",
                       "primary_column_item_cnt":2,
                       "primary_column_item_src": pillar}, 
    "nobel_man_forward": {"primary_column": "sky",
                       "primary_column_item_cnt":1,
                       "primary_column_item_src": sky}, 
    "nobel_man_backward": {"primary_column": "ground",
                       "primary_column_item_cnt":1,
                       "primary_column_item_src": ground}
}

class UserLogin:
    def __init__(self):
        
        # welcome a user
        st.title("Welcome to take the Quiz")
        # new user or existing user
        st.subheader("Please login or create a new account")

        if st.button("Create a new account"):
            self.create_account()

        st.subheader("Login")   
        self.login_account()     
                
        if st.button("Delete Account"):
            self.delete_account()
            
    
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
    
    def login_account(self):
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
            else:
                st.write("Incorrect password. Please try again.")
        
        else:
            st.write(f"Username {username_input} does not exist. Need to create a new account")

    @st.dialog("Delete Account")
    def delete_account(self):
        user_input = st.text_input("Please Input Your Username", value="")
        if user_input == "":
            pass
        elif self.is_username_exist(user_input):
            df = pd.read_csv("username password.csv")
            # Delete row where username is 'user1'
            df = df[df['username'] != user_input]
            df.to_csv("username password.csv", index=False)
            st.write(f"Account {user_input} deleted successfully!")
            # delete user folder
            user_folder_path = os.path.join(os.path.abspath("./users"), user_input)
            if os.path.exists(user_folder_path):
                shutil.rmtree(user_folder_path)
        else:
            # create password
            st.write(f"Username {user_input} does not exist. Please input a correct username.")

    def _create_user_account(self, user_input_new: str, password_input_new: str):
        # add new user and password to csv file(database)
        df = pd.read_csv("username password.csv", delimiter=",")
        df.loc[len(df)] = [user_input_new, password_input_new]
        df.to_csv("username password.csv", index=False)
        st.write(f"Account created successfully for {user_input_new}!")
        # create a new folder for the user
        new_folder_path = os.path.join(os.path.abspath("./users"), user_input_new)
        os.mkdir(new_folder_path)
        self.create_quiz_stat_file(new_folder_path)
    
    def create_quiz_stat_file(self, new_folder_path: str):
        for quiz_choice in QUIZ:
            primary_col = QUIZ_STATE_FILE_DIC[quiz_choice]["primary_column"]
            df = pd.DataFrame(columns=[primary_col, "correct", "wrong", "total"])
            if QUIZ_STATE_FILE_DIC[quiz_choice]["primary_column_item_cnt"] == 1:
                df[primary_col] = QUIZ_STATE_FILE_DIC[quiz_choice]["primary_column_item_src"]
            elif QUIZ_STATE_FILE_DIC[quiz_choice]["primary_column_item_cnt"] == 2:
                col = QUIZ_STATE_FILE_DIC[quiz_choice]["primary_column_item_src"]
                df[primary_col] = list(itertools.combinations(col, 2))
            df["correct"] = 0
            df["wrong"] = 0
            df["total"] = 0
            df.to_csv(os.path.join(new_folder_path, f"{quiz_choice}.csv"), index=False)    

    def is_password_valid(self, password: str):
        return bool(re.match(r'^\w+$', password)) and (len(password) >= 6 and len(password) <= 10)

    def is_username_exist(self, username_input: str):
        df = pd.read_csv("username password.csv", delimiter=",")
        return username_input in df['username'].values
    
    def username_password_match(self, username_input: str, password_input: str):
        if self.is_username_exist(username_input):
            df = pd.read_csv("username password.csv", delimiter=",")
            idx = df['username'] == username_input
            correct_password = df.loc[idx, "password"].values[0]
            return str(correct_password) == password_input
        return False



if __name__ == '__main__':
    UserLogin()

        
        