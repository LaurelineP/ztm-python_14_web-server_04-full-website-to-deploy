# ---------------------------------------------------------------------------- #
#                             STORING DATA TO FILES                            #
# ---------------------------------------------------------------------------- #
from datetime import datetime as date
import csv
import uuid
import os


# ------------------------- VARIABLES FOR REUSABILITY ------------------------ #
storing_filename = ".emulated-database"



# ------------------------ SAVE TO FILE EMAIL CONTENT ------------------------ #
class EmailData:
	def __init__(self, data):
		self.data = data

	
	# Stores data into csv file
	def store_to_csv(data):
		"""Stores email content data into a csv file ( fine.csv )

		Args:
			data ( dictionary ): email content data received to format for the file
		"""
		#  Using a dictionary to create
		# - headers with the dictionaries keys
		# - rows from the dictionary values
		data_row = {
			"date":  date.now(),		# added this to mimic more a db
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


	# Stores data into file
	def store_to_file(data):
		"""Stores email content data into a text file ( fine.txt )

		Args:
			data ( dictionary ): email content data received to format for the file
		"""
		with open('./.emulated-database.txt', 'a+') as file:
			email_content = f'''
			date: {date.now()}
			uuid: {uuid.uuid4()}
			email: {data["email"]}
			subject: {data["subject"]}
			message :
				{data["message"]}

			'''
			file.writelines(email_content)


