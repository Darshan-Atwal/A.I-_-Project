from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationDrawer
try:
    import pywhatkit as pwt
except Exception:
    pass
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivymd.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.core import window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.toolbar import MDTopAppBar
import webbrowser as wb
window.android

screen_helper='''
ScreenManager:
    Client_Info:
    Client_Service:
    hint:

    

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
        id: location
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
        on_press:  root.manager.current = 'Client_Service'
         
        
<hint>:
    name: 'hint'
    
    MDRectangleFlatButton:
        text: 'Back'
        on_press: root.manager.current = 'Client_Service'
        pos_hint: {'center_y':0.19, 'center_x':0.9} 
    MDTopAppBar:
        title: "Helper Text"
    Widget:

    MDLabel:
        text: ":- Type 'Search' to search on Google"
        pos_hint: {'center_y':0.7}  
    MDLabel:
        text: ':- Type "cure a disease" to find an cure'
        pos_hint: {'center_y':0.6}    
    MDLabel:
        text: ':- Type "Indian healthcare website" for accessing the indian healthcare website'
        pos_hint: {'center_y':0.5}      
    MDLabel:
        text: ':- Type "Hospitals near me" to see the nearest hospitals'
        pos_hint: {'center_y':0.4} 
    MDLabel:
        text: ':- Type "Diagonse a disease" to Diagnose a disease'
        pos_hint: {'center_y':0.3} 
        
            
<Client_Service>:
    name: "Client_Service"
    ScreenManager:
        Screen:    
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
        
                    elevation: 5
                    title: 'HealthyLiving'
                    
                Widget:

            MDRectangleFlatButton:
                text: 'Back'
                on_press: root.manager.current = 'Client_Info' 
            
            MDRectangleFlatButton:
                text: 'Hint'
                on_press: root.manager.current = 'hint'
                pos_hint: {'center_x': 0.9}
            MDTextField:
                id: inp
                pos_hint: {'center_y':0.5, 'center_x': 0.5} 
                size_hint: (0.5,0.1)
                hint_text: 'User Input'
           
                

            MDRectangleFlatButton:
                text: 'Submit'
                pos_hint: {'center_y':0.4, 'center_x': 0.5}
                on_press: root.onclck() 
                

    MDNavigationDrawer:
        id: nav_drawer
              


'''

class Client_Info(Screen):
    pass


class Client_Service(Screen):
    
    def onclck(self):
        
        inp = self.ids.inp.text
        if inp=='search' or inp=='Search':
            self.ids.inpu.text=""
            wb.open_new_tab("www.google.com")
          
        elif inp=="Indian healthcare website":
            wb.open_new_tab('https://www.mohfw.gov.in/')
            
        
        elif inp=='cure a disease' or inp=='Cure A disease' or inp=='Cure a Disease' or inp=='Cure A Disease':
            wb.open_new_tab('https://medlineplus.gov')
            
        elif inp=='Diagnose a disease' or inp=='diagnose a disease' or inp=='Diagnose A Disease' or inp=="Diagnose a Disease":
            wb.open_new_tab('https://symptomate.com/diagnosis/0')
            
        elif inp=="Hospitals near me" or inp=="hospitals near me" or inp=="Hospitals Near Me" or inp=='Hospitals Near me':
            pwt.search("Hospitals near me")
            
        
class hint(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Client_Info(name="Client_Info"))
sm.add_widget(Client_Service(name='Client_Service'))



class HealthyLiving(MDApp):
    def build(self):

        self.screen=Builder.load_string(screen_helper)
        
        return self.screen
    

 
    def onclick(self, obj):
        location = self.ids.city.text        
        name = self.ids.Name.text
        gender = self.ids.gender.text

HealthyLiving().run()
