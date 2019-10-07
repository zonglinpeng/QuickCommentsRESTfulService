# QUICK Comments RESTful APIs

### Instructions
run by: ./app.py

### HTTP Request
http://127.0.0.1:5000/comment/

### Install
- flask
- psycopg2
- nltk

### Description
- app.py: where Flask APIs are stored. /comment/ query is used to get requests.
- trained_model/grade_prediction_function.py: where grades and/or comments are generated

### Jsons
#####  -- Request -- 
```
[
    {
        "user_ID": 111,
        "plog_ID": 0,
        "answer_text": "answer1",
        "num_comments": 1
    },
    {
        "user_ID": 111,
        "plog_ID": 1,
        "answer_text": "answer2",
        "num_comments": 1
    }
]
```
#####  -- Response -- 
```
[
   {
       "plog_id": 0,
       "comments": [
           "comments1",
           "comments2",
           "comments3"
       ]
   },
   {
       "plog_id": 1,
       "comments": [
           "comments1",
           "comments2",
           "comments3"
       ]
   }
]
```

