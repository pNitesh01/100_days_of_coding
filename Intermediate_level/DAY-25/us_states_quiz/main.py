import turtle
import pandas as pd
from state import State

IMAGE = 'blank_states_img.gif'
CSV_PATH = '50_states.csv'
GAME_TITLE = 'U.S. States Game'


data = pd.read_csv(CSV_PATH)
all_states = data.state.to_list()
total_num_of_states = len(all_states)
guessed_states = []

screen = turtle.Screen()
screen.title(GAME_TITLE)
screen.addshape(IMAGE)
turtle.shape(IMAGE)

while len(guessed_states) < total_num_of_states:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/{total_num_of_states} States Correct', prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        missing_states = []
        
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        State(int(state_data.x), int(state_data.y), answer_state)

