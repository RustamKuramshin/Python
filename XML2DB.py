# Сильно незавершенный скрипт
import os
from xml.etree import ElementTree as ET
import pymssql
import csv

s = 'black'

file_name = 'sample.xml'
file_path = os.path.abspath(os.path.join('data', file_name))

tree = ET.parse(file_path)
root = tree.getroot()

# print(root.tag, root.attrib, root.text)

# for child in root:
#     print(child.tag, child.attrib, child.text)

# for child in root:
#     for i in range(2):
#         print(child[i-1][i].tag, child[i-1][i].attrib, child[i-1][i].text)

# for child in root:
#     print(child[0][1].tag, child[0][1].text)

for neighbor in root.iter():
    if neighbor.tag == 'Location':
        print(neighbor.tag, neighbor.attrib)
    # print(neighbor.tag, neighbor.attrib, neighbor.text)

###########################################################	
import pymssql

conn = pymssql.connect(host='CAT\SQLEXPRESS', user='sa', password='15112016', database='pydb')
cursor = conn.cursor()


cursor.execute('SELECT * FROM dbo.persons')
row = cursor.fetchone()

print(row[0], row[1])
###########################################################
import xml.etree.ElementTree as ET

tree = ET.parse('PlaceList.xml')


def find(element_name):
    root = tree.getroot()
    for item in root.iter(element_name):
        element_property = [item.attrib, item.text]
        print(element_property[1])

element = input('Enter the name of the desired element: ')
find(element)
###########################################################
import unittest
import ExampleXML as ex

class TestFind(unittest.TestCase):
    def test_find(self):
        self.assertEqual(ex.find('StreetType'), 'Avenida\n Steet')


if __name__ == '__main__':
    unittest.main()
	
###########################################################	
