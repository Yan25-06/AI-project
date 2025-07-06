import streamlit as st
from state import update_solution
import cv2

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
        st.session_state.curr_step = 0
        st.session_state.total_cost = 0
        st.session_state.is_playing = False
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

def display_metrics():
    if st.session_state.curr_step <= len(st.session_state.steps) - 5:
        cur = st.session_state.curr_step
    else:
        cur = len(st.session_state.steps) - 5
    st.markdown(f"<h5 style='text-align:center;'>Step: {cur} / {len(st.session_state.steps) - 5} </h5>", unsafe_allow_html=True)
    st.divider()
    st.markdown(f"<h5 style='text-align:center;'>Total Cost: {st.session_state.total_cost}</h5>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<h5 style='text-align:center;'>Status</h5>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align:center;'>{'▶️ Playing' if st.session_state.is_playing else '⏸️ Paused'}</h2>", unsafe_allow_html=True)
def overlay_image(bg, img, x, y, w, h):
    # Resize img theo kích thước (w, h) trên nền
    img = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)
    if img.shape[2] == 4:  # ảnh có alpha
        alpha = img[:, :, 3] / 255.0
        for c in range(3):
            bg[y:y+h, x:x+w, c] = (1 - alpha) * bg[y:y+h, x:x+w, c] + alpha * img[:, :, c]
    else:
        bg[y:y+h, x:x+w] = img[:, :, :3]
    return bg

def draw_map(board):
    c1, c2, c3 = st.columns([1, 7, 1])
    with c2:
        size = board.size
        cell_size = 70  # mỗi ô vuông có kích thước 70px
        width = (size + 4) * cell_size
        height = size * cell_size

        # Tạo nền từ ảnh
        bg = cv2.imread("src/GUI/assets/Background.png")
        bg = cv2.resize(bg, (width, height))

        # Vẽ xe
        for name, car in board.cars.items():
            x, y = car.x, car.y
            dx = car.length if car.dir == 'H' else 1
            dy = car.length if car.dir == 'V' else 1

            px = x * cell_size
            py = y * cell_size
            pw = dx * cell_size
            ph = dy * cell_size

            img_path = f"src/GUI/assets/R.png" if name == 'R' else f"src/GUI/assets/{car.length}3.png"
            img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
            if car.dir == 'H':
                img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

            if img is not None:
                bg = overlay_image(bg, img, px, py, pw, ph)
            else:
                # Vẽ hình chữ nhật thay thế
                cv2.rectangle(bg, (px, py), (px + pw, py + ph), (150, 150, 150), -1)

        # BGR -> RGB để Streamlit hiển thị đúng màu
        st.image(cv2.cvtColor(bg, cv2.COLOR_BGR2RGB))