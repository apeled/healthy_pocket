from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import plotly.graph_objs as go


class BatteryUsage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Get the battery usage data
        self.battery_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

        # Create a plot
        self.plot = go.Scatter(
            x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], y=self.battery_data)

        # Add the plot to the layout
        self.add_widget(FloatLayout(size_hint=(1, 1), pos_hint={
                        'center_x': .5, 'center_y': .5}))

        # Add a button to update the plot
        self.update_button = Button(text="Update Plot")
        self.update_button.bind(on_press=self.update_plot)
        self.add_widget(self.update_button)

    def update_plot(self, instance):
        # Update the data
        self.battery_data = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

        # Update the plot
        self.plot.y = self.battery_data

    def on_kv_post(self, base_widget):
        # Show the plot
        go.FigureWidget(data=[self.plot]).show()


class BatteryUsageApp(App):
    def build(self):
        return BatteryUsage()


if __name__ == '__main__':
    BatteryUsageApp().run()
