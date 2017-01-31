#!/usr/bin/env python
# coding: utf-8

import re

hexcol = re.compile("#[0-9A-z]{6}")


from bs4 import BeautifulSoup

filename = r'./table.html'
soup = BeautifulSoup(open(filename, 'r'))

def texify(el):
    if el.name == 'sup':
        return "^{"+el.text+"}"
    if el.name == 'sub':
        return "_{"+el.text+"}"
    if el.name == 'b':
        return "\\mathbb{"+el.text+"}"
    if el.name == 'i':
        return "\\mathbb{"+el.text+"}"
    if el == u'×':
        return "\\times"
    if el == u'π':
        return "\\pi"
    return el # stringa ascii, in teoria

def makecol(attr):
    safe = "" if attr == None else attr;
    match = re.search('#([0-9A-z]{6})', safe)
    return "FFFFFF" if match == None else match.group(1)

colnum = 0

rows = []
for row in soup.findAll('tr'):
    cells = []
    for cell in row.findAll(['th','td']): # OR th
        col = makecol(cell.get('style'))
        tex_cell = "{\\cellcolor[HTML]{" + col +"}"+ "".join(["$"]+map(texify, cell.contents)+["$"]) + "}"
        cells.append(tex_cell)
    rows.append(cells)
    colnum = len(cells)

f_rows = map(lambda row: "&".join(row)+"\\\\", rows)

f_rows.insert(0, "\\begin{tabular}{"+"c"*colnum+"}")
f_rows.append("\\end{tabular}")

print "".join(f_rows)
