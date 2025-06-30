freeze-pip:
	pip freeze --local > requirements.txt

run-gui-test:
	python3 -m streamlit run GUI/main.py

install: 
	pip install -r requirements.txt