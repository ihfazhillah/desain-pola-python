#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tukang_01.py
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

class Tukang(object):
    @staticmethod
    def is_handle(bagian):
        return None
    
    def get_bayaran(self):
        return 0

class TukangUtama(Tukang):
    @staticmethod
    def is_handle(bagian):
        return bagian in ["utama"]
    
    def get_bayaran(self, bagian):
        return 70000

class TukangLaden(Tukang):
    @staticmethod
    def is_handle(bagian):
        return bagian in ['laden']
    
    def get_bayaran(self, bagian):
        return 65000

class Tukang_Factory(object):
    @staticmethod
    def tukang_baru(bagian):
        #ambil semua subclass dari class Tukang
        tukangClasses = [x() for x in Tukang.__subclasses__()]
        for tukang in tukangClasses:
            
            if tukang.is_handle(bagian):
                return tukang.get_bayaran(bagian)
        #kalau gak dapet
        raise ValueError("%s tidak ditemukan" %bagian)

def dapat_gaji_tukang(bagian):
    factory = None
    try:
        factory = Tukang_Factory().tukang_baru(bagian)
    except ValueError as ve:
        print ve
    
    return factory
    
        

def main():
    laden = dapat_gaji_tukang("laden")
    print "bayaran tukang laden adalah ", laden
    utama = dapat_gaji_tukang("utama")
    print "bayaran tukang utama adalah ", utama
    lain = dapat_gaji_tukang("lain")
    
   
    

if __name__ == '__main__':
	main()

