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

import random

# Set KIVY_HOME environment variable. This is where
# the kivy configuration is (supposed to be) read and 
# where log files are (supposed to be) stored.
import os
os.environ['KIVY_HOME'] = f"{os.environ['PWD']}/.kivy"
# Read local kivy config
import kivy.config
kivy.config.Config.read(f"{os.environ['PWD']}/.kivy/config.ini")
kivy.config.Config.set('kivy', 'exit_on_escape', 1)
kivy.config.Config.set('kivy', 'log_enable', 1)
kivy.config.Config.write()

from kivy.app import App
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from wordlists.wordlist_se import WORDLIST

NO_GUESSES = 10

Window.set_title("Hangman")
# Window.size = (500, 500)

class HangmanGame(Widget):
# class HangmanGame(BoxLayout):
    """Hangman game root widget"""
    secret_word_str = random.choice(WORDLIST)
    secret_word_len_int = len(secret_word_str)
    secret_word_len = NumericProperty(secret_word_len_int)
    secret_word = StringProperty(secret_word_str)
    
    partially_hidden_str = "_" * secret_word_len_int
    partially_hidden = StringProperty(partially_hidden_str)
    partially_hidden_list = ListProperty(list(partially_hidden_str))

    s = str(secret_word)
    print("len(secret_word) =", len(s))
    print(str(secret_word_str))
    print(secret_word_str)

    number_guesses = NumericProperty(10)
    guesses = StringProperty("")
    guesses_list = ListProperty()

    def __init__(self, *args, **kwargs):
        """Constructor. Calls __init__() of Widget."""
        super().__init__()
        #popup = Popup(title="Hej men nej",
        #              content=Label(text="Hej fubar"),
        #              size_hint=(None, None),
        #              size=(300, 300),
        #              background="0, 0, 0, 1")
        #popup.open()
        self.sword = random.choice(WORDLIST)

    def update_gallows(self):
        """Update the gallows graphics"""
        pass

    def update_status_line(self, text):
        """Update the status line:
        - previously guessed characters (all incorrect)
        - number of guesses left
        - the (partially) revealed secret word
        """
        def update_partially_hidden(text):
            for k, c in enumerate(self.secret_word):
                if text == c:
                    self.partially_hidden_list[k] = text
            s = " ".join(self.partially_hidden_list)
            print(s)
            l = [s[k] for k in range(len(s))]
            print(l)

        # Decrease number of remaining guesses 
        self.number_guesses -= 1
        # If not already guessed, add to guesses
        if not text in self.guesses:
            self.guesses += text[0]
            self.guesses_list.append(text[0])
            update_partially_hidden(text)
        self.ids.text_input.text = ""
        self.ids.text_input.focus = True

    #def on_enter(instance, value):
    #    print(instance)
    #    print(instance.ids.text_input.text)
    #    print(str(instance.number_guesses))
    #    print(value)
    #    instance.guesses += value

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
