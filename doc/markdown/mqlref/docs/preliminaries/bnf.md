# Introduction to Backus-Naur Form

If you already know what Backus-Naur form is, feel free to skip this
section.

## Context-Free Grammars in general

BNF is a way of specifying the “syntactic rules” of a
language. English also has “syntactic rules,” and some of them can be
specified using a “Context-Free Grammar.” BNF is precisely a way of
specifying a context-free grammar for a formal language. Thus it is
beneficial first to see what a context-free grammar is, before looking
at the details of BNF.

In English, the basic clause-pattern is “Subject - Verb - Object”. For
example, in the clause “I eat vegetables,” the word “I” is the
subject, the word “eat” is the verb, and the word “vegetables” is the
object.  A clause which exhibits exactly the same “Subject - Verb -
Object” structure is “You drink coke.” Here, “You” is the subject,
“drink” is the verb, and “coke” is the object.

Consider the following context-free grammar:

```
Sentence --> NPsubj VP
NPsubj --> “I” | “You”
VP --> V NPobj
V --> “eat” | “drink”
NPobj --> “vegetables” | “coke”
```

This little context-free grammar is a toy example of a context-free
grammar. However, despite its simplicity, it exemplifies all of the
concepts involved in context-free grammars:

- Rule
- Non-terminal
- Terminal
- Choice
- Concatenation
- Start-symbol.

These will be described in turn below

### Rule

A “Rule” consists of three parts:

1. The left-hand side
2. The “production arrow” (“`-->`”).
3. The right-hand side

An example of a rule in the above context-free grammar is:

``Sentence --> NPsubj VP``

It specifies that the left-hand side (“Sentence”) can be replaced with
the right-hand side, which in this case is two symbols, “NPsubj”
followed by “VP”. Sometimes, we also say that a left-hand side is
expanded to the right-hand side.

### Non-terminal

There are only two kinds of symbols in a context-free grammar:
Non-terminals and Terminals. They are a contrasting pair. In this
section, we describe what a non-terminal is, and in the next section,
what a terminal is.

A “Non-terminal” is a symbol in a rule which can be expanded to other
symbols. Thus the symbols “Sentence”, “NPsubj”, “VP”, “V”, and
“NPobj” constitute all of the non-terminals of the above context-free
grammar.

Only non-terminals can stand on the left-hand side of a rule. A
non-terminal is defined as a symbol which can be expanded to or
replaced with other symbols, and hence they can stand on the left-hand
side of a rule. But as you will notice in the above context-free
grammar, a non-terminal can also stand on the right-hand-side of a
rule.

For example, the non-terminal “V” is present both in the rule for how
to expand the non-terminal “VP”, and in the rule for how to expand
itself. Thus, in order to expand “VP” fully, you must first expand to
the right-hand-side “V NPobj”, and then expand both “V” and “NPobj”,
using the rules for these two.

### Terminal

A “Terminal” is a symbol in a rule which cannot be expanded to other
symbols. Hence, it is “terminal” in the sense that the expansion
cannot proceed further from this symbol. In the above context-free
grammar, the terminals are: “I”, “You”, “eat”, “drink”, “vegetables”,
and “coke”.  These are symbols which cannot be expanded further.

Terminals can only stand on the right-hand side of a rule. If they
were to stand on the left-hand-side of the rule, that would mean that
they could be expanded to or replaced with other symbols. But that
would make them non-terminals.

### Choice

In the rule for “V” in the above grammar, we see an example of
choice. The choice is indicated by the “|” symbol, which is read as
“or”. Thus, this example:

`V --> “eat” | “drink”`

is read as ‘V expands to “eat” *or* “drink”’.


### Concatenation

We have already seen an example of concatenation, namely in the rule
for “Sentence”:

`Sentence --> NPsubj VP`

Here, the symbols “NPsubj” and “VP” are *concatenated*, i.e., placed
in sequence. Thus “VP” comes immediately after “NPsubj”.

“Concatenated” is simply a fanciful name for “being in sequence”.

### Start-symbol

The start-symbol is merely the left-hand side non-terminal of the rule
in the grammar from which parsing must start.  It is the "top level"
symbol, from which the entire grammar generates its strings. Thus, in
the above grammar, “Sentence” is the start-symbol.

## Context-free grammars: Putting it all together

It is time to see how all of this theory works in practice. The above
grammar can produce 8 sentences, some of which do not make sense:

1. I eat vegetables
2. I eat coke
3. I drink vegetables
4. I drink coke
5. You eat vegetables
6. You eat coke
7. You drink vegetables
8. You drink coke

Let us pick one of these sentences and see how it was produced from the above grammar. We will pick number 8, “You drink coke”, and trace all the steps. We start with the start-symbol, “Sentence”:

1. `Sentence`
   This is expanded using the rule for “Sentence”:
   
2. `NP subj VP`
   The “NPsubj” non-terminal is then expanded to “You” using one of the
   choices in the rule for NPsubj:
   
