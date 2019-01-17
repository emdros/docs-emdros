# Database model and Query Language

In this section, we will show a bit about Emdros's database model and query language, to whet your appetite.

## Organizing principles

Emdros's database model supports modeling your text with any **object types** needed for your problem domain.  You declare your own object types, such as "document", "section", "paragraph", "token", etc.

Each **object type** is a collection of **objects**.  All objects in a given object type have the same attributes, called **features**.  The features are declared when declaring the object type.

Each object has a special feature called "**monads**".  It is a **set** of "monads", where a **"monad" is simply another name for "integer"**.  The set of integers (monads) is arbitrary, except it cannot be empty: It can consist of one monad (a singleton), or a stretch of monads (say, "{1,2,3}") or it can have **gaps** (e.g., "{1,2,5,6,7}").

## Object type declaration

The **text itself** is stored as objects with features.  You, the database creator, decide which object type(s) should hold the text.  You could declare an object type "token" with a feature "surface" of type "string":

```
CREATE OBJECT TYPE
[Token
    surface : STRING;
]
GO
```

This object type will have the feature "surface", into which you then put the surface text of that token.

The object type will also have a special feature called "monads", which is a set of monads.  Because of some mathematics called the "well-foundedness of the integers", it is possible to order any collection of sets of integers totally.  Therefore, we can use the sequence of the integers to establish the logical reading order of the text.

## Text object creation

For example, you might store the text "*He is good.*" as follows:

```
CREATE OBJECT  
FROM MONADS = {1}  
[Token
    surface := "He ";
]
GO  

CREATE OBJECT  
FROM MONADS = {2}  
[Token
    surface := "is ";
]
GO  


CREATE OBJECT  
FROM MONADS = {3}  
[Token
    surface := "good.";
]
GO  
```

## Annotation object creation

Now, if we want to say that this is a sentence, we can create another object type, "Sentence":


```
CREATE OBJECT TYPE
[Sentence]
GO
```

Again, this will have an implicit feature called "monads".  We can now create an object of this object type, saying the first three words of the database are a Sentence:

```
CREATE OBJECT  
FROM MONADS = {1-3}  
[Sentence]
GO  
```

As can be seen, the text object type(s) are declared in the exact same way as the annotation objects.  Emdros makes no distinction between what is text and what is annotation.


# Query language

Because the Token objects have sets of monads {1}, {2}, {3}, that are **subsets of** the set of monads of the Sentence object, {1,2,3}, they are thus "inside" the Sentence object, and are thus "part of" the Sentence.

The query language takes advantage of this.  For example, to find all Sentence objects in which there is a Token inside the Sentence which has the surface "is ", we can query like this:

```
SELECT ALL OBJECTS  
WHERE  
[Sentence
   [Token surface = "is "]
]
GO
```
