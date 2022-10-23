from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationDrawer

from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivymd.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.core import window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.toolbar import MDTopAppBar
window.android

screen_helper='''
ScreenManager:
    Client_Info:
    Client_Service:
    

<Client_Info>:
    name: 'Client_Info'

    MDTopAppBar:
        text: 'HealthyLiving'
    
    Widget:
    
    MDTextField:
        id: Name
        helper_text: "Your name"
        pos_hint: {'center_x':0.5, 'center_y':0.8}
        helper_text_mode: "on_focus"
        size_hint: (0.5, 0.1)
        icon_right: "android"
        hint_text: 'Enter Your Name'
        width: 200
    
    MDTextField:
        id: city
        helper_text: "Your City"
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        size_hint: (0.5, 0.1)
        helper_text_mode: "on_focus"
        hint_text: 'Enter Your Location'
        icon_right: "android"
        width: 200
    
    MDTextField:
        id: gender
        helper_text: "Your Gender"
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        size_hint: (0.5, 0.1)
        helper_text_mode: "on_focus"
        hint_text: 'Enter Your Gender'
        icon_right: "android"
        width: 200

    MDRectangleFlatButton:    
        text: 'Submit'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'Client_Service' 
        
         
        
            
<Client_Service>:
    name: "Client_Service"
    ScreenManager:
        Screen:    
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
        
                    elevation: 5
                    title: 'HealthyLiving'
                    left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                Widget:

            MDRectangleFlatButton:
                text: 'Back'
                on_press: root.manager.current = 'Client_Info' 
    MDNavigationDrawer:
        id: nav_drawer
              


'''

class Client_Info(Screen):
    pass

class Client_Service(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Client_Info(name="Client_Info"))
sm.add_widget(Client_Service(name='Client_Service'))

class HealthyLiving(MDApp):
    def build(self):
        
        self.screen=Builder.load_string(screen_helper)
        return self.screen
    def navigation_draw(self):
        print('lmao')


HealthyLiving().run()
