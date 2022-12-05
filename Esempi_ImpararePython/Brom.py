from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog

kv="""
Screen:
    GridLayout:
        rows: 4

        MDTextField:
            id: mdtext1
            hint_text: "Cosa vuoi"
            mode: "rectangle"

        MDTextField:
            id: mdtext2
            hint_text: "Cosa vuoi"
            mode: "rectangle"

        MDRaisedButton:
            text: "CONCATENA!"
            size_hint_x: 1
            size_hint_y: 0.1
            on_press: app.normal_search_button()

        ScrollView:
            MDLabel:
                id: mdlab
                text: ""
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None
"""

class WikiReaderApp(MDApp):

    def build(self):
        self.title = "Concatenatore"
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "400"
        return Builder.load_string(kv)

    def normal_search_button(self):
        self.root.ids["mdlab"].text = self.root.ids["mdtext1"].text+" "+self.root.ids["mdtext2"].text

WikiReaderApp().run()