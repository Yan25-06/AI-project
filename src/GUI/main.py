import streamlit as st
from state import *
from config import PAGE_CONFIG
from visualizer import *

if __name__ == "__main__":
    # page config
    st.set_page_config(**PAGE_CONFIG)
    init_session_state()
    display_title()
    display_selectbox()
    
    col1, sep12, col2, sep23, col3 = st.columns([0.7, 0.1, 3, 0.2, 0.5])
    with sep12:
        st.markdown(
            "<div style='border-left: 2px solid #bbb; height: 400px; margin: auto'></div>",
            unsafe_allow_html=True,
        )
    with col2:
        draw_map(st.session_state.steps[st.session_state.curr_step])
    with col1:
        display_metrics()
    with sep23:
        st.markdown(
            "<div style='border-left: 2px solid #bbb; height: 400px; margin: auto'></div>",
            unsafe_allow_html=True,
        )
    with col3:
        display_controls()

    update_current_step()

    
    
