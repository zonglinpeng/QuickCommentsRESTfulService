
import pandas as pd
import pickle
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

def predict_comment(student_answer, num_comments, plog_id=0):
    #TODO: do with student_answer
    comments = []
    for _ in range(num_comments):
        #TODO implement the baseline model
        comments.expend([str(plog_id) + ": Good work!"])
    return comments

