"""
Hangman implemented in kivy (https://kivy.org/)

    Hangman is a word-game where the aim is to reveal
    a hidden word.

    The player enters one character at a time. If the
    character is correct it is revealed, otherwise
    the incorrect guess is added to the list of incorrect
    characters and one piece is added to the gallows. 

    After ten (this number is configurable) incorrect
    attempts, the game is lost. 

Technical stuff:
    * Use pydoc <module> for command-line access to 
      module documentation, .e.g. pydoc kivy.graphics


"""

# Read local kivy config
import os
import kivy.config
kivy.config.Config.read(f"{os.environ['PWD']}/.kivy/config.ini")

from kivy.app import App
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

NO_GUESSES = 10

Window.set_title("Hangman")
# Window.size = (500, 500)

class HangmanGame(Widget):
# class HangmanGame(BoxLayout):
    """Hangman game root widget"""
    number_guesses = NumericProperty(10)
    guesses = StringProperty("abc")

    def __init__(self, *args, **kwargs):
        """Constructor. Calls __init__() of Widget."""
        super().__init__()

    def update_gallows(self):
        """Update the gallows graphics"""
        pass

    def update_status_line(self):
        """Update the status line:
        - previously guessed characters (all incorrect)
        - number of guesses left
        - the (partially) revealed secret word
        """
        self.number_guesses -= 1
        self.guesses += "x"


class HangmanApp(App):
    """The Hangman app"""

    def __init__(self, *args, **kwargs):
        """For now, just calls __init__() of the App classs"""
        super().__init__()

    def build(self):
        """Build the widget tree"""
        self.root = HangmanGame()
        return self.root


if __name__ == "__main__":
    """Run this code if we're run rather than imported"""
    HangmanApp().run()
