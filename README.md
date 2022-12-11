## HOW TO RUN THIS FOLDER
### FOLDER 04-full-website-to-deploy
- Set the terminal's location: `cd 14_web-server/04-full-website-to-deploy`
- Run flask router/server: 
	- if the main script is called `app.py`: `flask run` ( this is the case )
	- if the main script is called `<smth>.py`: 
		- in your terminal set a global variable for Flask to read the correct file:
		`FLASK_APP=<filename>.py`
		- then run `flask run`
- If .txt or .csv files are present and want to witness the creation of them - remove them  
✅ The code supports the file creation when a mail would have been sent through the website
( Those files are mimicking a database storage / here it allows to not loose emails sent )
- Otherwise any email sent would be aggregated to the files ( both .txt and .csv files )

## DEPLOYING A PYTHON SERVER
Python anywhere: https://www.pythonanywhere.com/
Python anywhere is a cloud service that allows one to
host a python server
For the free tier it will auto generate the domain name
( it is customizable if one pays their services )

- Create a free account at python anywhere
- Dashboard > All web apps > Open Web Tab
- Bash
- in parallel in your folders
	- create a new repository - the repository would be cloned from python anywhere
	- in project terminal - save environment's requirements: `pip freeze > requirements.txt`
	see doc: https://pip.pypa.io/en/stable/cli/pip_freeze/
	- copy all previous code except `venv` and `__pycache__` folders  
	and files `.emulated-database` files
	*A new environment will be built into python anywhere*
	*the program will be able to generate both files when*
	*an email will be sent*
