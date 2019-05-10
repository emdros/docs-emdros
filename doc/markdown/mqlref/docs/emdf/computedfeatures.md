# Computed features

The following computed features can always be used on any object type,
even though they are never declared:

- first\_monad(&lt;monad\_set\_name&gt;)

- last\_monad(&lt;monad\_set\_name&gt;)

- monad\_count(&lt;monad\_set\_name&gt;)

- monad\_set\_length(&lt;monad\_set\_name&gt;)

The “&lt;monad\_set\_name&gt;” inside the parentheses must be a valid
monad set name, such as the name of a feature of type “SET OF MONADS”,
or the privileged monad set feature, “`monads`”.

If the &lt;monad\_set\_name&gt; to be used is the privileged `monads`
monad set feature, the parenteses and the name “`monads`” can be
omitted, as a short-cut.

## Meaning

The features mean the folllowing:

- **first\_monad(&lt;monad\_set\_name&gt;):**  
  Retrieve the &lt;monad\_set\_name&gt; monad set, and yield its smallest
  (first) monad. For example, the monad set
  “{1-3}” has first\_monad = 1.

- **last\_monad(&lt;monad\_set\_name&gt;):**  
  Retrieve the &lt;monad\_set\_name&gt; monad set, and yield its largest
  (last) monad. For example, the monad set
  “{1-3}” has first\_monad = 3.

- **monad\_count(&lt;monad\_set\_name&gt;):**  
  Retrieve the &lt;monad\_set\_name&gt; monad set, and yields the number
  of monads in it, i.e., its cardinality. For example, the monad set
  “{1-3, 5}” has a monad\_count of 4,
  since it has 4 monads in it (“1, 2, 3, 5”). Also, the monad set
  “{3}” has a monad\_count of 1, while
  the monad set “{2-4}” has a
  monad\_count of 3 (“2, 3, 4”).

- **monad\_set\_length(&lt;monad\_set\_name&gt;):**  
  Retrieve the &lt;monad\_set\_name&gt; feature, and yield the number  
    
    `last_monad(monad_set_name) - first_monad(monad_set_name) + 1`
    
    For example, the set “{1-3, 5}” has a monad\_set\_length of 5 - 1
    + 1 = 5.  Note that if the monad set has no gaps, then this will
    be the same as monad\_count(&lt;monad\_set\_name&gt;). If, on the
    other hand, the monad set has gaps, the
    monad\_set\_length(&lt;monad\_set\_name&gt;) will be strictly
    greater than monad\_count(&lt;monad\_set\_name&gt;).
