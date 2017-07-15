#encoding=utf8
from __future__ import unicode_literals
from ds import DS
import random

for obj in DS:
    for k in obj:
        obj[k] = obj[k].strip()    
# f = set()
# l = set()
# s = set()
#     
# for obj in DS:
#     for n, k in zip([f,l,s], ['FirstBless', 'LastBless', 'Special']):
#         n.add(obj[k])
# 
# print(f)
# print(l)
# print(s)

quesTypeText = {
    'FirstBless' : 'מהי הברכה הראשונה על %s?',
    'LastBless' : 'מהי הברכה האחרונה על %s?',
    'Special' : 'מה מברכים על %s?',
    'Name' : 'עבור מי מהבאים תברך %s?',
    #'Unusual' : 'מי מהבאים יוצא דופן?'
}

#the thing of the question about↓
TheThing = None


class QGen:

    quesHistory = []

    def __init__(self):
        quesHistory = []

    def generate_question(self):
        ques = {}
        the_thing = self.get_the_thing()
        quesStyle = random.random()
        if quesStyle < 0.17:
            ques = self.ask_what_the_bless(the_thing)
        #elif (0.17<= quesStyle< 0.33) & (not the_thing['Special']):
        #    ques = self.ask_unusual(the_thing)
        else:
            ques = self.ask_what_to_bless(the_thing)
        return ques

    def ask_what_the_bless(self, the_thing):
        ques = {}
        categs = self.get_cagtegories(the_thing)
        ques_type = random.choice(categs)
        ques['question'] = quesTypeText['Name'] % the_thing[ques_type]

        options = [the_thing['Name']]
        while len(options) < 4:
            curo = random.choice(DS)
            if (curo[ques_type] == the_thing[ques_type]):
                continue
            if curo['Name'] in options:
                continue
            options.append(curo['Name'])
        options.remove(the_thing['Name'])
        correct = random.randint(0, len(options))
        options.insert(correct, the_thing['Name'])
        ques['answers'] = options
        ques['correct'] = correct
        self.quesHistory.append(the_thing)

        return ques

    def ask_unusual(self, the_thing):
        ques = {}
        categs = self.get_cagtegories(the_thing)
        border = random.random()

        ques['question'] = quesTypeText['Unusual']

        options = [the_thing['Name']]
        the_diferent = None
        while True:
            curo = random.choice(DS)
            to_append = curo['Name']
            if(not to_append):
                continue;
            elif (to_append in options):
                continue;
            else:
                dif = 0
                for c in categs:
                    if the_thing[c] != curo[c]:
                        dif += 1
                if dif * random.random() > border:
                    options.append(curo['Name'])
                    the_diferent = curo
                    break
        while len(options) < 4:
            curo = random.choice(DS)
            to_append = curo['Name']
            if to_append in options:
                continue
            elif (curo['FirstBless'] == the_diferent['FirstBless']) & (curo['LastBless'] == the_diferent['LastBless']):
                options.append(curo['Name'])

        options.remove(the_thing['Name'])
        correct = random.randint(0, len(options))
        options.insert(correct, the_thing['Name'])
        ques['answers'] = options
        ques['correct'] = correct

        self.quesHistory.append(the_thing)

        return  ques

    def ask_what_to_bless(self, the_thing):
        ques = {}
        categs = self.get_cagtegories(the_thing)
        ques_type = random.choice(categs)
        ques['question'] = quesTypeText[ques_type] % the_thing['Name']
        #ques['name'] = the_thing['Name']
        ques['image'] = the_thing['Picture']
        options = [the_thing[ques_type]]
        while len(options) < 4:
            curo = random.choice(DS)
            to_append = curo[ques_type]
            if (not to_append):
                if ( 0.5 < random.random() < 0.55):
                    to_append = random.choice(self.get_cagtegories(curo))
                continue;
            if to_append in options:
                continue;
            if to_append == None :
                to_append = curo[ques_type]
            options.append(to_append)

        options.remove(the_thing[ques_type])
        correct = random.randint(0, len(options))
        options.insert(correct, the_thing[ques_type])
        ques['answers'] = options
        ques['correct'] = correct

        self.quesHistory.append(the_thing)

        return ques

    def get_the_thing(self):
        the_thing = None
        while True:
            the_thing = random.choice(DS)
            if(the_thing not in self.quesHistory):
                break
        return the_thing


    def get_cagtegories(self, thing):
        categs = []
        if thing['FirstBless']:
            categs.append('FirstBless')
        if thing['LastBless']:
            categs.append('LastBless')
        if thing['Special']:
            categs.append('Special')
        return categs


if __name__ == '__main__':
    g = QGen()
    q = g.generate_question()
    print(q)
    print(q['question'])
    print(q['answers'][q['correct']])


