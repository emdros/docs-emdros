# What is a monad?

A monad is simply an integer.  No more, no less.

However, in the EMdF database model, we have two kinds of integers:

- Those integers that are simply integer values, and
- Those integers that are called "monads".

The "monad" integers are special.  We shall now explain why.


# Monads and textual sequence

Language is linear in nature. We produce language in real-time, with
sequences of sounds forming sequences of words. Text, being language, is
also linear in nature. In the EMdF model, this linearity is captured by
the monads.

A monad is simply an integer – no more, no less. The sequence of
integers (1,2,3,4,…) forms the backbone to which the flow of the text is
tied. Thus, because a monad is an integer, and because we can order the
integers in an unambiguous way, we use the sequence of monads to keep
track of the sequence of textual information.

The sequence of monads begins at 1 and extends upwards to some large
number, depending on the size of the database.

# Granularity

What unit of text does a monad correspond to? For example, does a monad
correspond to a morpheme, a word, a sentence, or a paragraph?

The answer is that you, the database user, decide the granularity of the
EMdF database. You do this before any text is put into the database. If
you want each monad to correspond to a morpheme, you simply decide that
this is so. A more common choice is for each monad to correspond to a
word. However, there is nothing implicit or explicit in the EMdF model
that prevents the user from deciding that another unit of text should
correspond to a monad. Be aware, however, that once the choice has been
made, and the database has been populated with text, it is not easy to
revoke the decision, and go from, say, a word-level granularity to a
morpheme-granularity.

# Text flow

What is the reading-order of an EMdF database? Is it left-to-right,
right-to-left, top-to-bottom, or something else?

The answer is that the EMdF model is agnostic with respect to
reading-order. In the EMdF model, what matters is the textual sequence,
as embodied by the monads. How the text is displayed on the screen is
not specified in the EMdF model.

The MQL query language provides for both 7-bit (ASCII) and 8-bit
encodings of strings, which means that the database implementor can
implement any character-set that can be encoded in an 8-bit encoding,
including Unicode UTF-8.

# Conclusion

A monad is an integer. The sequence of integers (1,2,3,4,…) dictates the
textual sequence. The granularity of an EMdF database is decided by the
database-implementor. The EMdF model is agnostic with respect to
reading-order (right-to-left, left-to-right, etc.).
