# src/converter.py
from html_to_markdown import convert_to_markdown

def html_to_markdown(html_content: str) -> str:
   return convert_to_markdown(html_content)