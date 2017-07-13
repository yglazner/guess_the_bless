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

    
<BetterLabel@AutoSizedLabel>:    
    rtext: "some_default"
    text: reverse_text(self.rtext)
    font_name: default_font_name
    #font_size:  default_font_size
    ratio: 0.6

<BetterButton@BoxLayout+Button>:
    rtext: "some_default"
    background_normal: ""
    background_color: [0.0, 0.2, 0.8, 1]
    color: 0.0, .1, .1, 1
    BetterLabel:
        rtext: self.parent.rtext
        

    
<BetterImage@Image>:
    size: (0,0) if not self.source else self.size
        

<MainScreen>:
    BoxLayout:
        orientation: "vertical"
        Image:
            allow_stretch: True
            keep_ratio: False
            source: "Img/logo.png"
            
        BetterButton:
            rtext: "התחל" 
            on_press: root.start()
            background_color: [0.0, 0.8, 0.1, 1]
        
        BetterButton:
            rtext: "צא בחוץ" 
            on_press: root.exit()
            background_color: [0.8, 0.2, 0.2, 1]
            
            
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
                    size_hint: 1.0, 0.2
                    rtext: root.question['question']
                Image:
                    id: q_img
                    source: "Img/%s" % (root.question['image'] if root.question.get('image') else 'question_mark.png')
                    size_hint: 1.0, 0.8
                    allow_strech: True
                    keep_ratio: True
                
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
        
<ImagePop>:
    id: pop
    source: ""
    title: ""
    separator_height: 0.0
    
    Button:
        on_press: pop.dismiss()
        size_hint: 1.0, 1.0
        Image:
            size: self.parent.size
            pos: self.parent.pos
            source: "%s" % pop.source
            allow_stretch: True
            keep_ratio: False

"""