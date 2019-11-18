
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
        1:["Your answer is not correct.", "Incorrect answer.", "Please focus more on details.", "Wrong answer.", "Your should work harder.", "I can help you."],
        2:["Your answer is partially correct.", "There is a more correct solution.","Partially incorrect answer.","Please focus more on details.", "You anwser is not necessarily correct.", "I can help you if you could provide some useful feedback please."],
        3:["Your answer is partially incorrect.", "You got 50 percent correct.", "You are half way through.", "You can improve on you answer.", "Partially incorrect answer.", "I can help you if you could provide some useful feedback please."],
        4:["Your answer is almost correct.", "Think more about details.", "You almost got there.", "Nice work, but some details are incorrect.", "Think more about the question.", "Minor issues are in your solution."],
        5:["Good work.", "Correct.", "Your answer is correct.", "Good solution.", "Good job.", "Nice work."]
    }
    comments_set = sample[grade]
    comments = []
    for i in range(num_comments): 
        comments.append(comments_set[random.randint(0,5)])
    print("PREDICTED COMMENTS:" + ' '.join(map(str,comments))) # DEBUG
    return comments