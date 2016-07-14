import os.path

def red_text(txt):
    return '\033[31m' + txt + '\033[0m'


def green_text(txt):
    return '\033[32m' + txt + '\033[0m'

basedir = os.path.abspath(os.path.dirname(__file__))
