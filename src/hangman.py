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

    # Generate a secret word 
    secret_word_str = random.choice(WORDLIST)
    secret_word_len_int = len(secret_word_str)
    secret_word_len = NumericProperty(len(secret_word_str))
    secret_word = StringProperty(secret_word_str)
    
    # The partially hidden string is stored as a ListProperty
    # so that it can be accessed in the kv file
    partially_hidden_str = "_" * secret_word_len_int
    partially_hidden_list = ListProperty(list(partially_hidden_str))

    # The number of guesses made is stored as a NumericPropery,
    # also so that it can be used in the kv file
    number_guesses = NumericProperty(10)

    # Guessed characters are stored as a ListProperty
    guesses = ListProperty()

    def __init__(self, *args, **kwargs):
        """Constructor. Calls __init__() of Widget."""
        super().__init__()

        # NB: The Popup widget below was supposed to
        # be used to print a welcome screen containing
        # the rules of the game. Couldn't get it 
        # working, though, so for now it's commented out.
        #popup = Popup(title="Regler",
        #              content=Label(text="""Regler: 
        #                            Spelet går ut på att gissa ett ord.  
        #                            Man har tio (10) gissningar på sig.  """, 
        #              color=(1, 1, 1, 1)),
        #              size_hint=(None, None),
        #              size=(300, 300),
        #              background="0, 0, 0, 1",
        #              opacity=1)
        #popup.open()

        # Keep track of number of correctly guessed characters
        self.number_correct_guesses = 0

    def update_gallows(self):
        """Update the gallows graphics"""
        pass

    def update_status_lines(self, char):
        """Update the status lines:
        - previously guessed characters (all incorrect)
        - number of guesses left
        - the (partially) revealed secret word
        """
        def check_game_won():
            if self.number_correct_guesses == self.secret_word_len:
                print("Hurra!")
                self.ids.text_input.hint_text = "Hurra, du vann!"

        def check_game_over():
            if self.number_guesses == 0:
                self.ids.text_input.hint_text = "Game over!"

        def update_partially_hidden(char):
            """Iterate through the secret word and if the guessed 
            character matches, update the partially hidden string.
            Also update the number of correctly made guesses."""
            for k, c in enumerate(self.secret_word):
                if char == c:
                    self.partially_hidden_list[k] = char
                    self.number_correct_guesses += 1

        # If not already guessed, add to guesses, decrease number of
        # remaining guesses, and update the StatusLabels
        if not char in self.guesses:
            self.number_guesses -= 1
            self.guesses.append(char)
            update_partially_hidden(char)

        # Check if the game is won or lost.
        check_game_won()
        check_game_over()

        # Reset (clear) the TextInput widget
        self.ids.text_input.text = ""
        # Return focus to the TextInput widget
        self.ids.text_input.focus = True

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
