from ds import DS
import random

quesTypeText = {
    'FirstBless' : 'מהי הברכה הראשונה על %s?',
    'LastBless' : 'מהי הברכה האחרונה על %s?',
    'Special' : 'מה מברכים על %s?'
}

#the thing of the question about↓
TheThing = None


class Game:

    quesHistory = []

    def __init__(self):
        quesHistory = []

    def generate_question(self):
        ques = {}
        the_thing = self.get_the_thing()
        categs = self.get_cagtegories(the_thing)
        ques_type = random.choice(categs)
        ques['question'] = quesTypeText[ques_type] % the_thing['Name']
        ques['name'] = the_thing['Name']
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
    g = Game()
    print(g.generate_question())


