#!/usr/bin/env python
# -*- coding: utf-8 -*-
import kivy, time, webbrowser, json
from kivy.app import App
from kivy.app import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.core.window import Window;
#pegar o maximo de informaçoes deste link: http://stackoverflow.com/questions/36729140/how-to-automatically-load-data-from-json-file-on-startup-with-kivy
#neste aplicativo, necessito aprender como carregar o json e exibi-lo em uma label
class PrimeiroScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'um'
		super(Screen,self).__init__(**kwargs)
		nome = {u'nome': ''}
		
	def fc(self):
		escreva = self.ids.texto1.text
		nome1 = json.dumps(escreva)
		with open('nome1.json', 'w') as f:
			json.dump(nome1, f)
		#print(escreva)
class SegundoScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'dois'
		super(Screen,self).__init__(**kwargs)
		
	
class RootScreen(ScreenManager):
    pass
    
class gravaApp(App):
	title = 'Teste Json!'
	def on_pause(self):
		return True
		
	def on_resume(self):
	   
	   pass
      
	def build(self):
		return RootScreen()
if __name__ == '__main__':
    appVar = gravaApp()
    gravaApp().run()
