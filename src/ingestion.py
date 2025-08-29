import fitz  # PyMuPDF
from bs4 import BeautifulSoup
import os

def load_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    return text

def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    return soup.get_text()

def load_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
