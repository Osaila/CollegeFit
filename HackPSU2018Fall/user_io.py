questions_sen = ["Do you like soccer? 1 = it is the worst sport ever, 5 = soccer is awesome ", "How do you feel about physics? 1 = yuck, 5 = physics is the best "]
questions_sal = ["Do you care about soccer? 1 = I don't care at all, 5 = soccer is like water, a necessity ", "Do you care about having a good physics department? 1 = it doesn't matter for my major, 5 = physics is my life "]
salience = ['']*len(questions_sal)
sentiment = ['']*len(questions_sen)
print(len(questions_sal))
print(len(questions_sen))
for i in [0,1]:
    print(i)
    salience[i] = float(input(questions_sal[i]))*0.1
for j in [0,1]:
    sentiment[j] = float(input(questions_sen[j]))*0.2
print(salience)
print(sentiment)
