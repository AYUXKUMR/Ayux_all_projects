# This Project of dice simulation is made on kivy on a very basic level
# import required libraries
import kivy
from kivy.app import App
from kivy.uix.button import Button
import random


# making a class to store all the work
class roll_the_dice(App):
    def build(self):
        # setting a button in the kivy window
        btn = Button(text="roll the dice",
               size = (.32, .32),
               pos = (0,0))
        btn.bind(on_press = self.callback)
        return btn
    # making a callback syestem which returns the value for dice
    def callback(self, event):
        rolled = random.randrange(1, 7)
        print(f"the answer is : {rolled}")
        


roll = roll_the_dice() 

roll.run()
# thanks for reading the code

# Licensed By AYUXKUMR