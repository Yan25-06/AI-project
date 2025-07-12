Creation of virtual environments (optional but recommended):
	https://docs.python.org/3/library/venv.html#module-venv

install: 
	pip install -r requirements.txt
	
run-gui:
	python -m streamlit run src/GUI/main.py
	or
	python3 -m streamlit run src/GUI/main.py

run_test: 
	python -m src.test.test
	or
	python3 -m src.test.test
