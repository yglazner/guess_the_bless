'''
Created on Jun 29, 2017

@author: yglazner
'''
from kivy.uix.widget import Widget
from kivy.properties import *
from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp
from kivy.uix.slider import Slider
Slider
class EmotionFeedBack(Widget):
    '''
    EmotionFeedBack - a widget that lets the user express its emotion by swipping up or down
    '''
    level = NumericProperty(0.5)
    orientation = OptionProperty('horizontal', options=(
        'horizontal', 'vertical'))
    sources = ListProperty([])
    def __init__(self, sources=[], **kw):
        '''
        '''
        self.sources = sources
        super(EmotionFeedBack, self).__init__(**kw)
        
    @property
    def vertical(self):
        return self.orientation == 'vertical'
    
        
    
    def on_touch_down(self, touch):
        touch.ud['pos'] = touch.pos
        return super(EmotionFeedBack, self).on_touch_down(touch)
        
    def on_touch_move(self, touch):
        sx, sy = touch.ud['pos']
        touch.ud['pos'] = x, y = touch.pos
        
        ts, t = (sy, y) if self.vertical else (sx, x)
        size = self.height if self.vertical else self.width
        change = (t - ts)*20.0 / size
        self.level += change
        self.level = max(min(self.level, 1.0), 0)
        
        
        print (self.level)
        return super(EmotionFeedBack, self).on_touch_move(touch)
    
    
if __name__ == '__main__':
    runTouchApp(EmotionFeedBack())