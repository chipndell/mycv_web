from flask import Flask, render_template, request, flash, redirect, get_flashed_messages
from .forms import ContactForm
from .email import send_email_notification

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ("MYCV_WEB_APP_SECRET")

@app.route('/', methods=["GET","POST"])
def index():
	form = ContactForm(request.form)
	if request.method == 'POST':
		f_name = form.f_name.data
		l_name = form.l_name.data
		email_address = form.email.data
		subject = form.subject.data
		body = form.message.data 
		flash("Your message has been received. Thanks for Feedback. Make sure confirmation email is not spammed!", "info")
		send_email_notification(email_address, subject, body)
		return redirect("/")
	else:
		return render_template('index.html', form=form)

