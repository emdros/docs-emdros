import sys
import re


def read_doc(infilename):
    doc = b"".join(open(infilename, "rb")).decode('utf-8')
    return doc

def write_doc(outfilename, doc):
    fout = open(outfilename, "wb")
    fout.write(doc.encode('utf-8'))
    fout.close()

def process_doc(doc):
    doc = re.sub(r'\$\\rightarrow\$', r'->', doc)
    doc = re.sub(r'\$_\{([^\$\}]+)\}\$', r'<sub>\1</sub>', doc)

    #doc = re.sub(r'~', r'', doc)
    doc = re.sub(r'\\{', r'<lcurlybrace/>', doc)
    doc = re.sub(r'\\}', r'<rcurlybrace/>', doc)

    doc = re.sub(r'/\{\*\}', r'/*', doc)
    doc = re.sub(r'\{\*\}/', r'*/', doc)
    
    return doc

def doIt(infilename, outfilename):
    doc = read_doc(infilename)

    doc = process_doc(doc)

    write_doc(outfilename, doc)


if __name__ == '__main__':
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    doIt(infilename, outfilename)
    
