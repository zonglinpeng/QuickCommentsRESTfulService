#!/usr/bin/env python
"""QUICK Comments RESTful APIs
Give comments based on the given student answers
and the number of comments
"""
import os
import numpy as np
import json
from flask import Flask, request, render_template, jsonify, session, Markup
from trained_model.grade_prediction_function import predict_grade, predict_comment

__author__ = "Zonglin Peng, Rui Huang, and Meghana K V"
__copyright__ = "Copyright 2019, The ASSISments Project"
__license__ = "GPL"
__version__ = "1.0.1"
__status__ = "Production"


'''MACRO'''
app = Flask(__name__)
app.secret_key = os.urandom(20)


'''HELPER'''
def get_comment_prediction(answer, plog_ID):
    comment_prob = predict_comment(answer, plog_ID)
    return comment_prob


'''API CALL'''
@app.route("/comment/", methods=['POST'])
def commnent_me():
    response_list = []
    req = request.get_json()
    # parse req
    for json in req:
        response_dict = {}
        plog_ID = json["plog_ID"]
        answer_text = json["answer_text"]
        answer_number = json["num_comments"]
        # answer_text = Markup(answer_text).striptags()
        if not answer_text:
            print("NOTE: No answers are passed in")
        session["answer"] = answer_text
        # get comments
        comment_prob = get_comment_prediction(answer_text, plog_ID)
        # parse data
        response_dict["plog_id"] = plog_ID
        response_dict["comments"] = comment_prob
        response_list.extend([response_dict])
    # parse into JSON
    session["comments"] = json.dumps(response_list)
    print(session["comments"])
    return session["comments"]


@app.route("/_cleanup")
def cleanup():
    session.clear()

@app.route('/')
def hello_world():
    return 'Hello World!'

'''MAIN'''
if __name__ == '__main__':
    app.run()
