import os
import csv
import uuid
from flask import Flask, render_template, request, redirect
from datetime import datetime as Date


# ------------------------- VARIABLES FOR REUSABILITY ------------------------ #
assets_code_files = {
	"js" : "main.70a66962.js",
	"css": "main.3f6952e4.css",
}
storing_filename = ".emulated-database"



# ---------------------------------------------------------------------------- #
#                                    ROUTING                                   #
# ---------------------------------------------------------------------------- #


# Classic routing - but we can observe repetitions --> repeated task could be done with loops
def set_classic_rooting():
	@app.route('/index', methods = ["GET"])
	@app.route('/index.html', methods = ["GET"])
	@app.route('/', methods = ["GET"])
	def root_home():
		return render_template('index.html', fileNames = assets_code_files )



	@app.route('/about')
	@app.route('/about.html')
	def root_about():
		return render_template('about.html')


	@app.route('/works')
	@app.route('/works.html')
	def root_woks():
		return render_template('works.html')


	@app.route('/contact')
	@app.route('/contact.html')
	def root_contact():
		return render_template('contact.html')



# Personal implementation: Uses for loop and os.walk to get files to get to 
def set_dynamic_routing():
	for _,_,f in os.walk('./templates/'):
		@app.route(f'/<f>', methods = ["GET"])
		def root(f):
			return render_template(f, fileNames = assets_code_files )


# Courses solution : routing with any file mention in url
def set_dynamic_routing_any():
	@app.route('/<string:file_name_in_url>')
	def root(file_name_in_url):
		return render_template(file_name_in_url, fileNames = assets_code_files)


# ---------------------------------------------------------------------------- #
#                             STORING DATA TO FILES                            #
# ---------------------------------------------------------------------------- #
# Stores data into file
def store_to_file(data):
	"""Stores email content data into a text file ( fine.txt )

	Args:
		data ( dictionary ): email content data received to format for the file
	"""
	with open('./.emulated-database.txt', 'a+') as file:
		email_content = f'''
		date: {Date.now()}
		uuid: {uuid.uuid4()}
		email: {data["email"]}
		subject: {data["subject"]}
		message :
			{data["message"]}

		'''
		file.writelines(email_content)



# Stores data into csv file
def store_to_csv(data):
	"""Stores email content data into a csv file ( fine.csv )

	Args:
		data ( dictionary ): email content data received to format for the file
	"""
	# -------------------------- Personal implementation ------------------------- #
	# data_row = [Date.now(), uuid.uuid4(), data['email'], data['subject'], data['message']]
	# with open('./.emulated-database.csv', 'w', newline='' ) as csvFile:
		# csv_writer = csv.writer(csvFile)
		# csv_writer.writerow(data_row)

	# -------------------------------- Alternative ------------------------------- #
	# Alternative ( from course [ without dates and uuid ] )
	date = Date.now()			# added this to mimic more a db
	_uuid = uuid.uuid4()		# added this to mimic more a db
	email = data['email']
	subject = data['subject']
	message = data['message']
	data_row = [ date, _uuid, email, subject, message ]

	# Alternative dig up: using a dictionary to create
	# - headers with the dictionaries keys
	# - rows from the dictionary values
	data_row = {
		"date":  Date.now(),		# added this to mimic more a db
		"uuid" : uuid.uuid4(),		# added this to mimic more a db
		"email" : data['email'],
		"subject" : data['subject'],
		"message" : data['message'],
	}

	# Prevents the program from exiting on edge cases ( added before video )
	try:
		CSV_PATH = f'./{storing_filename}.csv'

		# Helping to identify if the program needs to create csv file headers
		is_created = os.path.exists( CSV_PATH )

		# Creates / Edit the csv file to store data
		with open( CSV_PATH, 'a', newline='') as csvFile:
			csv_writer = csv.writer( csvFile, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL )

			# Writes csv header on creation only ( added because: .writeheader() not available using csv.writer as course suggests ) ()
			if not is_created: csv_writer.writerow(list( data_row.keys() ))

			# Writes a csv row with data
			csv_writer.writerow(list( data_row.values() ))

	except ValueError or AttributeError as error:
		print('error', error)
		pass




def handle_contact_request_route():
	"""Handles POST request for the Contact form"""
	@app.route('/submit_form', methods = ['POST'])
	@app.route('/submit_form.html', methods = ['POST'])
	def submit_form():
		if request.form:
			request_data = request.form.to_dict()
			store_to_file(request_data)
			store_to_csv(request_data)
			return redirect('thankyou.html')
		else:
			return 'Email content not received'




# ---------------------------------------------------------------------------- #
#                                  FINAL CODE                                  #
# ---------------------------------------------------------------------------- #
# ----------------------- Mounting server up and ready ----------------------- #

# Flask instantiation
app = Flask(__name__)

# Mount server
def mount_server():
	'''Set the server and serves it'''

	# Provides index.html for the route "/" 
	@app.route('/')
	def root_index():
		return render_template('index.html', fileNames = assets_code_files )

	# Provides routing for others templates "/<filename>"
	set_dynamic_routing_any()
	handle_contact_request_route()


	# set_classic_rooting()
	# set_dynamic_routing()



mount_server()
