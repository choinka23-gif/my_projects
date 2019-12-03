from __future__ import division
import tkinter as tk
from tkinter import filedialog
import pytesseract
from langdetect import detect
from googletrans import Translator
from pdf2image import convert_from_path


def translate_text(pdf_path):
    eng_text = "Text after translate"
    pages = convert_from_path(pdf_path, 500)
    number = 1
    for page in pages:
        eng_text = "\r\n" + eng_text + "STR" + str(number) + "\r\n"
        text = get_text_from_jpg(page)
        language = choose_language(text)
        eng_text = eng_text + translate_2(text, language)
    print(eng_text)
    return eng_text


def get_file_path():

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path


def get_text_from_jpg(file_name):
    pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract'
    config = ('-l deu --oem 1 --psm 3')
    im = file_name
    text = pytesseract.image_to_string(im, config=config)
    return text


def choose_language(text):
    lang = detect(text)
    return lang


def translate_2(text, language):
    translator = Translator()
    text_translate = str(translator.translate(text, src=language, dest='en').text)
    return text_translate