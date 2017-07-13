from DataSet import DS
import random

quesTypeText = ['מהי הברכה הראשונה למקרה זה?',
             'מה מבין הבאים מתאים לברכה זו?']
quesTypes = [0, 1, 2]

#the thing of the question about↓
TheThing = None

ques = {}

def ask_first_blessQ():
    while True:
        TheThing = random.choice(DS)
        if hasattr(TheThing, 'FirstBless'):
            break
    ques['question'] = quesTypeText[0]
    ques['img'] = TheThing['img']
    options = []
    while len(options) < 3:
        curo = random.choice(quesTypes)
        if (not hasattr(curo, 'firstBless')):
            continue
        if curo['firstBless'] in options:
            continue
        options.append(curo['firstBless'])

    correct = random.randint(0, len(options))
    options.insert(correct, TheThing['firstBless'])

    ques['options'] = options
    ques['correct'] = correct

def generate_question():

    quesType = random.choice(quesTypes)

    if(quesType == quesTypes[0]):
        ask_first_blessQ()
    #elif


    return ques


