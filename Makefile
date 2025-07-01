run_main: 
	python3 -m src.main
freeze-pip:
	pip freeze --local > requirements.txt