run_main: 
	python3 -m src.main
run_toy:
	python3 -m src.bin.toy

run_streamlit_next_states_visualizers:
	streamlit run src/bin/generate_next_states.py

# run_gui: 
# 	python3 -m src.GUI.main

freeze-pip:
	pip freeze --local > requirements.txt

run-gui-test:
	python3 -m streamlit run src/GUI/main.py

install: 
	pip install -r requirements.txt

run_test_ucs: 
	python3 -m src.test.gen_test_ucs