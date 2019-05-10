# Databases

The EMdF model has a concept of “database.” It is an organizational
concept which generally corresponds to what the back-end database
system calls a “database.” Within a database, there is one string of
monads starting at 1 and extending upwards to some very large
number. Within this stretch of monads, the user is free to create
objects.

You may need to issue the USE DATABASE statement as the first thing
you do before doing anything else, in order to tell Emdros which
database you want to deal with. Ask the implementor of your Emdros
application whether this is what you should do.

A database can be created with the CREATE DATABASE statement.
