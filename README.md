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
- Create a github repository for the deployment
	- create a new repository - the repository would be cloned from python anywhere bash
	- prepare your local project to be pushed to Github
		- in project terminal - save environment's requirements: `pip freeze > requirements.txt`
		see doc: https://pip.pypa.io/en/stable/cli/pip_freeze/
		- copy all previous code except `venv` and `__pycache__` folders  
		and files `.emulated-database` files
		*A new environment will be built into python anywhere*
		*the program will be able to generate both files when*
		*an email will be sent*
		- push the project to the new repository
- Import project to python anywhere
	- in python anywhere > Dashboard > Consoles > bash
	- clone the repository ( https way )
	- in files tab: all the project files would be loaded and listed in this tab
	- in web tab: add a new web app
		- Create a new web app modal/your web app domain name explanation: click next 
		- Create a new web app modal/select a python framework > manual configuration
		- Create a new web app modal/select a python version ( the one used by the project )
		- Create a new web app modal/manual configuration information WSGI ( the one used by the project ) > next
		- Now a redirection is made to the web tab with a new link toward the new domain created
		```LaurelineP.pythonanywhere.com```
		This is a pre-setted web app that is currently served
- Configure the environment with imported project
	Python anywhere with flask: https://help.pythonanywhere.com/pages/Flask/
	- in Consoles > bash
		- create a virtual env: `mkvirtualenv --python=/usr/bin/python3.10 my-virtualenv`
		- install flask: `pip install flask`
		- install any other dependencies if needed : `cd <project-folder> && pip install -r requirements.txt` ( did not work from requirements )
		- indicate it will work with which environment : `workon my-virtualenv`
	- in Web tab
		- go to section virtual env and add the name of the virtual environment folder: `my-virtualenv`
		- reload the app ( domain will be serve with flask from that env ) / still not the project updated with the project content
		- go to code section > click on link WGSI configuration file to modify it
			- remove everything but the # Flask commented part
			- uncomment path variable
			- adjust path with the name of your folder
			- uncomment `if` condition
			- uncomment `from __main__ ...`
			- replace `from __main__ ... line` with `from app import app as application`
			```py
			import sys
			
			path = '/home/LaurelineP/ztm-python_14_web-server_04-full-website-to-deploy'
			if path not in sys.path:
				sys.path.append(path)

			from app import app as application
			```

			- save the file
		- go back to web tab and "reload <app-url>"
		- once reloaded > click on the link and the app would be available

App link : https://LaurelineP.pythonanywhere.com


### Resources: 
How requirements.txt works: https://www.idkrtm.com/what-is-the-python-requirements-txt/