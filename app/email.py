import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_email_notification(email_address, subject, body):

	FROM_EMAIL_ADDRESS = os.environ("FROM_EMAIL_ADDRESS")
	FROM_EMAIL_PASSSWORD = os.environ("FROM_EMAIL_PASSSWORD")
	RECEIVER_EMAIL_ADDRESS = email_address

	subject_user = "Confirmation from cvmananbh9.herokuapp.com for Submitting feedback"
	body_user = "Thank you for your time and consideration. Your message have been recieved and will be worked upon."
	message_user = f'Subject: {subject_user} \n\n {body_user}'

	message_admin = f'Subject: {subject} \n\n {body}'

	smtp = smtplib.SMTP(host='smtp.office365.com', port="587")
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()
	smtp.login(FROM_EMAIL_ADDRESS, FROM_EMAIL_PASSSWORD)
	smtp.set_debuglevel(1)
	smtp.sendmail(FROM_EMAIL_ADDRESS, RECEIVER_EMAIL_ADDRESS, message_user)

	smtp.sendmail(FROM_EMAIL_ADDRESS, FROM_EMAIL_ADDRESS, message_admin)

	smtp.quit()
