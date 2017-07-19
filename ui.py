#encoding=utf8
data = """
#:set default_font_size "30sp"
#:set ui_color [0.7, 0.4, 0.62]
#:set btn_color [0.5, 0.6, 0.8, 1]
#:set block_color [1.0, 0.75, 0.0]
#:set default_font_name "fonts/VarelaRoundRegular.ttf"
#:import reverse_text utils.reverse_text


<LevelBlock>:
    level_no: 0
    current_level: 2
    text: "%s" % self.level_no
    font_size: "20sp"
    canvas.before:
        Color:
            rgb: ui_color if self.current_level< self.level_no else block_color
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
    background_color: btn_color
    color: 0.0, .1, .1, 1
    BetterLabel:
        rtext: self.parent.rtext


<BetterImage@Image>:
    size: (0,0) if not self.source else self.size
        

<MainScreen>:

    BoxLayout:
        orientation: "vertical"
        Image:
            canvas.before:
                Color:
                    rgb: 1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            
            allow_stretch: True
            keep_ratio: True
            source: "Img/logo_credits.png"
            
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
    
    canvas.before:
        Color:
            rgb: ui_color
        Rectangle:
            pos: self.pos
            size: self.size
            
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation:  'horizontal'
           
            BoxLayout:
                orientation:  'vertical'
                BetterLabel:
                    size_hint: 1.0, 0.25
                    ratio:0.95
                    rtext: root.question['question']
                Image:    
                    id: q_img
                    source: "Img/%s" % (root.question['image'] if root.question.get('image') else 'question_mark.png')
                    size_hint: 1.0, 0.75
                    allow_stretch: True
                    keep_ratio: True
                
            GridLayout:
                size_hint: 0.1, 1.0
                id: levels
                cols: 1
                spacing: [10, 0]
        GridLayout:
            cols: 2
            padding: [10, 10, 10, 10]
            spacing: [10, 10]
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
        id: b
        size_hint: 1.0, 1.0
        on_press: pop.dismiss()
        background_color: btn_color
        BoxLayout:
            size_hint: 1.0, 1.0
            pos: b.pos
            size: b.size
            Image:
                id: img
                allow_stretch: True
                size_hint: 1.0, 1.0
                
                source: "%s" % pop.source
                
                keep_ratio: True
                #center: b.center

"""