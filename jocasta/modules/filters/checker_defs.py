import os
import re

from numpy import void



class Helper(object):
    
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def lista(dets):
        return re.findall(r'[0-9]+', dets)


def save_live(text: str):
    with open('text_files/live.txt', 'a',encoding = 'utf-8') as ap:
        ap.write(text)


def gate_error(text: str, gate_name: str):
    with open(f'text_files/{gate_name}.txt', 'w',encoding = 'utf-8') as ap:
        ap.write(text)


def find_between( data, first, last ):
    try:
        start = data.index( first ) + len( first )
        end = data.index( last, start )
        return data[start:end]
    except ValueError:
        return None

def remove_html_tags(xx):
    tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
    return tag_re.sub('', xx)