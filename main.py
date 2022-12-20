from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.effectwidget import EffectWidget, InvertEffect, HorizontalBlurEffect
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.properties import ObjectProperty
from kivy.core.window import Window


Window.size = (500, 900)
Window.top = 100

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        anim = Animation(x=100, y=500)  + Animation(x=300, y=0, duration=2.)
        anim &= Animation(font_size=50) + Animation(font_size=14, duration=2.)
        anim.start(self.ids.fly)  
        
        
class MenuGame(Screen):
    ...

class InfoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.box = BoxLayout(orientation='vertical')
        # self.grid = GridLayout(cols=3)
        
        for i in ANIMALS_01:
            image = Image(source=ANIMALS_01[i])
            self.ids.learn_grid.add_widget(image)

        # for child in self.children:
        #     anim = Animation(size=(50, 50), duration=5)
        #     anim.start(child)
        # image = Image(source='images/animals_01/rat.png')

        # w = EffectWidget()
        # w.add_widget(Button(text='Hello!'))
        # w.effects = [InvertEffect(), HorizontalBlurEffect(size=2.0)]
        # grid.add_widget(w)
        # w.add_widget(Image(source='images/animals_01/cat.png'))
        # w.effects = [InvertEffect(), HorizontalBlurEffect(size=2.0)]
        # grid.add_widget(w)
        # self.btnOk = Button(text='Got It!', size_hint_y=0.2)
        # self.btnOk.on_press = self.pressOk

        # self.box.add_widget(self.grid)
        # self.box.add_widget(self.btnOk)

        # self.add_widget(self.box)

    def on_enter(self, *args):
        # for child in self.ids.learn_grid.children:
        #     child.size_hint = (None, None)
        #     anim = Animation(size=(0, child.size[1]), duration=3) + Animation(size=(child.size[0], child.size[1]))
        #     anim.start(child)

        return super().on_enter(*args)

    def pressOk(self):
        self.manager.current = 'menu'
        self.manager.transition.direction = "right"

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(MenuGame(name='menu'))
        sm.add_widget(InfoScreen(name='info'))

        return sm

ANIMALS_01 = {
    'cat': 'images/animals_01/cat.png',
    'dog': 'images/animals_01/dog_01.png',
    'cow': 'images/animals_01/cow_01.png',
    'owl': 'images/animals_01/owl_01.png',
    'wolf': 'images/animals_01/wolf_01.png',
    'snake': 'images/animals_01/snake_01.png',
    'monkey': 'images/animals_01/monkey_01.png',
    'turtle': 'images/animals_01/turtle.png',
    'bear': 'images/animals_01/bear.png',
    'hedgehog': 'images/animals_01/hedgehog.png',
    'fox': 'images/animals_01/fox_01.png',
    'rat': 'images/animals_01/rat.png'
    }

RESULTS = {}
RESULTS['class1'] = False

if __name__=="__main__":
    app = MainApp()
    app.title = "Master of all!"

    app.run()