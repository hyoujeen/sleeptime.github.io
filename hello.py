from flask import Flask, request, render_template, redirect
import sys

app = Flask(__name__)

@app.route("/createschedule", methods=['POST'])
def handle_data():
	answer = "The answer is" +" " +request.form['user']
	return str(answer), render_template('planner.html')

@app.route("/main.css")
def main_css_to_static():
	return redirect("/static/main_old.css")

@app.route("/planner.html")
def planner_html():
	return render_template('planner.html')
@app.route("/index.html")
def index_html():
	return render_template('index.html')
@app.route("/contact.html")
def contact_html():
	return render_template('contact.html')

@app.route("/")
def response():
	return index_html();
	#tutorial = """<form action= "/asdf" method="POST">
	#<input type=text name=user>
	#<input type=submit /></form>"""
	

