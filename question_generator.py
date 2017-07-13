from ds import DS
import random

quesTypeText = {
    'FirstBless' : 'מהי הברכה הראשונה על %s?',
    'LastBless' : 'מהי הברכה האחרונה על %s?',
    'Special' : 'מה מברכים על %s?'
}

#the thing of the question about↓
TheThing = None



def generate_question():
    ques = {}
    TheThing = random.choice(DS)
    categs = get_cagtegories(TheThing)
    quesType = random.choice(categs)
    ques['question'] = quesTypeText[quesType] % TheThing['Name']
    ques['name'] = TheThing['Name']
    ques['image'] = TheThing['Picture']
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
    ques['answers'] = options
    ques['correct'] = correct
    return ques

def get_cagtegories(thing):
    categs = []
    if thing['FirstBless']:
        categs.append('FirstBless')
    if thing['LastBless']:
        categs.append('LastBless')
    if thing['Special']:
        categs.append('Special')
    return categs


if __name__ == '__main__':
    print(generate_question())


