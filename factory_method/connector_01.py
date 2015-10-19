#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  connector_01.py
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
"""Ini adalah contoh dari buku mastering python design pattern
dengan modifikasi untuk mensimpelkan saja, dan untuk memahami pattern ini
yaitu factory method"""


class Connector(object):
    @classmethod
    def name(self):
        raise NotImplementedError("Tidak bisa di inisiasi langsung")

class JsonConnector(Connector):
    @classmethod
    def name(self):
        return "Hay, saya json connector"

class XmlConnector(Connector):
    @classmethod
    def name(self):
        return "Hay, saya xml connector"

class SqlConnector(Connector):
    @classmethod
    def name(self):
        return "Hay, saya sql connector"

def connection_factory(filepath):
    if filepath.endswith("json"):
        connector = JsonConnector
    elif filepath.endswith("xml"):
        connector = XmlConnector
    elif filepath.endswith("sql"):
        connector = SqlConnector
    else:
        raise ValueError("gak bisa konek ke %s" %filepath)
    return connector.name()

def connect_to(filepath):
    factory = None
    
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print ve
    
    return factory

def main():
    sqlite = connect_to("ssss/sql.sql")
    print sqlite
    json = connect_to("apaja/json.json")
    print json
    xml = connect_to("apaaja/xml.xml")
    print xml
    html = connect_to("html/html.html")
    print html
        
if __name__ == '__main__':
	main()

