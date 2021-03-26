from html.parser import HTMLParser

# create a subclass and override the handler methods
"""
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Found a start tag  :", tag)
    def handle_endtag(self, tag):
        print ("Found an end tag   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Found an empty tag :", tag)
"""
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for ele in attrs:
            print('->',ele[0],'>',ele[1])
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for ele in attrs:
            print('->',ele[0],'>',ele[1])
# instantiate the parser and fed it some HTML
#parser = MyHTMLParser()
#parser.feed("<html><head><title>HTML Parser - I</title></head>"
 #           +"<body><h1>HackerRank</h1><br /></body></html>")
            
#inputfeed = ''.join([input() for _ in range(int(input()))])
#parser.feed(inputfeed)

parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())