# What is an enumeration?

Each feature, it will be remembered, is of a certain type. These can be
integers, strings, and id\_ds, but they can also be enumerations. An
enumeration is a set of pairs, where each pair consists of a
constant-identifier and an integer value.

# Example

For example, the enumeration “phrase\_type\_t” might have the pairs of
constants and values as in the following table:

| constant              | value |
| :-------------------- | :---: |
| phrase\_type\_unknown |  \-1  |
| VP                    |   1   |
| NP                    |   2   |
| AP                    |   3   |
| PP                    |   4   |
| AdvP                  |   5   |
| ParticleP             |   6   |

#  Default constant

Each enumeration has exactly one default constant which is used when the
user does not give a value for a feature with that enumeration type. In
this example, “phrase\_type\_unknown” might be the default.

#  Terminology

The constants are called *enumeration constants*, while the type
gathering the enumeration constants into one whole is called an
*enumeration*.

# Names are identifiers

The names of both enumerations and enumeration constants must be
*identifiers*.

# Each enumeration is a name-space

Each enumeration forms its own namespace. All name-spaces in the MQL
language are orthogonal to each other. This means that two enumeration
constants within the same enumeration cannot be called by the same
constant-identifier, but two enumeration constants in two different
enumerations may be the same. For more information, see section
[\[Namespaces\]](#Namespaces) for more information.

# Enumeration constants must be unique

Enumeration constants must be unique within each enumeration, both in
their values and in their names. For example, you cannot have two labels
with the same name in the same enumeration. Nor can you have two labels
with the same value in the same enumeration, even if the labels have
different names.

This is different from C or C++ enumerations, where the same value can
be assigned to different labels.

Thus an enumeration is effectively a one-to-one correspondence (also
called a bijective function) between a set of label names and a set of
values.
