#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tjm.py
#  
#  Copyright 2015 IbnuAmin <mihfazhillah@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

class Targeem(object):
    
    
        
    def is_handle(self):
        pass
        
    def action(self):
        pass

class AboutTargeem(Targeem):
    
   
    
    def is_handle(self, choice):
        return choice.lower() == "about"
    
    def action(self,data):
        print "ini adalah menu about targeem"
        
class HelpTargeem(Targeem):
    
    
        
    def is_handle(self, choice):
        return choice.lower() == "help"
        
    def action(self, data):
        print "ini adalah menu bantuan targeem"

class ArIdTargeem(Targeem):
    """ Pilihan untuk melakukan terjemahan dari arab ke bahasa indonesia"""
    
    def is_handle(self, choice):
        return choice.lower() == "arid"
        
    def action(self, data):
        print 'melakukan terjemahan dari', data, 'ke indonesia'

def targeemFactory(choice, data=None):
    tgmClasses = [x() for x in Targeem.__subclasses__()]
    for tgm in tgmClasses:
        if tgm.is_handle(choice):
            return tgm.action(data)
    assert 0, choice + " perintah tidak dikenali"

def targeem(choice, data=None):
    factory = None
    try:
        factory = targeemFactory(choice, data)
    except AssertionError as err:
        print err
    return factory

def main():
    masukan = [
    ["about"],
    ["tentang"],
    ["help"],
    ['arid', 'كاتا'],
    ['irad', 'halo'],
    ]
    for x in masukan:
        targeem(*x)

if __name__ == '__main__':
	main()

"""
keluaran
================
ini adalah menu about targeem
tentang perintah tidak dikenali
ini adalah menu bantuan targeem
melakukan terjemahan dari كاتا ke indonesia
irad perintah tidak dikenali

==========
"""
