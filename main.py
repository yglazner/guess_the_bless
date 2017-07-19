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


import ui
import random
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import os
from glob import glob

py3 = sys.version[0] == '3'
print (py3, sys.version)
__version__ = '1.0.2'

image_folder = 'Img'

sm = None

TOTAL_LEVELS = 15

# if py3:
#     with open('ui.kv', encoding='utf8') as f:
#         s = f.read()
# else:
#     with open('ui.kv') as f:
#         s = f.read()



class LevelBlock(Label):
    level_no = NumericProperty(0)
    current_level = NumericProperty(2)
    def __init__(self, level_no, current_level, **kw):
        super(LevelBlock, self).__init__(**kw)
        
        self.ratio = 0.99
        self.text = "%s" % level_no
        self.level_no = level_no
        self.current_level = current_level
    
SAMPLE_QUESTION = {
                'image': u"egg.png",
                
                "question": u"מה מברכים לפני שמתים?",
                "answers": [u'ברכה אחרונה'
                            , u'שהכל'
                            , u'מחיה המתים'
                            , u'ברוך דיין האמת'],
                "answers_images": ['pop.png', ],
                "correct_answer": 0,  
               }

class FakeGen(object):
    
    def generate_question(self):
        
        return SAMPLE_QUESTION
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
        Clock.schedule_once(self._fix_center)
        
    def _fix_center(self, dt=None):
        self.ids.img.center = self.ids.b.center

success_snds = [SoundLoader.load('Sounds/success%d.wav' % i)
                for i in range(1, 3)]
fail_snd = SoundLoader.load('Sounds/fail.wav')

win_snd = SoundLoader.load('Sounds/claps.wav')

def play_success():
    random.choice(success_snds).play()


def play_win():
    win_snd.play()

success_imgs = glob('Img/memes/success*.jpg')

fail_imgs = glob('Img/memes/fail*.jpg')

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
        self.question = SAMPLE_QUESTION    
        self.question = self.g.generate_question()
        self.set_level(self.level + 1)
        Clock.schedule_once(self.do_layout)
        #self.applause_sound.play()
        
        
    def on_pre_enter(self, *args):
        
        self.level = 0
        self.g = QGen()
        self.next_question()
    
    def show_win(self):
        win_pic = 'Img/memes/winner.jpg'
        pop = ImagePop(win_pic)
        play_win()
        pop.open()

    def show_success(self):
        
        pop = ImagePop(random.choice(success_imgs))
        play_success()
        pop.open()
    
    
    def show_fail(self):
        
        pop = ImagePop(random.choice(fail_imgs))
        fail_snd.play()
        pop.open()
    
    def answer(self, num):
        if num == self.question['correct']:
            if self.level >= TOTAL_LEVELS:
                #win, make noise and animation
                self.show_win()
                sm.current = 'menu'
                return
            self.next_question()
            self.show_success()
            
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