#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 9, 2014

@author: anroco

How to know if a python str starts with a specific string?

¿Como saber si un str python comienza con un string especifico?
'''

#create a str
s = 'Strings are immutable sequences of unicode code points'
print(s)

#the startswith() method verify if string starts with the defined value,
#can also be a tuple of prefixes to look for. Return True or False.
print(s.startswith('Strings'))

#define the search starting from a specified index
print(s.startswith('are', 8))

#search on a substring
print(s.startswith('sequences', 22, -6))
