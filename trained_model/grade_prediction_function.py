
import pandas as pd
import numpy as np
import pickle
import random
# student_answer = ['this is an example, the answer id 3245.347 - 2346 +43534 = 100']#, ['asd asgsad the dog 12 is ']])[0]
### LOAD THE TRAINED tfidf
def predict_grade(student_answer):
    load_count_vect2= pickle.load(open('./trained_model/count_vectorizer_vocab2', 'rb'))
    counting_words_test_traditional = load_count_vect2.transform(student_answer)
    load_tfidf = pickle.load(open('./trained_model/tfidf_model', 'rb'))
    counting_words_test_traditional = load_count_vect2.transform(student_answer)
    term_freq_words_traditional = load_tfidf.transform(counting_words_test_traditional)
    loaded_trained = pickle.load(open('./trained_model/grading_model.sav', 'rb'))
    prediction = loaded_trained.predict(term_freq_words_traditional) # this for now, to predict the grade
    return prediction[0]
    # grade_answer(practice_text)

# predict_grade(student_answer)

# predict_grade()
# prediction

def predict_comment(student_answer, num_comments, problem_ID, teacher_ID):
    # do with student_answer
    grade_prob = predict_grade([student_answer])
    grade = np.where(grade_prob == 1.0)[0][0] + 1
    print("PREDICTED GRADE: " + str(grade)) # DEBUG
    # baseline model based on grades
    comments = get_comment_by_grade(grade, num_comments)
    # # baseline model of netural generic comment
    # generic_comment = get_comment_by_grade(3, 1)
    # comments.extend(generic_comment)
    return comments

def get_comment_by_grade(grade, num_comments):
    # TODO: populate comment lib
    sample = {
        0:["c0-0", "c0-1", "c0-2", "c0-3"],
        1:["c1-0", "c1-1", "c1-2", "c1-3"],
        2:["c2-0", "c2-1", "c2-2", "c2-3"],
        3:["b3-0", "b3-1", "b3-2", "b3-3"],
        4:["b4-0", "b4-1", "b4-2", "b4-3"],
        5:["a5-0", "a5-1", "a5-2", "a5-3"]
    }
    comments_set = sample[grade]
    comments = []
    for i in range(num_comments): 
        comments.append(comments_set[random.randint(0,3)])
    print("PREDICTED COMMENTS:" + ' '.join(map(str,comments))) # DEBUG
    return comments