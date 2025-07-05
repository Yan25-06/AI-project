import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from state import update_solution, get_move_cost

def display_title():
    st.markdown("<h1 style='text-align: center;'>🚗 Rush Hour Solver GUI</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Step-by-step solver</h3>", unsafe_allow_html=True)
def display_selectbox():
    c1, c2, c3, c4, c5 = st.columns([1, 2, 0.5, 2, 1])
    with c2:
        st.selectbox("Select Algorithm", ["Astar", "UCS", "BFS", "DFS"], key="algorithm", on_change=update_solution, index=0)
    with c4:
        st.selectbox("Select Map", ["MAP_1", "MAP_2", "MAP_3", "MAP_4"], key="map", on_change=update_solution, index=0)
def display_controls():
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

    if st.button("⏮️ Previous", key="prev", use_container_width=True):
        if st.session_state.curr_step > 0:
            st.session_state.curr_step -= 1
            curr_step = st.session_state.curr_step
            st.session_state.total_cost += get_move_cost(st.session_state.steps[curr_step], st.session_state.steps[curr_step + 1], True)
            st.rerun()
    if st.button("⏯️ Play", key="play", use_container_width=True):
        st.session_state.is_playing = True
        st.rerun()
    if st.button("⏸️ Pause", key="pause", use_container_width=True):
        st.session_state.is_playing = False
        st.rerun()
    if st.button("⏭️ Next Step", key="next", use_container_width=True):
        if st.session_state.curr_step < len(st.session_state.steps) - 1:
            st.session_state.curr_step += 1
            curr_step = st.session_state.curr_step
            st.session_state.total_cost += get_move_cost(st.session_state.steps[curr_step - 1], st.session_state.steps[curr_step])
            st.rerun()
    if st.button("🔄 Reset", key="reset", use_container_width=True):
        st.session_state.curr_step = 0
        st.session_state.is_playing = False
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

def display_metrics():
    st.markdown(f"<h5 style='text-align:center;'>Step: {st.session_state.curr_step} / {len(st.session_state.steps) - 1} </h5>", unsafe_allow_html=True)
    st.divider()
    st.markdown(f"<h5 style='text-align:center;'>Total Cost: {st.session_state.total_cost}</h5>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<h5 style='text-align:center;'>Status</h5>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align:center;'>{'▶️ Playing' if st.session_state.is_playing else '⏸️ Paused'}</h2>", unsafe_allow_html=True)
def draw_map(board):
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        size = board.size
        if "fig" not in st.session_state or "ax" not in st.session_state:
            fig, ax = plt.subplots(figsize=(size + 4, size))
            st.session_state.fig = fig
            st.session_state.ax = ax
        else:
            fig = st.session_state.fig
            ax = st.session_state.ax
            ax.clear()
        ax.set_xlim(0, size + 4)
        ax.set_ylim(size, 0)
        ax.set_aspect('equal')
        ax.axis('off')

        # Vẽ nền
        bg_img = mpimg.imread(f"src/gui/assets/Background.png")
        ax.imshow(bg_img, extent=(0, size + 4, 0, size), zorder=0)
        # Vẽ xe
        for name, car in board.cars.items():
            x = car.x
            y = car.y 
            dx = car.length if car.dir == 'H' else 1
            dy = car.length if car.dir == 'V' else 1

            try:
                if car.name == 'R':
                    img = mpimg.imread(f"src/gui/assets/R.png")
                else:
                    img = mpimg.imread(f"src/gui/assets/{car.length}2.png")
                if car.dir == 'H':
                    img = np.rot90(img, k=3)
                ax.imshow(img, extent=(x, x+dx, y, y+dy), zorder=1)
            except FileNotFoundError:
                ax.add_patch(plt.Rectangle((x, y), dx, dy, color="gray"))
                ax.text(x + dx/2, y + dy/2, name, ha='center', va='center')
        st.pyplot(fig)