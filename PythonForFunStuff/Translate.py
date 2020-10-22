import os
import io
import textwrap
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from googletrans import Translator

class Translate(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()
        tabControl = ttk.Notebook(root)
        tabControl.configure(width=350, height=400)

        self.translate_tab = ttk.Frame(tabControl)
        tabControl.add(self.translate_tab, text="Translator")
        tabControl.grid()
        self.translate_tab.grid_propagate(0)

        self.speak_it = BooleanVar()
        self.languages = { 'Arabic': 'ar', 'Belarusian': 'be',
            'Bulgarian': 'bg', 'Bosnian': 'bs',
            'Czech': 'cs', 'Danish': 'da',
            'German': 'de', 'Greek': 'el',
            'English': 'en', 'Spanish': 'es',
            'Persian': 'fa', 'Finnish': 'fi',
            'French': 'fr', 'Irish': 'ga',
            'Hebrew': 'he', 'Hindew': 'hi',
            'Croatian': 'hr', 'Haitian': 'ht',
            'Hungarian': 'hu', 'Armanian': 'hy',
            'Indonisian': 'id', 'Italian': 'it',
            'Japanese': 'ja', 'Korean': 'ko',
            'Kurdish': 'ku', 'Latin': 'li',
            'Lithuanian': 'lt', 'Latvian': 'lv',
            'Dutch': 'nl', 'Norwegian': 'no',
            'Polish': 'pl', 'Portuguese': 'pt',
            'Romanian': 'ro', 'Russian': 'ru',
            'Somalia': 'so', 'Albanian': 'sq',
            'Serbian': 'sr', 'Swedish': 'sv',
            'Swahili': 'sw', 'Turkish': 'tr',
            'Vietnamese': 'vi'}
        self.translate_page()

    def translate_page(self):
        self.top_label = Label(self.translate_tab, text="Enter Word(s): ")
        self.top_label.grid(column=0, row=0)

        self.entry = Entry(self.translate_tab, width=48)
        self.entry.grid(column=0, row=2, columnspan=3, padx=4, pady=4)

        self.language_label = Label(self.translate_tab, text="Language :")
        self.language_label.grid(column=0, row =2, pady=4)

        self.language_DDL = ttk.Combobox(self.translate_tab, values=[*self.languages.keys()])
        self.language_DDL.grid(column=1, row=2)
        self.language_DDL.current(0)

        self.translate_button = Button(self.translate_tab, text="Translate", command=self.translate_fuction)
        self.translate_button.grid(column=0, row=3, pady= 14)

        self.translated_frame = LabelFrame(self.translate_tab, text="Word:", width=300, height=50)
        self.translated_frame.grid(column=0, row=4, columnspan=3)
        self.translated_frame.grid_propagate(0)
        self.translated_result = Label(self.translated_frame, text="")
        self.translated_result.grid()

    def translate_fuction(self):
        translate = self.entry.get()
        language = self.languages.get(self.language_DDL.get())

        translated_word = self.translate_func(translate, language)

        self.translated_result.configure(text=translated_word)

    def translate_func(self, words, language):
        translator = Translator(service_urls=["translate.google.com"])
        translation = translator.translate(words, dest=language)
        return translation

if __name__ == '__main__':
    root = Tk()
    root.title("Translator")
    root.geometry("350x430")
    Translate(root)
    root.mainloop()