3. `“You” VP`
   The “VP” is then expanded using the rule for “VP”:
   
4. `“You” V NPobj`
   The “V” non-terminal is then expanded to the terminal “drink”:
   
5. `“You” “drink” NPobj`
   The “NPobj” non-terminal is then expanded to the terminal “coke”:
   
6. `“You” “drink” “coke”`
   Which yields the final sentence, “You drink
   coke”. This sentence has no non-terminals, only terminals, and
   therefore it cannot be expanded further. We are finished.


If you would like to, try to trace the production of one of the other
sentences using pencil and paper, tracing each step as in the above
example. When you have done so once or twice, you should understand
all there is to understand about context-free grammars.

And BNF is simply a way of specifying a context-free grammar. So let
us start looking at the details of BNF.

## BNF

### Introduction

BNF comes in various variants, and almost everyone defines their usage
of BNF a little differently from everyone else. In this document, we
shall also deviate slightly from “standard BNF”, but these deviations
will only be very slight.

This treatment of BNF will be made from an example of a context-free
grammar in “MQL BNF.” This example covers every formalism used in “MQL
BNF,” and is a real-life example of the syntax of an actual MQL
statement:

```
create_enumeration_statement : “CREATE”
              (“ENUMERATION” | “ENUM”)
              enumeration_name “=”
              “{” ec_declaration_list “}”
;
enumeration_name : T_IDENTIFIER
              /* The T_IDENTIFIER is a terminal
              denoting an identifier. */
;
ec_declaration_list : ec_declaration { “,” ec_declaration }
;
ec_declaration : [ “DEFAULT” ]
              ec_name [ ec_initialization ]
;
ec_name : T_IDENTIFIER
;
ec_initialization : “=” T_INTEGER
;
```


#### Elements of “MQL BNF”

All of the elements of “MQL BNF” can be listed as follows:

1.  Rule
    
    This is just the same as in the context-free grammars above, except
    that the “-\>” production arrow is replaced by a “:“ colon. Also, a
    rule ends with a “;” semicolon.

2.  Non-terminal
    
    Non-terminals always start with a lower-case letter, e.g.,
    “ec\_declaration.”

3.  Terminal
    
    Terminals are either strings in “double quotes” or strings that
    start with “T\_”, e.g., “T\_IDENTIFIER”.

4.  Choice
    
    This is the same as in the context-free grammars. The symbol “|” is
    used.

5.  Concatenation
    
    This is the same as in the context-free grammars. A space between
    two symbols is used.

6.  Start-symbol
    
    This is the same as in the context-free grammars. The left-hand side
    non-terminal of the first rule is the start-symbol.

7.  Comment
    
    A comment is enclosed in /\* slashes and stars \*/. The comments are
    not part of the grammar, but serve to explain a part of the grammar
    to the human reader.

8.  Optional specification
    
    A symbol or sequence of symbols enclosed in <span>\[</span>square
    brackets<span>\]</span> is considered optional. For example, the
    `ec_initialization` non-terminal is optional in the `ec_declaration`
    rule. Both terminals and non-terminals can be optional. Here, the
    choice is between “ENUM” and “ENUMERATION”, rather than, say,
    “CREATE ENUMERATION” and the rest of the rule.

9.  Bracketing
    
    Sometimes, we do not go to the trouble of spelling out a choice with
    a rule by itself. Instead, (brackets) are used. For example, in the
    above grammar, there is a choice between “ENUMERATION” and “ENUM”.
    Only one must be chosen when writing the CREATE ENUMERATION
    statement. The brackets serve to let you know the scope of the
    choice, i.e., between exactly which elements the choice stands.

10. Bracing (repetition)
    
    The \<lcurlybrace/\> braces \<rcurlybrace/\> are used to indicate
    that the enclosed part can be repeated zero or more times. For
    example, in the rule for `ec_declaration_list`, the first
    `ec_declaration` can be followed by zero or more occurrences of
    first a “,” comma and then an `ec_declaration`. This effectively
    means that the `ec_declaration_list` is a comma-separated list of
    `ec_declaration`s, with one or more `ec_declaration`s.
    
    There is no comma after the last `ec_declaration`. To see why,
    notice that the part that is repeated starts with a comma and ends
    with an `ec_declaration`. Thus, no matter how many times you repeat
    this sequence, the `ec_declaration` will always be last, and the
    comma will never be last.
    
    That it can be repeated *zero* or more times simply means that it is
    optional. In the rule for `ec_declaration_list`, the first
    `ec_declaration` can stand alone.
    
    Notice also that, in the rule for `create_enumeration_statement`,
    there are braces as well. These braces, however, are enclosed in
    “double quotes” and are therefore terminals. Thus they do not have
    the meaning of repetition, but are to be written in the statement
    when writing a CREATE ENUMERATION statement. The braces without
    double quotes are repetition-braces and must not be written.

