#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 00:17:43 2020

@author: gianlucapagliaro
"""

print('Trying to save a trial file')

with open('textfile.txt', 'w') as filehandle:  
    filehandle.write('that is the output')