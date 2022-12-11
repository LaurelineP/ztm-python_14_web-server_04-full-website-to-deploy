# ---------------------------------------------------------------------------- #
#                                    ROUTING                                   #
# ---------------------------------------------------------------------------- #
from flask import Flask, render_template, request, redirect
from EmailData import EmailData


store_to_file = EmailData.store_to_file
store_to_csv = EmailData.store_to_csv



# ------------------------- VARIABLES FOR REUSABILITY ------------------------ #
assets_code_files = {
	"js" : "main.70a66962.js",
	"css": "main.3f6952e4.css",
}

# Flask instantiation
app = Flask(__name__)


# Provides index.html for the route "/" 
def set_entry_route():
	@app.route('/')
	def root_index():
		return render_template('index.html', fileNames = assets_code_files )


# Sets dynamically routes based on url param
def set_get_routes():
	@app.route('/<string:file_name_in_url>')
	def root(file_name_in_url):
		return render_template(file_name_in_url, fileNames = assets_code_files)


# Sets specific routes for POST requests
def set_post_routes():
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


# Mount the entire flask app server.
def set_server():
	""" Sets the server routing """
	set_entry_route()
	set_get_routes()
	set_post_routes()