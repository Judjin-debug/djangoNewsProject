from django import template
import re

register = template.Library()

curses_list = ['doomed']


@register.filter(name='censor')
def censor(text):
    if isinstance(text, str):
        for word in curses_list:
            word_len = len(word)
            text = re.sub(word, '*' * word_len, text)
        return text
    else:
        raise ValueError(f'Filter can\'t be applied to {type(text)}')
