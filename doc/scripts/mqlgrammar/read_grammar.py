from __future__ import unicode_literals, print_function
import sys
import re
import pprint
import copy

def read_file(infilename):
    udoc = (b"".join(open(infilename, "rb"))).decode('utf-8')
    return udoc

comment_re = re.compile(r'/\*(?:.|\n)*?\*/')
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

    #print("LHS: %s => %s" % (lhs, repr(mylist)))
    return mylist

def process_grammar(udoc):
    grammar = {} # non-terminal -> (block, non_terminal_list)

    block_re = re.compile(r'[A-Za-z_][A-Za-z0-9_]+\s*=(?:.|\s)+?;[ \t]*\n')
    for block in block_re.findall(udoc):
        arr = block.split("=")
        lhs = arr[0].strip()
        rhs = "=".join(arr[1:])
        non_terminal_list = get_nonterminals_in_rhs(lhs, rhs)
        grammar[lhs] = (block, non_terminal_list)

    return grammar


def get_outfilename_from_non_terminal(non_terminal):
    return "%s.md" % non_terminal

def emit_non_terminal_recursively(grammar, non_terminal, non_terminal_set, fout):
    block, non_terminal_list  = grammar[non_terminal]

    fout.write(block.encode('utf-8'))
    fout.write(b'\n')
    
    non_terminal_set.add(non_terminal)
    
    for block_non_terminal in non_terminal_list:
        if block_non_terminal not in non_terminal_set:
            non_terminal_set.add(block_non_terminal)
            emit_non_terminal_recursively(grammar, block_non_terminal, non_terminal_set, fout)

def emit_preamble(non_terminal, fout):
    statement_name = " ".join([s.upper() for s in non_terminal.replace("_statement", "").split("_")])
    fout.write(("=%s=\n\n" % statement_name).encode('utf-8'))
    fout.write(b'==Grammar==\n\n')
    fout.write(b'```\n')

    
def emit_postamble(non_terminal, fout):
    fout.write(b'```\n\n')

    fout.write(b'==Examples==\n\n')
    fout.write(b'```\n')
    fout.write(b'```\n\n')

    fout.write(b'==Explanation==\n\n')
    fout.write(b'\n\n')

    fout.write(b'==Return type==\n\n')
    fout.write(b'\n')
    fout.write(b'\n')
    

def doIt(grammar_infilename, non_terminal_list):
    udoc = read_file(grammar_infilename)

    grammar = process_grammar(udoc)

    for non_terminal in non_terminal_list:
        outfilename = get_outfilename_from_non_terminal(non_terminal)
        fout = open(outfilename, "wb")
        emit_preamble(non_terminal, fout)
        emit_non_terminal_recursively(grammar, non_terminal, set(), fout)
        emit_postamble(non_terminal, fout)
        fout.close()
        sys.stderr.write(("Now look in: %s ...\n" % outfilename).encode('utf-8'))

if __name__ == '__main__':
    if sys.argv[1] == '--auto':
        doIt("mql_grammar.txt",
             [
                 "create_database_statement",
                 "initialize_database_statement",
                 "use_statement",
                 "drop_database_statement",
                 "vacuum_database_statement",
                 "create_object_type_statement",
                 "update_object_type_statement",
                 "drop_object_type_statement",
                 "insert_monads_statement",
                 "delete_monads_statement",
                 "get_monads_statement",
                 "monad_set_calculation_statement",
                 "create_enumeration_statement",
                 "update_enumeration_statement",
                 "drop_enumeration_statement",
                 "create_segment_statement",
                 "select_statement",
                 "select_objects_at_statement",
                 "select_objects_having_monads_in_statement",
                 "get_aggregate_features_statement",
                 "get_objects_having_monads_in_statement",
                 "get_set_from_feature_statement",
                 "select_object_types_statement",
                 "select_features_statement",
                 "select_enumerations_statement",
                 "select_enumeration_constants_statement",
                 "select_object_types_which_use_enum_statement",
                 "select_min_m_statement",
                 "select_max_m_statement",
                 "create_object_from_monads_statement",
                 "create_object_from_id_ds_statement",
                 "update_objects_by_monads_statement",
                 "update_objects_by_id_ds_statement",
                 "delete_objects_by_monads_statement",
                 "delete_objects_by_id_ds_statement",
                 "get_features_statement",
                 "quit_statement",
                 "create_indexes_statement",
                 "drop_indexes_statement",
                 "begin_transaction_statement",
                 "commit_transaction_statement",
                 "abort_transaction_statement",
                 "select_monad_sets_statement",
                 "get_monad_sets_statement",
                 "create_monad_set_statement",
                 "update_monad_set_statement",
                 "drop_monad_set_statement",
                 "create_objects_statement",
             ])
    else:
        grammar_infilename = sys.argv[1]
        non_terminal_list = sys.argv[2:]
        doIt(grammar_infilename, non_terminal_list)

    
