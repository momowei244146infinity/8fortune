import streamlit as st
from base_data import *
import random


QUIZ = ["pillar_melody", "melody_pillar", "pillar_period", "nobel_man_forward", "nobel_man_backward"]

QUIZ_DICT = {
    "pillar_melody": {
        "question": 'What\'s the melody of {item}',
        "q_source_lst": pillar,
        "q_item_cnt":1,
        "answer_dict": pillar_melody_dic,
        "answer_input_cnt": 1,
        "answer_item": "melody",
        "option_lst": melody
    },
    "melody_pillar": {
        "question": "What's the pillar of {item}",
        "q_source_lst": melody,
        "q_item_cnt":1,
        "answer_dict": melody_pillar_dic,
        "answer_input_cnt": 2,
        "answer_item": "pillar",
        "option_lst": pillar
    },
    "pillar_period": {
        "question": "Are {item} in the same period?",
        "q_source_lst": pillar,
        "q_item_cnt":2,
        "answer_input_cnt": 1,
        "answer_item": "pillar",
        "option_lst": ["Yes", "No"]
    },
    "nobel_man_forward": {
        "question": "Which grounds do noble men of sky {item} exist?",
        "q_source_lst": sky,
        "q_item_cnt":1,
        "answer_dict": nobel_man_forward,
        "answer_input_cnt": 2,
        "answer_item": "ground",
        "option_lst": ground
    },
    "nobel_man_backward": {
        "question": "Ground {item} exists noble men for which sky?",
        "q_source_lst": ground,
        "q_item_cnt":1,
        "answer_dict": nobel_man_backward,
        "answer_input_cnt": 2,
        "answer_item": "sky",
        "option_lst": sky
    }
}

