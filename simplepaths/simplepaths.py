# -*- coding: utf-8 -*-
import os
import sys
import inspect

def fixpaths(par_dir_name):
    # get the path of the current file (or interpreter or terminal)
    file_path = os.path.abspath(inspect.getfile(inspect.currentframe()))
    # get the parent directory of that file (or interpreter or terminal)
    par_dir_path = os.path.dirname(file_path)
    # search up through the folder structure to try to find the specified parent directory
    while os.path.basename(par_dir_path) <> par_dir_name:
        par_dir_path = os.path.dirname(par_dir_path)
        if par_dir_path == '/':
            raise ValueError('{} parent directory not found'.format(par_dir_name))
    # if the parent directory path is not in sys.path, add it at the beginning
    if par_dir_path not in sys.path:
        sys.path.insert(0, par_dir_path)