import random
import PySimpleGUI as sg
import os


class PassGen:
    def __init__(self):
        # layout
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text('Email/User', size=(10, 1)), 
             sg.Input(key='user', size=(20, 1))],
            [sg.Text('Number of characters'), sg.Combo(values=list(
                range(30)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Generate Password')]
        ]
        # window
        self.my_window = sg.Window('Password Generator', layout)
        
    def start(self):
        while True:
            event, values = self.my_window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Generate Password':
                new_password = self.generate_password(values)
                print(new_password)
                self.save_password(new_password, values)
                
    def generate_password(self, values):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*'
        chars = random.choices(char_list, k=int(values['total_chars']))
        new_pass = ''.join(chars)
        return new_pass
        
    def save_password(self, new_password, values):
        with open('password.txt', 'a') as file:
            file.write(f"{values['site']},{values['user']}{os.linesep}")
            
        print('saved file')
    
gen = PassGen()
gen.start()
