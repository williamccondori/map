import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

CLASSES = ['ship']
INPUT_DIR = '/home/william/data/hrsc/voc/'
OUTPUT_DIR = '/home/william/data/hrsc/map/'

def convert_annotation(image_id):
    in_file = open(INPUT_DIR + '/%s.xml' % (image_id))
    out_file = open(OUTPUT_DIR + '/%s.txt' % (image_id), 'w')

    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        print obj.find('name').text
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in CLASSES or int(difficult) == 1:
            continue
        classe = 'ship'
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('xmax').text), int(
            xmlbox.find('ymin').text), int(xmlbox.find('ymax').text))
        
        out_file.write('{0} {1} {2} {3} {4}\n'.format(classe, b[0], b[1], b[2], b[3]))
    out_file.close()
	

def main():
    file = open('/home/william/data/hrsc/test.txt', 'r')
    for line in file:
        line = line.rstrip('.jpg\n')
        line = line.split('/')
        print(line[6])
        convert_annotation(line[6])

if __name__ == '__main__':
    main()
