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


def get_outfilename_from_non_terminal(non_terminal, prefix):
    real_name = non_terminal.replace("statement", "").replace("_", "")
    return "%s%s.md" % (prefix, real_name)

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
    fout.write(("# %s\n\n" % statement_name).encode('utf-8'))
    fout.write(b'## Purpose\n\n')
    fout.write(b'## Grammar\n\n')
    fout.write(b'```\n')

    
def emit_postamble(non_terminal, fout):
    fout.write(b'```\n\n')

    fout.write(b'## Examples\n\n')
    fout.write(b'```\n')
    fout.write(b'```\n\n')

    fout.write(b'## Explanation\n\n')
    fout.write(b'\n\n')

    fout.write(b'## Return type\n\n')
    fout.write(b'\n')
    fout.write(b'\n')
    

def doIt(grammar_infilename, prefix, non_terminal_list):
    udoc = read_file(grammar_infilename)

    grammar = process_grammar(udoc)

    for non_terminal in non_terminal_list:
        outfilename = get_outfilename_from_non_terminal(non_terminal, prefix)
        fout = open(outfilename, "wb")
        emit_preamble(non_terminal, fout)
        emit_non_terminal_recursively(grammar, non_terminal, set(), fout)
        emit_postamble(non_terminal, fout)
        fout.close()
        sys.stderr.write("Now look in: %s ...\n" % outfilename)

if __name__ == '__main__':
    if sys.argv[1] == '--auto':
        grammar_infilename = "mql_grammar.txt"
        for (prefix, non_terminal_list) in [
                ("../../markdown/mqlref/docs/mql/schema/databases/", [
                 "create_database_statement",
                 "initialize_database_statement",
                    "use_database_statement",
                 "drop_database_statement",
                 "vacuum_database_statement",
                    ]),
                ("../../markdown/mqlref/docs/mql/schema/indexes/", [
                 "create_indexes_statement",
                 "drop_indexes_statement",
                    ]),
                ("../../markdown/mqlref/docs/mql/schema/enumerations/", [
                 "create_enumeration_statement",
                 "update_enumeration_statement",
                 "drop_enumeration_statement",
                ]),
                ("../../markdown/mqlref/docs/mql/schema/introspection/", [
                 "select_enumerations_statement",
                 "select_enumeration_constants_statement",
                 "select_object_types_using_enum_statement",
                ]), 
                ("../../markdown/mqlref/docs/mql/schema/objecttypes/", [
                 "create_object_type_statement",
                 "update_object_type_statement",
                 "drop_object_type_statement",
                ]),
                ("../../markdown/mqlref/docs/mql/schema/introspection/", [
                 "select_object_types_statement",
                 "select_features_statement",
                ]),
                ("../../markdown/mqlref/docs/mql/data/objects/", [
                 "create_objects_with_object_type_statement",
                 "create_object_from_monads_statement",
                 "create_object_from_id_ds_statement",
                 "update_objects_by_monads_statement",
                 "update_objects_by_id_ds_statement",
                 "delete_objects_by_monads_statement",
                 "delete_objects_by_id_ds_statement",
                 "select_all_objects_statement",
                 "get_objects_having_monads_in_statement",
                 "select_objects_at_statement",
                 "select_objects_having_monads_in_statement",
                 "get_aggregate_features_statement",
                 "get_monads_statement",
                 "get_features_statement",
                 "get_set_from_feature_statement",
                ]),
                ("../../markdown/mqlref/docs/mql/data/monadsets/", [
                 "create_monad_set_statement",
                 "update_monad_set_statement",
                 "drop_monad_set_statement",
                 "monad_set_calculation_statement",
                 "select_monad_sets_statement",
                 "get_monad_sets_statement",
                ]),
                ("../../markdown/mqlref/docs/mql/data/globaldata/", [
                 "select_min_m_statement",
                 "select_max_m_statement",
                ]),
                ("../../markdown/mqlref/docs/mql/meta/", [
                 "begin_transaction_statement",
                 "commit_transaction_statement",
                 "abort_transaction_statement",
                    ]),
                ("../../markdown/mqlref/docs/mql/meta/", [
                 "quit_statement",
                ]),
                ("../../markdown/mqlref/docs/mql/topographic/preliminaries/", [
                 "select_all_objects_statement",
                ]),
                ]:
            doIt(grammar_infilename, prefix, non_terminal_list)
    else:
        grammar_infilename = sys.argv[1]
        non_terminal_list = sys.argv[2:]
        doIt(grammar_infilename, "", non_terminal_list)

    
