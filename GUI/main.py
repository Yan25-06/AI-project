import streamlit as st
import pandas as pd
from time import sleep


# 3.5 Interactive GUI (10 pts)
# • step-by-step, play/pause, reset, select algorithms.
# • info: step count and total cost. Display a message if no solution is found.
if __name__ == "__main__": 
    # Input data 
    steps = [1,2,3,4,5]  # Example steps, replace with actual steps from the solver
    curr_step = 0
    is_playing = False

    # Headers 
    st.title("🚗 Rush Hour Solver GUI")
    st.subheader("Step-by-step Solver")  

    # Algorithm Selection
    col1, col2 = st.columns([2, 1])
    with col1:
        algorithm = st.selectbox("Select Algorithm", ["A*", "Dijkstra", "BFS", "DFS"], index=0)
    with col2:
        st.write("")  # Empty space for alignment
        if st.button("🔄 Reset", key="reset"):
            # RESET logics 
            pass 
    
    st.divider()

    # Control Buttons in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("⏮️ Previous Step", key="prev_step", use_container_width=True):
            if curr_step > 0:
                curr_step -= 1

    with col2:
        if st.button("⏯️ Play", key="play", use_container_width=True): 
            is_playing = True 

    with col3:
        if st.button("⏸️ Pause", key="pause", use_container_width=True):
            is_playing = False

    with col4:
        if st.button("⏭️ Next Step", key="next_step", use_container_width=True): 
            if curr_step < len(steps) - 1:
                curr_step += 1

    st.divider()

    # Current INFO 
    info_col1, info_col2, info_col3 = st.columns(3)
    
    with info_col1:
        st.metric("Current Step", curr_step)
    
    with info_col2:
        st.metric("Total Steps", len(steps))
    
    with info_col3:
        status = "▶️ Playing" if is_playing else "⏸️ Paused"
        st.metric("Status", status)


    # handle auto play  
    if is_playing:
        if curr_step < len(steps) - 1:
            curr_step += 1  
            print(f"Playing step {curr_step + 1} of {len(steps)}")
            sleep(1)  # Simulate delay for auto play
        else:
            is_playing = False  # Stop playing when reaching the last step