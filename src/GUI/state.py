import streamlit as st
import pickle
import os
import sys
from time import sleep
import matplotlib.pyplot as plt
# Thêm thư mục cha của 'src' vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

def init_session_state():
    if "algorithm" not in st.session_state:
        st.session_state.algorithm = "Astar"
    if "map" not in st.session_state:
        st.session_state.map = "MAP_1"
    if "update_sol" not in st.session_state:
        st.session_state.update_sol = False
    if "steps" not in st.session_state or st.session_state.update_sol:
        st.session_state.update_sol = False
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "Solution", st.session_state.algorithm, f"{st.session_state.map}.pkl")
        try:
            with open(file_path, 'rb') as f:
                st.session_state.steps = pickle.load(f)
                st.session_state.curr_step = 0
        except FileNotFoundError:
            st.error("❌ Solution file not found.")
            st.session_state.steps = []
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

# cập nhật solution khi thay đổi lựa chọn selectbox
def update_solution():
    st.session_state.update_sol = True

def update_current_step():
    if st.session_state.is_playing:
        if st.session_state.curr_step < len(st.session_state.steps) - 1:
            st.session_state.curr_step += 1
            st.rerun()
        else:
            st.session_state.is_playing = False
            st.rerun()