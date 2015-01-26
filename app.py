#!/usr/bin/python

import os, analyze
from flask import Flask, render_template, jsonify, request

class MyServer(Flask):

    def __init__(self, *args, **kwargs):
        super(MyServer, self).__init__(*args, **kwargs)    

app = MyServer(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
    return render_template("index.html")         

@app.route('/uploadInfo', methods=['POST'])
def uploadInfo():

    if request.method == 'POST':

    	entity, document = analyze.runAnalyzer(request.form['query'], request.form['count'])

    	return jsonify({"entity":entity, "document":document})       

    return jsonify({"success":False})       

if __name__ == "__main__":
	
	port = int(os.environ.get('PORT', 5000)) 
	app.run(host='0.0.0.0', port=port)	
