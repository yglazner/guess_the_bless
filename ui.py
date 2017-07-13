#encoding=utf8
data = """
#:set default_font_size "30sp"
#:set default_font_name "fonts/VarelaRoundRegular.ttf"
#:import reverse_text utils.reverse_text


<LevelBlock>:
    level_no: 0
    current_level: 2
    text: "%s" % self.level_no
    
    canvas.before:
        Color:
            rgb: (0.,0,0) if self.current_level< self.level_no else (0, 0, 0.8)
        Rectangle:
            pos: self.pos
            size: self.size

<BetterButton@Button>:
    rtext: "some_default"
    text: reverse_text(self.rtext)
    font_name: default_font_name
    font_size:  default_font_size
    
<BetterLabel@Label>:    
    rtext: "some_default"
    text: reverse_text(self.rtext)
    font_name: default_font_name
    font_size:  default_font_size
    
<BetterImage@Image>:
    size: (0,0) if not self.source else self.size
        

<MainScreen>:
    BoxLayout:
        orientation: "vertical"
        BetterButton:
            rtext: "התחל" 
            on_press: root.start()
        
        BetterButton:
            rtext: "צא בחוץ" 
            on_press: root.exit()
            
            
<GameScreen>:
    level: 1
    question: {'question': '', 'answers': ['','','',''], }
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation:  'horizontal'
           
            BoxLayout:
                orientation:  'vertical'
                BetterLabel:
                    
                    rtext: root.question['question']
                Image:
                    id: q_img
                    source: root.question.get('image', '') and "Img/%s" % root.question['image']
                    size_hint: (0,0) if not self.source else (1, 0.8)
                
            GridLayout:
                size_hint: 0.1, 1.0
                id: levels
                cols: 1
        GridLayout:
            cols: 2
            BetterButton:
                rtext: root.question['answers'][0]
                on_press: root.answer(0)
            BetterButton:
                rtext: root.question['answers'][1]
                on_press: root.answer(1)
            BetterButton:
                rtext: root.question['answers'][2]
                on_press: root.answer(2)
            BetterButton:
                rtext: root.question['answers'][3]
                on_press: root.answer(3)
        


"""