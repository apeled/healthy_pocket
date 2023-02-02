import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.icon = "HEALTHY POCKET.png"
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation = "vertical")
        self.solution = TextInput(background_color = "red", foreground_color = "white")
"""
        main_layout.add_widget(self.solution)
        buttons = [
            ["Take Measurment"]
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label, font_size = 30, background_color = "grey",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        
        take_measurement_button = Button(
            text="Take Measurment", font_size=30, background_color="grey",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        take_measurement_button.bind(on_press=self.on_solution)
        main_layout.add_widget(take_measurement_button)

        return main_layout

    def on_button_press(self, instance):
        current = 0
"""

if __name__ == "__main__":
    app = MainApp()
    app.run()

""" 
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from android.permissions import request_permissions, Permission

class CameraApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.cam_button = Button(text='Cam')
        self.cam_button.bind(on_press=self.open_camera)
        layout.add_widget(self.cam_button)
        return layout

    def open_camera(self, instance):
        request_permissions([Permission.CAMERA])
        self.camera = self.ids['camera']
        self.camera.play = True

if __name__ == '__main__':
    CameraApp().run()
 """