class QuizDis:

    def __init__(self):
        if st.button("Go to Pillar Melody Quiz"):            
            quiz0 = QUIZ[0]                       
            self.display(quiz0)
            #pillar_random = self.get_random_lst_q1()
            #self.display_q(quiz0, pillar_random)
        
        if st.button("Go to Melody Pillar Quiz"):            
            quiz1 = QUIZ[1]
            self.display(quiz1)
            #melody_random = self.get_random_lst_q2()
            #self.display_q(quiz1, melody_random)
        
        if st.button("Go to Pillar Period Quiz"):            
            quiz2 = QUIZ[2]            
            self.display(quiz2)
            #pillar_period_random = self.get_random_lst_q3()
            #self.display_q(quiz2, pillar_period_random)
        
        if st.button("Go to Nobel Man Forward Quiz"):            
            quiz3 = QUIZ[3]            
            self.display(quiz3)
        
        if st.button("Go to Nobel Man Backward Quiz"):
            quiz4 = QUIZ[4]            
            self.display(quiz4)
            
    
    def display_sub(self, 
                  quiz_choice:str, 
                random_lst:list
                  ):
        try:
            q_item, correct_answer = self.question(quiz_choice, random_lst)
            user_input_lst = self.input(quiz_choice)                    
            if st.button("Submit"):
                self.submit(q_item, correct_answer, user_input_lst, quiz_choice)
            
            if st.button("Next Question", key=f"{quiz_choice}_{st.session_state[f'{quiz_choice}_cnt']}", \
                        disabled=not st.session_state[f'{quiz_choice}_answered']):
                self.next(quiz_choice, random_lst)
        except IndexError:
            st.write("You have answered all questions in this round.")
            st.write("Let's review now!")
            if st.button("Review Round Answers"):
                self.review(quiz_choice)
            if st.button("Reset Round"):
                self.reset(quiz_choice)
                st.cache_data.clear()
                st.rerun(scope="fragment")

    
    @st.dialog(' ', width='large')
    def display(self, 
                  quiz_choice:str#,
                #random_lst:list
                  ):
        st.title(f'Welcome come to {QUIZ_DICT[quiz_choice]["answer_item"].replace("_", " ").capitalize()} Quiz')
        if f"{quiz_choice}_answered" not in st.session_state:
            self.reset(quiz_choice)
        
        st.write("How many rounds do you want to take?")
        num = st.number_input("Input a number", value=st.session_state[f"{quiz_choice}_round"], format="%d", step=1, key=f"{quiz_choice}_round_input")
        st.session_state[f"{quiz_choice}_round"] = num
        random_lst = self.generate_random_list(quiz_choice, num)

        if num == 0:
            st.write()
        
        else:
            st.write(f"OK! You are gonna take {st.session_state[f'{quiz_choice}_round']} challenges. \
                     You still have {st.session_state[f'{quiz_choice}_round'] - st.session_state[f'{quiz_choice}_cnt']} remained.")            
            self.display_sub(quiz_choice, random_lst)
                      
       
    def reset(self, quiz_choice:str):
        st.session_state[f"{quiz_choice}_answered"] = False
        st.session_state[f"{quiz_choice}_cnt"] = 0
        st.session_state[f"{quiz_choice}_correct_cnt"] = 0
        st.session_state[f"{quiz_choice}_wrong_record"] = []
        st.session_state[f"{quiz_choice}_round"] = 0
    
   
    @st.cache_data(show_spinner="Generating random list")
    def generate_random_list(_self, quiz_choice:str, round:int):
        q_source_lst = QUIZ_DICT[quiz_choice]["q_source_lst"]
        multi = QUIZ_DICT[quiz_choice]["q_item_cnt"]
        res = []
        size = len(q_source_lst)
        rest = (round * multi) % size
        loops = (round * multi) // size + 1
        for i in range(loops):
            if i + 1 < loops:
                res.extend(random.sample(q_source_lst, size))
            else:
                res.extend(random.sample(q_source_lst, rest))
        return res

    def question(self, 
                 quiz_choice:str, 
                 random_lst:list):
        index = st.session_state[f"{quiz_choice}_cnt"]
        if quiz_choice == 'pillar_period':
            q_item1 = random_lst[2*index]
            q_item2 = random_lst[2*index+1]
            q_item = [q_item1, q_item2]
            correct_answer = self.is_same_period(q_item1, q_item2)
        else:
            q_item = [random_lst[index]]
            correct_answer = QUIZ_DICT[quiz_choice]["answer_dict"][q_item[0]]  
        
        q_item_color = [self.change_item_color(item) for item in q_item] 
        q = QUIZ_DICT[quiz_choice]["question"].format(item=' and '.join(q_item_color))   
        
        st.markdown(q, unsafe_allow_html=True)

        return q_item, correct_answer if isinstance(correct_answer, list) else [correct_answer]
    
            
    def input(self, quiz_choice:str) ->list:
        key = 1
        user_input_lst = []
        input_cnt = QUIZ_DICT[quiz_choice]["answer_input_cnt"]
        option_lst = QUIZ_DICT[quiz_choice]["option_lst"]
        for col in st.columns(input_cnt):
            with col:
                user_input = st.selectbox(
                    "select an answer",
                    options=option_lst,
                    index=None,
                    key=f"{quiz_choice}_input_{str(key)}_{st.session_state[f'{quiz_choice}_cnt']}",
                    label_visibility="collapsed"
                )
                if user_input in ["Yes", "No"]:
                    answer_map = {"Yes": True, "No": False}
                    user_input = answer_map[user_input]
            key += 1
            user_input_lst.append(user_input)
        return user_input_lst
    
    def is_same_period(self, pillar1:str, pillar2:str)->bool:
        idx_pillar1 = pillar.index(pillar1)
        idx_pillar2 = pillar.index(pillar2)
        period1 = idx_pillar1 // 12
        period2 = idx_pillar2 // 12
        return period1 == period2

    
    def submit(self, 
               q_item:list, 
               correct_answer:list, 
               user_input_lst:list, 
               quiz_choice:str):
        st.session_state[f"{quiz_choice}_cnt"] += 1
        st.session_state[f"{quiz_choice}_answered"] = True

        if set(correct_answer) != set(user_input_lst):
            if QUIZ_DICT[quiz_choice][ "q_item_cnt"] == 2:
                q_item1, q_item2 = q_item
                st.error(f"Wrong! {q_item1} and {q_item2} are {'not ' if not correct_answer else ''} in the same period.")
            else:
                st.error(f"Wrong! The correct answer is {' and '.join(correct_answer)}")
            st.session_state[f"{quiz_choice}_wrong_record"].append((q_item, user_input_lst, correct_answer))
        else:
            st.session_state[f"{quiz_choice}_correct_cnt"] += 1
            st.success(f"Correct!")
    
    def next(self, quiz_choice:str, random_lst:list):
        st.session_state[f"{quiz_choice}_answered"] = False
        st.rerun(scope="fragment")
        
        
    def review(self,  quiz_choice:str):
        answer_item = QUIZ_DICT[quiz_choice]["answer_item"]
        st.write(f"Let's review {str(st.session_state[f'{quiz_choice}_cnt'])} questions you answered.")
        correct = st.session_state[f"{quiz_choice}_correct_cnt"]
        wrong = st.session_state[f"{quiz_choice}_cnt"] - correct
        st.write(f"You got {correct} correct and {wrong} wrong.")
        for item in st.session_state[f"{quiz_choice}_wrong_record"]:
            q_item, user_input_lst, correct_answer = item

            # not sure if this is corrected method
            q_item = [self.change_item_color(i) for i in q_item]
            user_input_lst = [self.change_item_color(i) for i in user_input_lst]
            correct_answer = [self.change_item_color(i) for i in correct_answer]
            
            if quiz_choice == "pillar_period":
                q_item1, q_item2 = q_item
                m = f'{q_item1} and {q_item2} are {"not " if not correct_answer else ""} in the same period.'
            elif quiz_choice == "nobel_man_forward":
                m = f'Nobel men of {q_item[0]} exists in ground \
                         {" and ".join(correct_answer)}, not {" and ".join(user_input_lst)}'
            elif quiz_choice == "nobel_man_backward":
                m = f'Ground {q_item[0]} exists nobel man for {" and ".join(correct_answer)}, \
                    not {" and ".join(user_input_lst)}'
            else:
                m = f'{answer_item.capitalize()}{"s" if len(correct_answer)<2 else ""}\
                        of {q_item[0]} {"is" if len(correct_answer)<2 else "are"} \
                        {" and ".join(correct_answer)}, not {" and ".join(user_input_lst)}'
            st.markdown(m, unsafe_allow_html=True)

    def _change_item_color(self, item:str):
        color_item = ""
        for c in item:
            color_item += color_dic[c]
        return color_item
    
    def change_item_color(self, item:str):
        return self._change_item_color(item) if item in pillar \
                                            or item in sky or item in ground \
                                            else item



    ################# method junkyard ##################################
    @st.dialog('Lets start the quiz', width='large')
    def display_orig(self, 
                  quiz_choice:str, 
                random_lst:list
                  ):
        if f"{quiz_choice}_answered" not in st.session_state:
            self.reset(quiz_choice)
        
        #self.round_set(quiz_choice)
        
        q_item, correct_answer = self.question(quiz_choice, random_lst)
        user_input_lst = self.input(quiz_choice)
                
        if st.button("Submit"):
            self.submit(q_item, correct_answer, user_input_lst, quiz_choice)
        
        if st.button("Next Question", key=f"{quiz_choice}_{st.session_state[f'{quiz_choice}_cnt']}", \
                     disabled=not st.session_state[f'{quiz_choice}_answered']):
            self.next(quiz_choice, random_lst)
              
        if st.button("Review Round Answers"):
            self.review(quiz_choice)
                
        if st.button("Reset Round"):
            self.reset(quiz_choice)

        # get data
    @st.cache_data(show_spinner="Getting random list")
    def get_random_lst_q1(_self) -> list:
        pillar_random = random.sample(list(pillar), len(pillar))
        return pillar_random

    @st.cache_data(show_spinner="Getting random list")
    def get_random_lst_q2(_self) -> list:
        melody_random = random.sample(list(melody), len(melody))
        return melody_random
    
    @st.cache_data(show_spinner="Getting random list")
    def get_random_lst_q3(_self) -> list:
        pillar_period_random = random.sample(list(pillar), len(pillar))
        return pillar_period_random
         

if __name__ == "__main__":   
    QuizDis()
        


