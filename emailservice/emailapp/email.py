#functions to send email and access email logs from service providers

import requests


mg_url = "https://api.mailgun.net/v2/sandbox19d1102a39d9474882ba5d088fb4ed1b.mailgun.org/messages"
mg_api_key = "key-00c8c44e8e5c484cca408e79e252dcd7"

sg_url = "https://api.sendgrid.com/api/mail.send.json"
sg_api_key = "passisapikey"


def send_simple_message(sender, to, subject, text):

	#mailgun is default
	try:
		
		return requests.post(mg_url,
			auth=("api", mg_api_key),
			data={"from"	: "<" + sender + ">",
				"to"		: "<" + to + ">",
				"subject"	: subject,
				"text"		: text})
		
		#raise requests.exceptions.RequestException()

	
	except requests.exceptions.RequestException as e:
		#print e

		#sendgrid is the secondary
		try:
			return requests.post(sg_url,
			auth=("api", sg_api_key),
			data={"from"	: "<" + sender + ">",
				"to"		: "<" + to + ">",
				"subject"	: subject,
				"text"		: text})

		except requests.exceptions.RequestException as e:
			return e

	#debug return: this return value should never execute
	return -1

"""
def get_mg_logs():
	return requests.get(
		"https://api.mailgun.net/v2/samples.mailgun.org/events",
		auth=("api", mg_api_key),
		params={"event" : "rejected OR failed"})
"""

#print send_simple_message("ian.karambelas@gmail.com", "Hello", "This is a sample email")

#print get_mg_logs()
