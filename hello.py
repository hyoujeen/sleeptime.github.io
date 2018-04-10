from flask import Flask, request, render_template, redirect, url_for
import sys
from Priority import output

app = Flask(__name__)

@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())

@app.route("/handle_data", methods=['POST'])
def handle_data():
	print(request.form)
	task1 = ' '.join([request.form["task1"].lower(), request.form['task2'].lower(), request.form['task3'].lower(), request.form['task4'].lower(), request.form['task5'].lower()])
	output1 = output(task1)
	return '<br>'.join(output1)

@app.route("/main.css")
def main_css_to_static():
	return redirect("/static/main_old.css")

@app.route("/planner.html")
def planner_html():
	return render_template('planner.html')
@app.route("/index.html")
def index_html():
	return render_template('index.html')
# @app.route("/contact.html")
# def contact_html():
# 	return render_template('contact.html')

@app.route("/")
def response():
	return index_html();
	#tutorial = """<form action= "/asdf" method="POST">
	#<input type=text name=user>
	#<input type=submit /></form>"""
	

