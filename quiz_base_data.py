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
