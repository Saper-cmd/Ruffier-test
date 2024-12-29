
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LandingPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        layout.add_widget(Label(text="Welcome to the Ruffier Test", font_size=20))
        layout.add_widget(Label(text="Enter your name and age to begin."))
        
        self.name_input = TextInput(hint_text="Enter your name", multiline=False)
        self.age_input = TextInput(hint_text="Enter your age", multiline=False)
        layout.add_widget(self.name_input)
        layout.add_widget(self.age_input)
        
        next_button = Button(text="Next", size_hint=(0.5, 0.2), pos_hint={"center_x": 0.5})
        next_button.bind(on_press=self.go_to_next)
        layout.add_widget(next_button)
        
        self.add_widget(layout)
    
    def go_to_next(self, instance):
        self.manager.current = "pulse_measurement"


class PulseMeasurementPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        layout.add_widget(Label(text="Measure your pulse for 15 seconds", font_size=20))
        self.pulse_input = TextInput(hint_text="Enter your pulse here", multiline=False)
        layout.add_widget(self.pulse_input)
        
        next_button = Button(text="Next", size_hint=(0.5, 0.2), pos_hint={"center_x": 0.5})
        next_button.bind(on_press=self.go_to_next)
        layout.add_widget(next_button)
        
        self.add_widget(layout)
    
    def go_to_next(self, instance):
        self.manager.current = "squats_instruction"


class SquatsInstructionPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        layout.add_widget(Label(text="Do 30 squats in 45 seconds", font_size=20))
        
        next_button = Button(text="Next", size_hint=(0.5, 0.2), pos_hint={"center_x": 0.5})
        next_button.bind(on_press=self.go_to_next)
        layout.add_widget(next_button)
        
        self.add_widget(layout)
    
    def go_to_next(self, instance):
        self.manager.current = "post_squat_measurement"


class PostSquatMeasurementPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        layout.add_widget(Label(text="Measure your pulse twice within the next minute:", font_size=16))
        layout.add_widget(Label(text="First 15 seconds and then the last 15 seconds.", font_size=16))
        layout.add_widget(Label(text="Write your results below.", font_size=16))
        
        self.pulse1_input = TextInput(hint_text="Result", multiline=False)
        self.pulse2_input = TextInput(hint_text="Result after rest", multiline=False)
        layout.add_widget(self.pulse1_input)
        layout.add_widget(self.pulse2_input)
        
        finalize_button = Button(text="Finalize", size_hint=(0.5, 0.2), pos_hint={"center_x": 0.5})
        finalize_button.bind(on_press=self.go_to_next)
        layout.add_widget(finalize_button)
        
        self.add_widget(layout)
    
    def go_to_next(self, instance):
        self.manager.current = "results"


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LandingPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text="Welcome to the Ruffier Test", font_size=20))
        layout.add_widget(Label(text="Enter your name and age to begin."))

        self.name_input = TextInput(hint_text="Enter your name", multiline=False)
        self.age_input = TextInput(hint_text="Enter your age", multiline=False)
        layout.add_widget(self.name_input)
        layout.add_widget(self.age_input)

        next_button = Button(text="Next", size_hint=(0.5, 0.2), pos_hint={"center_x": 0.5})
        next_button.bind(on_press=self.go_to_next)
        layout.add_widget(next_button)

        self.add_widget(layout)

    def go_to_next(self, instance):
        self.manager.current = "pulse_measurement"


class PulseMeasurementPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text="Measure your pulse for 15 seconds", font_size=20))
        self.pulse_input = TextInput(hint_text="Enter your pulse here", multiline=False)
        layout.add_widget(self.pulse_input)

        next_button = Button(text="Next", size_hint=(0.5, 0.2), pos_hint={"center_x": 0.5})
        next_button.bind(on_press=self.go_to_next)
        layout.add_widget(next_button)
+

    def go_to_next(self, instance):
        self.manager.current = "squats_instruction"


class SquatsInstructionPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text="Do 30 squats in 45 seconds", font_size=20))

        next_button = Button(text="Next", size_hint=(0.5, 0.2), pos_hint={"center_x": 0.5})
        next_button.bind(on_press=self.go_to_next)
        layout.add_widget(next_button)

        self.add_widget(layout)

    def go_to_next(self, instance):
        self.manager.current = "post_squat_measurement"


class PostSquatMeasurementPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text="Measure your pulse twice within the next minute:", font_size=16))
        layout.add_widget(Label(text="First 15 seconds and then the last 15 seconds.", font_size=16))
        layout.add_widget(Label(text="Write your results below.", font_size=16))

        self.pulse1_input = TextInput(hint_text="Result", multiline=False)
        self.pulse2_input = TextInput(hint_text="Result after rest", multiline=False)
        layout.add_widget(self.pulse1_input)
        layout.add_widget(self.pulse2_input)

        finalize_button = Button(text="Finalize", size_hint=(0.5, 0.2), pos_hint={"center_x": 0.5})
        finalize_button.bind(on_press=self.go_to_next)
        layout.add_widget(finalize_button)

        self.add_widget(layout)

    def go_to_next(self, instance):
        name = self.manager.get_screen("landing").name_input.text
        P1 = int(self.manager.get_screen("pulse_measurement").pulse_input.text)
        P2 = int(self.pulse1_input.text)
        P3 = int(self.pulse2_input.text)

        ruffier_index = 12 #X(P1, P2, P3)  # Placeholder function
        heart_efficiency = "low" #test(ruffier_index, level="normal")  # Placeholder function

        results_page = self.manager.get_screen("results")
        results_page.display_result(name, ruffier_index, heart_efficiency)

        self.manager.current = "results"


class ResultsPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.result_label = Label(text="", font_size=20)
        layout.add_widget(self.result_label)

        self.add_widget(layout)

    def display_result(self, name, ruffier_index, heart_efficiency):
        self.result_label.text = (
            f"{name}\n\n"
            f"Your Ruffier index: {ruffier_index}\n\n"
            f"Heart efficiency: {heart_efficiency}"
        )


class HeartCheckApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LandingPage(name="landing"))
        sm.add_widget(PulseMeasurementPage(name="pulse_measurement"))
        sm.add_widget(SquatsInstructionPage(name="squats_instruction"))
        sm.add_widget(PostSquatMeasurementPage(name="post_squat_measurement"))
        sm.add_widget(ResultsPage(name="results"))
        return sm


if __name__ == "__main__":
    HeartCheckApp().run()



class HeartCheckApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LandingPage(name="landing"))
        sm.add_widget(PulseMeasurementPage(name="pulse_measurement"))
        sm.add_widget(SquatsInstructionPage(name="squats_instruction"))
        sm.add_widget(PostSquatMeasurementPage(name="post_squat_measurement"))
        sm.add_widget(ResultsPage(name="results"))
        return sm


if __name__ == "__main__":
    HeartCheckApp().run()