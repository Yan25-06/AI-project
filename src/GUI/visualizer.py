import streamlit as st
from state import steps
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def display_title():
    st.markdown("<h1 style='text-align: center;'>🚗 Rush Hour Solver GUI</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Step-by-step solver</h3>", unsafe_allow_html=True)
def display_selectbox():
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        algorithm = st.selectbox("Select Algorithm", ["A*", "UCS", "BFS", "DFS"], index=0)
def display_controls():
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

    if st.button("⏮️ Previous", key="prev", use_container_width=True):
        if st.session_state.curr_step > 0:
            st.session_state.curr_step -= 1
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
            st.rerun()
    if st.button("🔄 Reset", key="reset", use_container_width=True):
        st.session_state.steps = steps
        st.session_state.curr_step = 0
        st.session_state.is_playing = False
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

def display_metrics():
    st.markdown(f"<h5 style='text-align:center;'>Step: {st.session_state.curr_step} / {len(st.session_state.steps)} </h5>", unsafe_allow_html=True)
    st.divider()
    st.markdown(f"<h5 style='text-align:center;'>Total Cost: {len(st.session_state.steps)}</h5>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<h5 style='text-align:center;'>Status</h5>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align:center;'>{'▶️ Playing' if st.session_state.is_playing else '⏸️ Paused'}</h2>", unsafe_allow_html=True)
def draw_map(grid):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.write("")
    with col2:
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_xlim(0, 6)
        ax.set_ylim(0, 6)
        ax.set_aspect('equal')
        ax.axis('off')
        color_map = {
            '.': '#CCCCCC',    # đường xám
            'R': '#FF4C4C',    # xe đỏ (xe chính)
            'O': '#FF9900',    # xe cam
            'Y': '#FFD700',    # xe vàng
            'B': '#4DA6FF',    # xe xanh dương
            'G': '#77DD77'    # xe xanh lá
        }

        # Vẽ lưới và các xe
        for i in range(6):
            for j in range(6):
                value = grid[i][j]
                color = color_map.get(value, 'white')
                rect = patches.Rectangle((j, 5 - i), 1, 1, linewidth=1, edgecolor='none', facecolor=color)
                ax.add_patch(rect)
                if value != '.':
                    ax.text(j + 0.5, 5 - i + 0.5, '', color='black', weight='bold',
                            ha='center', va='center', fontsize=16)

        st.pyplot(fig)
    with col3:
        st.write("")