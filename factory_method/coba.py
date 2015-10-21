#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cobaFactoryMethod.py
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

class Jajal(object):
    def dapat(self, msk):
        return None
    def act(self):
        return None

class coba(Jajal):
    def dapat(self, msk):
        return msk == "coba"
    def act(self):
        print "ini adalah coba pertama"

class coba2(Jajal):
    def dapat(self, msk):
        return msk == "cb"
    def act(self):
        print "ini adalah coba kedua"

class coba3(Jajal):
    def dapat(self, msk):
        return msk == "gajah"
    def act(self):
        print "gajah gajah gajah"
        
def factory(msk):
    jajalClasses = [x() for x in Jajal.__subclasses__()]
    for jajal in jajalClasses:
        if jajal.dapat(msk):
            return jajal.act()
    assert 0, "pilihan jelek " + msk

def cari(msk):
    fact = None
    try:
        fact = factory(msk)
    except AssertionError as err:
        print  err
    return fact


        
def main():
    query = ["facebook", "cb", "coba"]
    for x in query:
         cari(x)

	

cari("coba")
cari("cb")
cari("gajah")
main()

"""
Hasil
==============
ini adalah coba pertama
ini adalah coba kedua
gajah gajah gajah
pilihan jelek facebook
ini adalah coba kedua
ini adalah coba pertama
"""
