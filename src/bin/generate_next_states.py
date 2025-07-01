import streamlit as st
import sys
import os
from pathlib import Path

# Add the src directory to Python path for imports
current_dir = Path(__file__).parent
src_dir = current_dir.parent
project_root = src_dir.parent
sys.path.insert(0, str(src_dir))
sys.path.insert(0, str(project_root))

try:
    from game.game import Board
    from helper.solver_factory import initialize_solver
except ImportError:
    # Try alternative import paths
    try:
        from src.game.game import Board
        from src.helper.solver_factory import initialize_solver
    except ImportError:
        # If still failing, try absolute imports
        import sys
        sys.path.append(str(project_root / "src"))
        from game.game import Board
        from helper.solver_factory import initialize_solver

def board_to_html(board):
    """Convert board matrix to HTML table with styling"""
    matrix = board.to_matrix()
    
    html = "<table style='border-collapse: collapse; margin: 10px auto;'>"
    for row in matrix:
        html += "<tr>"
        for cell in row:
            color = get_car_color(cell)
            html += f"<td style='width: 40px; height: 40px; border: 1px solid black; text-align: center; vertical-align: middle; background-color: {color}; font-weight: bold; font-size: 16px;'>{cell}</td>"
        html += "</tr>"
    html += "</table>"
    return html

def get_car_color(car_name):
    """Get color for each car"""
    colors = {
        'R': '#FF6B6B',  # Red car - red
        'A': '#4ECDC4',  # Car A - teal
        'B': '#45B7D1',  # Car B - blue
        'C': '#96CEB4',  # Car C - green
        'D': '#FFEAA7',  # Car D - yellow
        'E': '#DDA0DD',  # Car E - plum
        'F': '#98D8C8',  # Car F - mint
        '.': '#F7F7F7'   # Empty space - light gray
    }
    return colors.get(car_name, '#E0E0E0')

def generate_states_by_depth(initial_board, max_depth):
    """Generate states organized by depth level with parent tracking"""
    all_states_by_depth = {}
    
    # Level 0: Initial state
    all_states_by_depth[0] = [(initial_board, None, 0)]  # (state, parent_index, parent_depth)
    
    # Generate states for each depth level
    for depth in range(1, max_depth + 1):
        current_level_states = []
        previous_level = all_states_by_depth[depth - 1]
        
        for parent_idx, (parent_state, _, _) in enumerate(previous_level):
            next_states = parent_state.generate_next_states()
            for next_state in next_states:
                current_level_states.append((next_state, parent_idx, depth - 1))
        
        all_states_by_depth[depth] = current_level_states
        
        # Stop if no new states found
        if not current_level_states:
            break
    
    return all_states_by_depth

def display_states_grid(states_with_parents, title, max_cols=4):
    """Display states in a grid layout with parent information"""
    if not states_with_parents:
        st.warning(f"No states found for {title}!")
        return
        
    st.subheader(f"{title} ({len(states_with_parents)} states)")
    
    # Calculate grid layout
    num_states = len(states_with_parents)
    cols_per_row = min(max_cols, num_states)
    rows_needed = (num_states + cols_per_row - 1) // cols_per_row
    
    # Display states in grid
    for row in range(rows_needed):
        cols = st.columns(cols_per_row)
        for col_idx in range(cols_per_row):
            state_idx = row * cols_per_row + col_idx
            if state_idx < num_states:
                state, parent_idx, parent_depth = states_with_parents[state_idx]
                with cols[col_idx]:
                    if parent_idx is not None:
                        st.markdown(f"**State {state_idx + 1}**")
                        st.markdown(f"<small style='color: #666;'>From: Depth {parent_depth}, State {parent_idx + 1}</small>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"**Initial State**")
                    st.markdown(board_to_html(state), unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Rush Hour - Next States Generator", layout="wide")
    
    st.title("🚗 Rush Hour Puzzle - Next States Generator")
    
    # Sidebar for depth control
    st.sidebar.title("⚙️ Settings")
    depth = st.sidebar.slider("Expansion Depth", min_value=1, max_value=5, value=3, 
                              help="Number of levels to expand from the initial state")
    
    st.markdown("---")
    
    # Define the initial car configuration
    cars = {
        'R': {'x': 2, 'y': 0, 'length': 2, 'dir': 'H'},
        'A': {'x': 0, 'y': 0, 'length': 2, 'dir': 'H'},
        'B': {'x': 1, 'y': 3, 'length': 2, 'dir': 'V'},
        'C': {'x': 3, 'y': 1, 'length': 3, 'dir': 'H'},
    }

    board = Board(cars)
    
    # Display original state
    st.subheader("🎯 Original State (Depth 0)")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(board_to_html(board), unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Generate states by depth
    with st.spinner(f"Generating states up to depth {depth}..."):
        states_by_depth = generate_states_by_depth(board, depth)
    
    # Display states for each depth level
    total_states = 0
    for current_depth in range(1, depth + 1):
        if current_depth in states_by_depth and states_by_depth[current_depth]:
            states_with_parents = states_by_depth[current_depth]
            total_states += len(states_with_parents)
            
            st.markdown("---")
            display_states_grid(states_with_parents, f"🔄 Depth {current_depth}", max_cols=4)
        else:
            st.markdown("---")
            st.subheader(f"🔄 Depth {current_depth}")
            st.info(f"No new states found at depth {current_depth}")
            break
    
    # Summary
    st.markdown("---")
    st.subheader("📊 Summary")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Max Depth Reached", len(states_by_depth) - 1)
    
    with col2:
        st.metric("Total States Generated", total_states)
    
    with col3:
        final_depth = max(states_by_depth.keys())
        if final_depth > 0:
            final_count = len(states_by_depth[final_depth])
        else:
            final_count = 1  # Just the initial state
        st.metric(f"States at Depth {final_depth}", final_count)
    
    # Add legend
    st.markdown("---")
    st.subheader("🎨 Legend")
    legend_cols = st.columns(len(cars) + 1)
    car_names = list(cars.keys()) + ['.']
    car_labels = list(cars.keys()) + ['Empty']
    
    for i, (name, label) in enumerate(zip(car_names, car_labels)):
        with legend_cols[i]:
            color = get_car_color(name)
            st.markdown(f"""
            <div style='text-align: center;'>
                <div style='width: 40px; height: 40px; background-color: {color}; border: 1px solid black; margin: 0 auto; display: flex; align-items: center; justify-content: center; font-weight: bold;'>{name}</div>
                <small>{label}</small>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
