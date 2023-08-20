# -*- coding: cp1251 -*-
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class CounterApp(App):
    def build(self):
        self.count = 0

        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='0', font_size=72)
        button = Button(text='Увеличить', font_size=24)
        button.bind(on_press=self.increment_count)

        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def increment_count(self, instance):
        self.count += 1
        self.label.text = str(self.count)


if __name__ == '__main__':
    CounterApp().run()