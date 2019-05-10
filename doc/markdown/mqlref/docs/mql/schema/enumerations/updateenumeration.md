# UPDATE ENUMERATION

## Purpose

To alter an enumeration by adding constants, removing constants, changing the value of a constant, and/or specifying a new DEFAULT constant.

## Grammar

```
update_enumeration_statement =
          "UPDATE" ("ENUM" | "ENUMERATION")
          enumeration_name "="  
          "{" ec_update_list "}" ;

enumeration_name = IDENTIFIER ; 

ec_update_list = ec_update { "," ec_update } ;

ec_update = ["ADD"] ["DEFAULT"] ec_name ec_initialization
          | "UPDATE" ["DEFAULT"] ec_name ec_initialization
          | "REMOVE" ec_name;

ec_name = IDENTIFIER ; 

ec_initialization = "=" signed_integer; 

signed_integer = unsigned_integer | "-" unsigned_integer | "NIL" ; 

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

```

## Examples

```
UPDATE ENUMERATION
phrase_type_t = {
    ADD DEFAULT Unknown = -99,
    REMOVE NotApplicable,
    UPDATE PP = 5,
    AdvP = 4
}
GO
```

This alters the table made in the example in section
[\[CREATE\_ENUMERATION\]](/mql/schema/enumerations/createenumeration/)
to be like this:

| Name    | Value | Default |
| :------ | :---: | :-----: |
| Unknown | \-99  |   Yes   |
| VP      |   1   |   No    |
| NP      |   2   |   No    |
| AP      |   3   |   No    |
| AdvP    |   4   |   No    |
| PP      |   5   |   No    |

## Explanation

This statement updates the enumeration constants of an already existing
enumeration. The user can specify whether to add, remove, or update an
enumeration constant.

It is an error (and none of the updates will be executed) if the user
REMOVEs the default enumeration constant without specifying a new
default.

Note that you are forced to specify values for all of the constants
updated or added.

It is an error (and none of the updates will be executed) if the
update would lave the enumeration in a state where two labels would
have the same value. This is because an enumeration is effectively a
one-to-one correspondence between a set of labels and a set of values.

It is the user’s responsibility that the update leaves the database in a
consistent state. For example, Emdros will not complain if you remove a
constant with a given value without specifying a different constant with
the same value, even if there are features that use this enumeration and
have this value. This would mean that those feature-values could not be
searched for, since there would be no label to look for. Neither would
it be possible to get the feature values with GET FEATURES, since there
would be no label to return.

## Return type

There is no return value.

