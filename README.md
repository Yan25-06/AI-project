run-gui:
	python -m streamlit run src/GUI/main.py

run_test: 
	python -m src.test.test

install: 
	pip install -r requirements.txt
