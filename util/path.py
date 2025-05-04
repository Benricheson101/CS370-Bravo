from os import path
import os
import sys


def is_bundle():
    """Returns True if the application is running in a PyInstaller bundle"""
    return getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS")

def to_path(*file):
    """Returns the path to the data file inside the built PyInstaller executable"""
    if is_bundle():
        return path.join(sys._MEIPASS, *file)
    return path.join(*file)

def exe_rel(*file):
    p = os.path.dirname(sys.executable) if is_bundle() else os.getcwd()
    return os.path.join(p, *file)
