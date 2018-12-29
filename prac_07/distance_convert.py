from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilestoKilometers(App):

    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('distance_convert.kv')
        return self.root

    def handle_increment(self, value):

        try:
            int(self.root.ids.input_miles.text)
        except ValueError:
            self.root.ids.input_miles.text = '0'

        result = int(self.root.ids.input_miles.text) + value
        self.root.ids.input_miles.text = str(result)

    def convert_distance(self, value):

        try:
            float(value)
        except ValueError:
            value = 0.0

        result = float(value) * 1.6
        self.root.ids.output_label.text = str(result)


MilestoKilometers().run()
