# What is a feature?

A feature is a way of assigning data to an object. For example, say we
have an object of type “word”. Let us call this object “O”, and let us
say that it consists of the singleton monad set
{1}. Assume, furthermore, that the object
type “word” has a feature called “surface\_text”. Then this feature,
taken on the object O, might be the string “In”. This is denoted as
“O.surface\_text”. If we have another object, O\<sub\>2\</sub\>, which
consists of the singleton monad set {2},
the value O\<sub\>2\</sub\>.surface\_text might be “the”. Thus we know
that the first text in this EMdF database starts with the words “In
the”.

# Object types have features

An object type has a fixed number of features defined by the database
implementor. For example, it might be necessary for a particular
application to have these features on the object type “word”:

  - surface\_text

  - lexical\_form

  - part\_of\_speech

  - preceding\_punctuation

  - trailing\_punctuation

  - ancestor

The “ancestor” feature would be a pointer to another object, allowing
the user to create an immediate constituency hierarchy.

The object type “phrase” might have the following list of features:

  - phrase\_type

  - ancestor

# Features have types

An object type has a number of features. Each feature, in turn, has one
type. In the current implementation of the EMdF model, a feature can
have one of the following types:

  - integer

  - string (which is an 8-bit string)

  - ascii (which is a 7-bit ASCII string)

  - id\_d (which is an object id – we will get to this later)

  - enumeration (which we will also get to later in this chapter)

  - list of integer

  - list of id\_d

  - list of enumeration constants

  - sets of monads

