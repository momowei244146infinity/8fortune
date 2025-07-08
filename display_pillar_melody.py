import streamlit as st
from base_data import *
import random
import pandas as pd
import os
from datetime import datetime
from collections import defaultdict

#from streamlit_extras.switch_page_button import switch_page



#pillar_melody_csv_path = os.path.join(os.path.dirname(__file__), 'pillar_melody_record.csv')
#melody_pillar_csv_path = os.path.join(os.path.dirname(__file__), 'melody_pillar_record.csv')

class QuizDisplay:

    def __init__(self):

        st.title("Quiz")
        st.subheader("Pillar Melody Quiz")
   
        if st.button("Go to Pillar Melody Quiz"):
            self.display_question_main1()
        
        if st.button("Go to Melody Pillar Quiz"):
            self.display_question_main2()
        
        if st.button("Go to Pillar Period Quiz"):
            self.display_question_main3()
        
        st.subheader("Nobility Quiz")
        
        if st.button("Go to Nobility Forward Quiz"):
            self.display_question_main4()
        
    def get_data(self):
        pass

    @st.dialog("Lets start pillar melody quiz", width='large')
    def display_question_main1(self):
        if 'current_pillar' not in st.session_state:
            pillar_random = random.sample(list(pillar), len(pillar))
            st.session_state['pillar_random'] = pillar_random
            st.session_state['current_pillar'] = pillar_random.pop()
            st.session_state['pillar_melody_answered'] = False
            st.session_state['pillar_melody_cnt'] = 0
            st.session_state['pillar_melody_user_answer'] = ""
            st.session_state['pillar_melody_user_correct_cnt'] = 0
            st.session_state['pillar_melody_user_wrong_record'] = []
        # display question, get user input
        pillar_item, correct_answer, user_input = self.question1()

        # click submit
        if st.button('Submit'):
            self.question1_submit(pillar_item, correct_answer, user_input)
        
        if st.button("Next Question", key=f"melody_select_next_{st.session_state['pillar_melody_cnt']}"):
            # Get next question\
            self.question1_next()
                    
        if st.button('Review Round answers'):
            self.question1_review()
        
        if st.button('Reset Round'):
            self.question1_round_reset()
           

    def question1(self):
        pillar_item = st.session_state['current_pillar']
        correct_answer = pillar_melody_dic[pillar_item]
        
        # show the queestion
        st.subheader(f'What\'s the melody of {pillar_item}?')

        # Get user input
        melody_with_empty = [""] + melody
        user_input = st.selectbox(
            'Select a melody',
            options=melody_with_empty,
            index=None,
            key=f"melody_select_{st.session_state['pillar_melody_cnt']}",
            label_visibility='collapsed'
        )
        #st.text_input("Please enter your answer", value=st.session_state['pillar_melody_user_answer'])
        st.session_state['pillar_melody_user_answer'] = user_input

        return pillar_item, correct_answer, user_input
    
    def question1_submit(self, pillar_item, correct_answer, user_input):
        st.session_state['pillar_melody_answered'] = True
        st.session_state['pillar_melody_cnt'] += 1
        if user_input != correct_answer:
            st.error(f"Wrong answer! The correct answer is {correct_answer}.")
            st.session_state['pillar_melody_user_wrong_record'].append((pillar_item, user_input, correct_answer))
        else:
            st.session_state['pillar_melody_user_correct_cnt'] += 1
            st.success("Correct answer!")

    def question1_next(self):
        if len(st.session_state['pillar_random']) > 0:
            st.session_state['current_pillar'] = st.session_state['pillar_random'].pop()
            st.session_state['pillar_melody_answered'] = False
            st.session_state['pillar_melody_user_answer'] = ""
            # Force a rerun to update UI
            st.rerun(scope="fragment")
                
        else:
            st.balloons()
            st.write("You've completed all questions!")

    #@st.dialog("Review your answers", width='large') # nexted dialog not suppprtd TT
    def question1_review(self):
        st.write(f"Let's review {str(st.session_state['pillar_melody_cnt'])} questions you answersed.")
        correct = st.session_state['pillar_melody_user_correct_cnt']
        wrong = st.session_state['pillar_melody_cnt'] - correct
        st.write(f"You got {correct} correct and {wrong} wrong in this round.")
        # Here you can implement the logic to review answers if needed.
        for item in st.session_state['pillar_melody_user_wrong_record']:
                
            pillar_item, user_answer, correct_answer = item
            st.write(f"Melody of pillar {pillar_item} is {correct_answer}, not {user_answer}.")

    def question1_round_reset(self):
        pillar_random = random.sample(list(pillar), len(pillar))
        st.session_state['pillar_random'] = pillar_random
        st.session_state['current_pillar'] = pillar_random.pop()
        st.session_state['pillar_melody_answered'] = False
        st.session_state['pillar_melody_cnt'] = 0
        st.session_state['pillar_melody_user_answer'] = ""
        st.session_state['pillar_melody_user_correct_cnt'] = 0
        st.session_state['pillar_melody_user_wrong_record'] = []

    ###########  melody pillar quiz ###########
    @st.dialog("Lets start meloday pillar quiz", width='large')
    def display_question_main2(self):
        if 'current_melody' not in st.session_state:
            melody_random = random.sample(list(melody), len(melody))
            st.session_state['melody_random'] = melody_random
            st.session_state['current_melody'] = melody_random.pop()
            st.session_state['melody_pillar_answered'] = False
            st.session_state['melody_pillar_cnt'] = 0
            st.session_state['melody_pillar_user_answer1'] = ""
            st.session_state['melody_pillar_user_answer2'] = ""
            st.session_state['melody_pillar_user_correct_cnt'] = 0
            st.session_state['melody_pillar_user_wrong_record'] = []
        # display question, get user input
        pillar_item, correct_answer, user_input = self.question2()

        # click submit
        if st.button('Submit'):
            self.question2_submit(pillar_item, correct_answer, user_input)
        
        if st.button("Next Question", key=f"melody_pillar_next_{st.session_state['melody_pillar_cnt']}"):
            # Get next question\
            self.question2_next()
                    
        if st.button('Review Round answers'):
            self.question2_review()
        
        if st.button('Reset Round'):
            self.question2_round_reset()

    def question2(self):
        melody_item = st.session_state['current_melody']
        correct_answer = melody_pillar_dic[melody_item]
        
        # show the queestion
        st.subheader(f'What are the pillars of {melody_item}?')

        # Get user input
        key = 1
        for col in st.columns(2):
            with col:
                user_input = self.question2_user_input(key = key)
                st.session_state[f'melody_pillar_user_answer{key}'] = user_input
            key += 1
        user_input = [st.session_state['melody_pillar_user_answer1'], st.session_state['melody_pillar_user_answer2']]

        return melody_item, correct_answer, user_input
    
    def question2_user_input(self, key=0):
        pillar_with_empty = [""] + pillar
        user_input = st.selectbox(
            'Select a pillar',
            options=pillar_with_empty,
            index=None,
            key=f"pillar_select_input_{str(key)}_{st.session_state['melody_pillar_cnt']}",
            label_visibility='collapsed'
        )
        #st.text_input("Please enter your answer", value=st.session_state['pillar_melody_user_answer'])
        return user_input
                
    def question2_submit(self, pillar_item, correct_answer, user_input):
        st.session_state['melody_pillar_answered'] = True
        st.session_state['melody_pillar_cnt'] += 1
        
        # check user input
        if set(user_input) != set(correct_answer):
            st.error(f"Wrong answer! The correct answer is {correct_answer}.")
            st.session_state['melody_pillar_user_wrong_record'].append((pillar_item, user_input, correct_answer))
        else:
            st.session_state['melody_pillar_user_correct_cnt'] += 1
            st.success("Correct answer!")

    def question2_next(self):
        if len(st.session_state['melody_random']) > 0:
            st.session_state['current_melody'] = st.session_state['melody_random'].pop()
            st.session_state['melody_pillar_answered'] = False
            st.session_state['melody_pillar_user_answer1'] = ""
            st.session_state['melody_pillar_user_answer2'] = ""
            # Force a rerun to update UI
            st.rerun(scope="fragment")
                
        else:
            st.balloons()
            st.write("You've completed all questions!")

    #@st.dialog("Review your answers", width='large') # nexted dialog not suppprtd TT
    def question2_review(self):
        st.write(f"Let's review {str(st.session_state['melody_pillar_cnt'])} questions you answersed.")
        correct = st.session_state['melody_pillar_user_correct_cnt']
        wrong = st.session_state['melody_pillar_cnt'] - correct
        st.write(f"You got {correct} correct and {wrong} wrong in this round.")
        # Here you can implement the logic to review answers if needed.
        for item in st.session_state['melody_pillar_user_wrong_record']:
                
            pillar_item, user_answer, correct_answer = item
            st.write(f"Melody of pillar {pillar_item} is {correct_answer[0]} and {correct_answer[1]}, not {user_answer[0]} and {user_answer[1]}.")

    def question2_round_reset(self):
        melody_random = random.sample(list(melody), len(melody))
        st.session_state['melody_random'] = melody_random
        st.session_state['current_melody'] = melody_random.pop()
        st.session_state['melody_pillar_answered'] = False
        st.session_state['melody_pillar_cnt'] = 0
        st.session_state['melody_pillar_user_answer1'] = ""
        st.session_state['melody_pillar_user_answer2'] = ""
        st.session_state['melody_pillar_user_correct_cnt'] = 0
        st.session_state['melody_pillar_user_wrong_record'] = []

    ###########  pillar period quiz ###########
    @st.dialog("Lets start pillar period quiz!", width='large')
    def display_question_main3(self):
        if 'current_period_pillar' not in st.session_state:
            period_pillar_random = random.sample(list(pillar), len(pillar))
            st.session_state['period_pillar_random'] = period_pillar_random
            st.session_state['current_period_pillar'] = period_pillar_random.pop()
            st.session_state['current_period_pillar1'] = period_pillar_random.pop()
            st.session_state['period_pillar_answered'] = False
            st.session_state['period_pillar_cnt'] = 0
            st.session_state['period_pillar_user_answer'] = None
            st.session_state['period_pillar_user_correct_cnt'] = 0
            st.session_state['period_pillar_user_wrong_record'] = []
        #display question
        # get userinput
        _, current_period_pillar1, current_period_pillar2 = self.question3()

        # submit answer
        if st.button("Submit"):
            self.question3_submit(current_period_pillar1, current_period_pillar2)

        # next question
        if st.button("Next Question"):
            # Get next question
            self.question3_next()
            
        # review
        if st.button("Review Round answers"):
            self.question3_review()

        # reset round
        if st.button("Reset Round"):
            self.question3_reset()


    def question3(self):
        current_period_pillar1 = st.session_state['current_period_pillar']
        current_period_pillar2 = st.session_state['current_period_pillar1']

        st.subheader(f'Are {current_period_pillar1} and {current_period_pillar2} in the same period?')
        
        answer_options = ['', 'Yes', 'No']
        user_input = st.selectbox(
            "Select your answer",
            options=answer_options,
            index=None,
            key=f"period_pillar_select_{st.session_state['period_pillar_cnt']}",
        )
        if user_input in ['Yes', 'No']:
            answer_map = {"Yes": True, "No": False}
            user_answer = answer_map[user_input]
            st.session_state['period_pillar_user_answer'] = user_answer
            return user_answer, current_period_pillar1, current_period_pillar2
        else:
            # Return None or default value when no selection is made
            st.session_state['period_pillar_user_answer'] = None
            return None, current_period_pillar1, current_period_pillar2

    def check_pillar_period(self, pillar1, pillar2):
        idx_pillar1 = pillar.index(pillar1)
        idx_pillar2 = pillar.index(pillar2)
        period1 = idx_pillar1 // 12
        period2 = idx_pillar2 // 12
        return period1 == period2
    
    def question3_submit(self, pillar1, pillar2):
        st.session_state['period_pillar_answered'] = True
        st.session_state['period_pillar_cnt'] += 1
        correct_answer = self.check_pillar_period(pillar1, pillar2)
        user_answer = st.session_state['period_pillar_user_answer']
        if correct_answer != user_answer:
            st.error(f"Wrong answer! {pillar1} and {pillar2} are {'not ' if not correct_answer else ''}in the same period.")
            st.session_state['period_pillar_user_wrong_record'].append((pillar1, pillar2, user_answer, correct_answer))
        else:
            st.session_state['period_pillar_user_correct_cnt'] += 1
            st.success("Correct answer!")

    def question3_next(self):
        if len(st.session_state['period_pillar_random']) > 1:
            st.session_state['current_period_pillar'] = st.session_state['period_pillar_random'].pop()
            st.session_state['current_period_pillar1'] = st.session_state['period_pillar_random'].pop()
            st.session_state['period_pillar_answered'] = False
            st.session_state['period_pillar_user_answer'] = None
            # Force a rerun to update UI
            st.rerun(scope="fragment")
        else:
            st.balloons()
            st.write("You've completed all questions!")
    
    def question3_review(self):
        st.write(f"Let's review {str(st.session_state['period_pillar_cnt'])} questions you answersed.")
        correct = st.session_state['period_pillar_user_correct_cnt']
        wrong = st.session_state['period_pillar_cnt'] - correct
        st.write(f"You got {correct} correct and {wrong} wrong in this round.")
        # Here you can implement the logic to review answers if needed.
        for item in st.session_state['period_pillar_user_wrong_record']:
                
            pillar1, pillar2, _, correct_answer = item
            st.write(f"Melody {pillar1} and {pillar2} are {'not ' if not correct_answer else ''} in the same period.")

    def question3_reset(self):
        period_pillar_random = random.sample(list(pillar), len(pillar))
        st.session_state['period_pillar_random'] = period_pillar_random
        st.session_state['current_period_pillar'] = period_pillar_random.pop()
        st.session_state['current_period_pillar1'] = period_pillar_random.pop()
        st.session_state['period_pillar_answered'] = False
        st.session_state['period_pillar_cnt'] = 0
        st.session_state['period_pillar_user_answer'] = None
        st.session_state['period_pillar_user_correct_cnt'] = 0
        st.session_state['period_pillar_user_wrong_record'] = []
    

    ###########  Nobility Forward quiz ###########
    @st.dialog("Lets start nobility forward quiz", width='large')
    def display_question_main4(self):
        pass

    


if __name__ == "__main__":
    quiz_display = QuizDisplay()
    



