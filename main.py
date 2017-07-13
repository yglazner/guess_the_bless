#encoding=utf8
from __future__ import unicode_literals
'''
Created on Jul 13, 2017

@author: yglazner
'''
from kivyoav.autosized_label import AutoSizedLabel
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import *
import sys
from kivy.uix.label import Label
from kivy.lang import Builder
#from kivy.core.audio import SoundLoader

import sys
import ui
import random
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader

py3 = sys.version[0] == '3'
print (py3, sys.version)
__version__ = '1.0.0'

image_folder = 'Img'

sm = None

TOTAL_LEVELS = 15

# if py3:
#     with open('ui.kv', encoding='utf8') as f:
#         s = f.read()
# else:
#     with open('ui.kv') as f:
#         s = f.read()



class LevelBlock(AutoSizedLabel):
    level_no = NumericProperty(0)
    current_level = NumericProperty(2)
    def __init__(self, level_no, current_level, **kw):
        super(LevelBlock, self).__init__(**kw)
        self.ratio = 0.99
        self.text = "%s" % level_no
        self.level_no = level_no
        self.current_level = current_level
    

class FakeGen(object):
    
    def generate_question(self):
        
        return {
                'image': u"egg.png",
                
                "question": u"מה מברכים לפני שמתים?",
                "answers": [u'ברכה אחרונה'
                            , u'שהכל'
                            , u'מחיה המתים'
                            , u'ברוך דיין האמת'],
                "answers_images": ['pop.png', ],
                "correct_answer": 0,  
               }
try:
    from question_generator import QGen
except ImportError:
    QGen = FakeGen
    

class ImagePop(Popup):
    source = StringProperty('')
    def __init__(self, choice, **kw):
        
        super(ImagePop, self).__init__( **kw)
        self.source = choice
        self.content.bind(on_press=self.dismiss)

success_snd = SoundLoader.load('Sounds/success.wav')
fail_snd = SoundLoader.load('Sounds/fail.wav')

class GameScreen(Screen):
    
    level = NumericProperty(1)
    #applause_sound = SoundLoader.load('Sounds/applause.mp3')
    #question = ObjectProperty({})
    
    def __init__(self, **kw):
        super(GameScreen, self).__init__(name='game', **kw)
        self.level = -1
        for i in range(TOTAL_LEVELS, 0, -1):
            self.ids.levels.add_widget(LevelBlock(i, self.level))
        self.g = QGen()
        self.next_question()
     
    def set_level(self, level):
        self.level = level
        for w in self.ids.levels.children:
            w.current_level = self.level
            
            
    def next_question(self):
        if self.level >= TOTAL_LEVELS:
            #win, make noise and animation
            sm.current = 'menu'
            
        self.question = self.g.generate_question()
        self.set_level(self.level + 1)
        #self.applause_sound.play()
        
        
    def on_pre_enter(self, *args):
        
        self.level = 0
        self.g = QGen()
        self.next_question()
    

    def show_success(self):
        success_imgs = ['Img/memes/success%s.jpg' % i for i in '123']
        pop = ImagePop(random.choice(success_imgs))
        success_snd.play()
        pop.open()
    
    
    def show_fail(self):
        fail_imgs = ['Img/memes/fail%s.jpg' % i for i in '123']
        pop = ImagePop(random.choice(fail_imgs))
        fail_snd.play()
        pop.open()
    
    def answer(self, num):
        if num == self.question['correct']:
            self.show_success()
            self.next_question()
        else:
            self.show_fail()
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
        Builder.load_string(ui.data)
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