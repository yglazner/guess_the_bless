import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

def reverse_text(text):
    if (type(text)==bytes):
        text = text.decode('utf8')
    return text[::-1]


#def reverse_text(text):
#    return text[::-1]