import os
import requests
import json

try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup

from .paths import pages_folder, current_page_path

def handle_uploaded_file(f):
    name = f.name
    if name.endswith('.html'):
        try:
            with open(pages_folder + 'input.html', 'wb+') as destination:
                for chunk in f.chunks():  
                    destination.write(chunk)
            
            with open(pages_folder + 'output.html', 'wb+') as destination:
                for chunk in f.chunks():  
                    destination.write(chunk)
            return True
        except Exception as e:
            print('Upload Ex : ',e)
            return False
    else:
        return 'TYPE'
    
def get_linked_sheets():
    soup = BeautifulSoup(current_page_path, 'html.parser')

    css_tags = soup.findAll('link', rel=True, href=True)
    list_of_css = []

    for tag in css_tags:
        if tag['rel'] == 'stylesheet':
            list_of_css.append(tag['href'])

def clone_project(path):
    print('clone_project',path)
    return True
        

    
        



