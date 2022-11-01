import pickle

def prediction_model(pclass, sex, age, sibsp, parch, fare, embarked):
    x = [[pclass, sex, age, sibsp, parch, fare, embarked]]
    rf = pickle.load(open('titanic/titanic_model.sav', 'rb'))
    prediction = rf.predict(x)
    return prediction