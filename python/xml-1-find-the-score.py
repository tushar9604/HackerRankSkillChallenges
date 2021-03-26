import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    return len(node.attrib) + sum((get_attr_number(child) for child in node))        
            
def get_attr_number2(node):
    return sum(len(child.attrib) for child in node.iter())
    
if __name__ == '__main__':
 #   sys.stdin.readline()
 #   xml = sys.stdin.read()
    xml = '\n'.join([input() for _ in range(int(input()))])
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
    print(get_attr_number2(root))