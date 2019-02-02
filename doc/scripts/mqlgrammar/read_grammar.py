from __future__ import unicode_literals, print_function
import sys
import re
import pprint
import copy

def read_file(infilename):
    udoc = (b"".join(open(infilename, "rb"))).decode('utf-8')
    return udoc

comment_re = re.compile(r'/\*.*?\*/')
terminal_re = re.compile(r'"[^"]*"')
operator_re = re.compile(r'[\|()\[\]=\{\};]')

def get_nonterminals_in_rhs(lhs, rhs):
    rhs2 = copy.copy(rhs)

    rhs2 = comment_re.sub(r'', rhs2)
    rhs2 = terminal_re.sub(r'', rhs2)

    # The only undefined non-terminal is STRING
    rhs2 = rhs2.replace("STRING", "")

    rhs2 = operator_re.sub(r' ', rhs2)

    non_terminal_list = rhs2.split()
    myset = set()
    mylist = []
    for non_terminal in non_terminal_list:
        if non_terminal not in myset:
            myset.add(non_terminal)
            mylist.append(non_terminal)

    print("LHS: %s => %s" % (lhs, repr(mylist)))
    return mylist

def process_grammar(udoc):
    grammar = {} # non-terminal -> (block, non_terminal_list)

    block_re = re.compile(r'([A-Za-z_][A-Za-z0-9_]+)(\s*=[^;]+;[ \t]*\n)')
    for (lhs, rhs) in block_re.findall(udoc):
        block = "%s%s" % (lhs, rhs)
        non_terminal_list = get_nonterminals_in_rhs(lhs, rhs)
        grammar[lhs] = (block, non_terminal_list)

    pprint.pprint(grammar)
    return grammar


def get_outfilename_from_non_terminal(non_terminal):
    return "XXX_%s.md" % non_terminal

def emit_non_terminal_recursively(grammar, non_terminal, non_terminal_set, fout):
    block, non_terminal_list  = grammar[non_terminal]

    fout.write(block.encode('utf-8'))
    fout.write(b'\n')
    
    non_terminal_set.add(non_terminal)
    
    for block_non_terminal in non_terminal_list:
        print("RECURSIVE: %s -> %s" % (non_terminal, block_non_terminal)) 
        if block_non_terminal not in non_terminal_set:
            non_terminal_set.add(block_non_terminal)
            emit_non_terminal_recursively(grammar, block_non_terminal, non_terminal_set, fout)
    

def doIt(infilename, non_terminal_list):
    udoc = read_file(infilename)

    grammar = process_grammar(udoc)

    for non_terminal in non_terminal_list:
        outfilename = get_outfilename_from_non_terminal(non_terminal)
        fout = open(outfilename, "wb")
        emit_non_terminal_recursively(grammar, non_terminal, set(), fout)
        fout.close()

    pprint.pprint(grammar)
    


if __name__ == '__main__':
    infilename = sys.argv[1]
    non_terminal_list = sys.argv[2:]
    doIt(infilename, non_terminal_list)

    
