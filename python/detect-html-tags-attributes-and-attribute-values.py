from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print(tag)
        for ele in attrs:
            print('->',ele[0],'>',ele[1])
            
    def handle_endtag(self,tag):
        pass
    
    def handle_startendtag(self,tag,attrs):
        print(tag)
        for ele in attrs:
            print('->',ele[0],'>',ele[1])
            

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()        