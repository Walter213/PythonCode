import os
import io
import pygame
import textwrap
import threading
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from gtts import gTTS
from googletrans import Translator
from PyDictionary import PyDictionary

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
        self.languages = googletrans.LANGUAGES
        self.translate_page()