from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

def format_date_joined(date):
    """Formats a date as Month, Year (e.g., Feb, 2021)"""
    return date.strftime("%B, %Y")

@app.route('/profile')
def profile():
    user_info = {
        "full-name": "Jahi Bennett",
        "username": "jahibennett",
        "location": "St.Catherine, Jamaica",
        "date_joined": format_date_joined(datetime.date(2019, 2, 7)),  # Example date
        "bio": "I am an asipiring cybersecurity anaylst and I am very passionate about coding and the lifestyle ahead.",
        "posts": 120,
        "followers": 350,
        "following": 180,
        "profile_image": "profile.jpg"
    }
    return render_template("profile.html", user=user_info)
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
