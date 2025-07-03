import streamlit as st
from time import sleep

steps = [
    [   # Step 0
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', 'R', 'R', '.', '.'],
        ['.', '.', '.', 'Y', '.', '.'],
        ['.', '.', '.', 'Y', '.', '.'],
        ['.', '.', '.', 'Y', '.', '.']
    ],
    [   # Step 1
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', 'R', 'R', '.'],
        ['.', '.', '.', 'Y', '.', '.'],
        ['.', '.', '.', 'Y', '.', '.'],
        ['.', '.', '.', 'Y', '.', '.']
    ],
    [   # Step 2
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', 'R', 'R'],
        ['.', '.', '.', 'Y', '.', '.'],
        ['.', '.', '.', 'Y', '.', '.'],
        ['.', '.', '.', 'Y', '.', '.']
    ]
]
def init_session_state():
    if "steps" not in st.session_state:
        st.session_state.steps = steps
    if "curr_step" not in st.session_state:
        st.session_state.curr_step = 0
    if "total_cost" not in st.session_state:
        st.session_state.total_cost = 0 
    if "is_playing" not in st.session_state:
        st.session_state.is_playing = False
    if not st.session_state.steps:
        st.error("❌ No solution found.")
        st.session_state.is_playing = False
        return

def update_current_step():
    if st.session_state.is_playing:
        if st.session_state.curr_step < len(st.session_state.steps) - 1:
            sleep(.5)
            st.session_state.curr_step += 1
            st.rerun()
        else:
            st.session_state.is_playing = False
            st.rerun()