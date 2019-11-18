#!/usr/bin/env python
"""QUICK Comments RESTful APIs
Give comments based on the given student answers
and the number of comments
"""
import os
import numpy as np
import json as js
from flask import Flask, request, render_template, jsonify, session, Markup
from trained_model.grade_prediction_function import predict_grade, predict_comment

__author__ = "Zonglin Peng, Rui Huang, and Meghana K V"
__copyright__ = "Copyright 2019, The ASSISTments Project"
__license__ = "GPL"
__version__ = "1.0.1"
__status__ = "Production"


'''MACRO'''
app = Flask(__name__)
app.secret_key = os.urandom(20)


'''HELPER'''
<<<<<<< HEAD
def get_comment_prediction(answer, num_comments, problem_ID, techer_ID):
    comment_prob = predict_comment(answer, num_comments, problem_ID, techer_ID)
=======
def get_comment_prediction(answer, num_comments, problem_ID):
    comment_prob = predict_comment(answer, num_comments, problem_ID)
>>>>>>> 737e3eb18ac257973e1fca9f88b56c4a5df05fcc
    return comment_prob


'''API CALL'''
@app.route("/comment/", methods=['POST'])
def commnent_me():
    response_list = []
    raw_req = request.get_data().decode("utf-8") # get JSON as string and decode
    # print(raw_req) # DEBUG
    # print(type(raw_req)) # DEBUG
    req = js.loads(raw_req) if(type(raw_req) == str) else raw_req
    # parse req
    for json in req:
        response_dict = {}
<<<<<<< HEAD
        problem_ID = json["problem_ID"] # not plog_ID
        techer_ID = json["teacher_ID"] 
=======
        problem_ID = json["problem_ID"]
        teacher_ID = json["teacher_ID"]
>>>>>>> 737e3eb18ac257973e1fca9f88b56c4a5df05fcc
        user_ID = json["user_ID"]
        answer_text = json["answer_text"]
        num_comments = json["num_comments"]
        # answer_text = Markup(answer_text).striptags()
        if not answer_text:
            print("NOTE: No answers are passed in")
        session["answer"] = answer_text.strip('<p>').strip('</p>') # remove paragraph tags
        # get comments
<<<<<<< HEAD
        comment_prob = get_comment_prediction(answer_text, num_comments, problem_ID, techer_ID)
=======
        comment_prob = get_comment_prediction(answer_text, num_comments, problem_ID)
>>>>>>> 737e3eb18ac257973e1fca9f88b56c4a5df05fcc
        # parse data
        response_dict["user_ID"] = user_ID
        response_dict["comments"] = comment_prob
        response_list.extend([response_dict])
    # parse into JSON
    session["comments"] = js.dumps(response_list)
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
