from DataSet import DS
import random

quesTypeText = {
    'FirstBless' : 'מהי הברכה הראשונה למקרה זה?',
    'LastBless' : 'מהי הברכה האחרונה למקרה זה?',
    'Special' : 'מהי ברכת הראייה למקרה זה?'
}

#the thing of the question about↓
TheThing = None



def generate_question():
    ques = {}
    TheThing = random.choice(DS)
    categs = get_cagtegories(TheThing)
    print(categs)
    quesType = random.choice(categs)
    ques['question'] = quesTypeText[quesType]
    ques['name'] = TheThing['Name']
    ques['img'] = TheThing['img']
    options = [TheThing[quesType]]
    while len(options) < 4:
        curo = random.choice(DS)
        if (not curo[quesType]):
            continue;
        if curo[quesType] in options:
            continue;
        options.append(curo[quesType])

    options.remove(TheThing[quesType])
    correct = random.randint(0, len(options))
    options.insert(correct, TheThing[quesType])
    ques['options'] = options
    ques['correct'] = correct
    return ques

def get_cagtegories(thing):
    categs = []
    if 'FirstBless' in thing:
        categs.append('FirstBless')
    if 'LastBless' in thing:
        categs.append('LastBless')
    if 'Special' in thing:
        categs.append('Special')
    return categs


if __name__ == '__main__':
    print(generate_question())


