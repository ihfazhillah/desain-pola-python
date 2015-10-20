#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  shape.py
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
from abc import ABCMeta, abstractmethod

class Shape:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def draw():
        pass

class Lingkaran(Shape):
    
    def draw(self):
        print "lingkaran "

class Kotak(Shape):
    def draw(self):
        print "kotak "

class ShapeFactory:
    @classmethod
    def get_shape(self, name):
        if name.lower() == 'kotak':
            return Kotak()
        elif name.lower() == 'lingkaran':
            return Lingkaran()
        raise TypeError("Masukkan yang bener")


def main():
    try:
        get_shape = ShapeFactory.get_shape("lingkaran")
        get_shape.draw()
        get_shape = ShapeFactory.get_shape("bundar")
        get_shape.draw()
    except TypeError as err:
        print err
        
	
	

if __name__ == '__main__':
	main()

