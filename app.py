from flask import Flask, Blueprint, jsonify, request, render_template, url_for, flash, redirect

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/recommendations')
def recs():
    return render_template('recommendations.html')

if __name__ == '__main__':
    application.run(debug=True)