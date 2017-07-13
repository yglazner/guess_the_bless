'''
Created on Jul 13, 2017

@author: yglazner
'''
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import *
import sys
from kivy.uix.label import Label
from kivy.lang import Builder


sm = None

TOTAL_LEVELS = 15

with open('ui.kv', encoding='utf8') as f:
    s = f.read()

Builder.load_string(s)

class LevelBlock(Label):
    level_no = NumericProperty(0)
    current_level = NumericProperty(2)
    def __init__(self, level_no, current_level, **kw):
        super(LevelBlock, self).__init__(**kw)
        self.text = "%s" % level_no
        self.level_no = level_no
        self.current_level = current_level
    

class FakeGen(object):
    
    def next_question(self):
        
        return {
                'image': "pizza.png",
                "question": "מה מברכים לפני שמתים?",
                "answers": ['ברכה אחרונה', 'שהכל', 'מחיה המתים', 'ברוך דיין האמת'],
                "correct_answer": 0,  
               }
try:
    from question_gen import QG
except ImportError:
    QG = FakeGen
    
class GameScreen(Screen):
    
    level = NumericProperty(1)
    #question = ObjectProperty({})
    
    def __init__(self, **kw):
        super(GameScreen, self).__init__(name='game', **kw)
        self.level = -1
        for i in range(TOTAL_LEVELS, 0, -1):
            self.ids.levels.add_widget(LevelBlock(i, self.level))
            
        self.g = QG()
        self.next_question()
     
    def set_level(self, level):
        self.level = level
        for w in self.ids.levels.children:
            w.current_level = self.level
            
            
    def next_question(self):
        if self.level >= TOTAL_LEVELS:
            #win, make noise and animation
            sm.current = 'menu'
            
        self.question = self.g.next_question()
        self.set_level(self.level + 1)
    
    def on_enter(self, *args):
        self.level = 0
        
        self.next_question()
    
    def answer(self, num):
        if num == self.question['correct_answer']:
            self.next_question()
        else:
            sm.current = 'menu'

class MainScreen(Screen):
    
    def __init__(self, **kw):
        super(MainScreen, self).__init__(name='menu', **kw)

    def start(self):
        sm.current = 'game'

    def exit(self):
        sys.exit(0)

class GuessTheBless(App):
    '''
    classdocs
    '''


    def build(self):
        global sm
        
        sm = ScreenManager()
        
        sm.add_widget(MainScreen())
        sm.add_widget(GameScreen())
        sm.current = 'menu'
        return sm
    
    def on_pause(self):
        # Here you can save data if needed
        if sm.current not in ['menu']:
            return True
        else:
            return False
        
    def on_resume(self):
        pass
    
    def open_settings(self, *largs):
        pass

    
if __name__ == '__main__':
    GuessTheBless().run()