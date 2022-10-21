import xml.etree.ElementTree as ET
import glob
import os
def remove_seg(root):
    for box in root.iter('box'):
        for seg in box.findall('segs'):
            a = box.remove(seg)
            return a    

def remove_pts(root):
    for box in root.iter('box'):
        for pts in box.findall('pts'):
            a = box.remove(pts)
            return a
xml_path = 'ctw1500_train_labels/*.xml'

for xml in glob.glob(xml_path):
    name = os.path.basename(xml)
    tree = ET.parse(xml)
    root = tree.getroot()
    remove_seg(root)
    remove_pts(root)
    for box in root.iter('box'):
        for label in box.findall('label'):
            label.text = '1'
            print (ET.tostring(root))

            tree.write('out/' + name)
