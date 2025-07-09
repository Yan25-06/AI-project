import streamlit as st
import pickle
import os
import sys
from time import sleep
import matplotlib.image as mpimg
# Thêm thư mục cha của 'src' vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

def init_session_state():
    if "background" not in st.session_state:
        st.session_state.background = mpimg.imread(f"src/GUI/assets/Background.png")
    if "algorithm" not in st.session_state:
        st.session_state.algorithm = "Astar"
    if "map" not in st.session_state:
        st.session_state.map = "MAP_1"
    if "update_sol" not in st.session_state:
        st.session_state.update_sol = False
    if "steps" not in st.session_state or st.session_state.update_sol:
        st.session_state.is_playing = False
        st.session_state.update_sol = False
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "Solution", st.session_state.algorithm, f"{st.session_state.map}.pkl")
        try:
            with open(file_path, 'rb') as f:
                st.session_state.steps = pickle.load(f)
                st.session_state.curr_step = 0
                st.session_state.total_cost = get_total_cost(st.session_state.steps)
        except FileNotFoundError:
            st.error("❌ Solution file not found.")
            st.session_state.steps = []
    if "is_playing" not in st.session_state:
        st.session_state.is_playing = False
    if not st.session_state.steps:
        st.error("❌ No solution found.")
        st.session_state.is_playing = False
        return
def get_total_cost(state_path):
    total_cost = 0
    for i in range(1, len(state_path) - 4):
        total_cost += get_move_cost(state_path[i - 1], state_path[i])
    return total_cost
def get_move_cost(current_state, next_state, prev=False):
    for name, car in current_state.cars.items():
        other_car = next_state.cars[name]
        if (car.x, car.y) != (other_car.x, other_car.y):
            return car.length if not prev else -car.length
    return 0
# cập nhật solution khi thay đổi lựa chọn selectbox
def update_solution():
    st.session_state.update_sol = True

def update_current_step():
    if st.session_state.is_playing:
        if st.session_state.curr_step < len(st.session_state.steps) - 1:
            st.session_state.curr_step += 1
            sleep(0.05)
            st.rerun()
        else:
            st.session_state.is_playing = False
            st.rerun()