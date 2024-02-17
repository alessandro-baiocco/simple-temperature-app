from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.network.urlrequest import UrlRequest
import os
from dotenv import load_dotenv


load_dotenv()
class MyFirstApp(App):
    def build(self):
        authToken = os.environ.get('SECRET_KEY')
        print(authToken , "qui")
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.8 , 0.9)
        self.window.pos_hint = {"center_x" : 0.5 , "center_y" : 0.5}
        Window.size = (360,640)
        
        self.window.add_widget(Image(source="thermometer.png"))
        
        
        
        self.input_testo = TextInput(
            size_hint=(1 , 0.2),
            font_size="20sp",
            padding_y="12sp",
            halign="center"
            )
        
        
        self.bottone = Button(
            text="CERCA!", 
            size_hint=(1 , 0.2),
            bold="true",
            background_color="#0099ff"
            )
        
        self.scritta = Label(
            text="Cerca una città ...", 
            size_hint=(1 , 0.2),
            font_size="20sp",
            color="#007dd1"
            )
        
        
        self.window.add_widget(self.input_testo)
        
        self.window.add_widget(self.bottone)
        self.bottone.bind(on_press=self.trova_temp)
        
        self.window.add_widget(self.scritta)
        
        return self.window
    
    
    
    def trova_temp(self, instance):
        def edit_label(request, result):
            temp = result['main']['temp']
            self.scritta.text = f"oggi a {self.input_testo.text} ci sono {temp}°C"
        link = f"https://api.openweathermap.org/data/2.5/weather?q={self.input_testo.text}&appid=81ba62b31c758d02755836a11d185a38&units=metric"
        UrlRequest(link, edit_label)
        
        
MyFirstApp().run()