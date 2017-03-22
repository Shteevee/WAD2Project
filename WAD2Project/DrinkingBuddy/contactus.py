#
# SendGrid
#

import sendgrid
import os
from sendgrid.helpers.mail import *

def send_mail(firstname, lastname, email, subject, message):
	"""
	Sends an e-mail message to the Drinking Buddy e-mail address with the details provided.
	"""
	sg = sendgrid.SendGridAPIClient(apikey="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")
	
	data = {
	  "personalizations": [
		{
		  "to": [
			{
			  "email": "DrinkingBuddyTeamE@gmail.com"
			}
		  ],
		  "subject": subject
		}
	  ],
	  "from": {
		"email": email
	  },
	  "content": [
		{
		  "type": "text/plain",
		  "value": "From: {firstname} {lastname}\r\n\r\n{message}".format(firstname=firstname, lastname=lastname, message=message)
		}
	  ]
	}
		
	response = sg.client.mail.send.post(request_body=data)