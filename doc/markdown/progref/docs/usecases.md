# Common use cases of Emdros

## Basic capabilities

Emdros provides these basic capabilities:

- **Store**: storage of annotated text
- **Query, Find**: querying of text + its annotation structure
- **Aggregate Query**: aggregate querying (counting, max/min, etc.)
- **Replay**: Re-assembly of (parts of) documents (replay)
- **FTS**: Full Text Search

## Storage characteristics

Depending on the storage engine, the following are also available:

- Single-file database (BPT, SQLite)
- Database encryption (BPT, SQLite)
- Database compression at-rest (BPT)
- Further database compression in-transit (BPT, SQLite)
- Small database size at-rest (BPT)
- Server-side databases (BPT, PostgreSQL, MySQL, MariaDB)

## Good usage cases

The following are good candidates for applications using Emdros:

1. Delivery of content to end-users (store, find, replay, display)

    1. On mobile
    2. On the desktop
    3. On the web
    
2. Querying text based on its structure (store, query, replay, display)

    1. Querying treebanks (linguistic syntax tree corpora)
    2. Querying plays (actors, lines, prose, poetry, etc.)
    3. Querying legal texts (laws, decisions, articles, chapters, sections, etc.)
    4. Querying Bibles (books, chapters, verses, sections, paragraphs, footnotes, etc.)
    5. DNA research (the structure of DNA is very much like natural language)
    
3. Statistical analysis of texts (store, query, count, display)

4. Full Text Search applications (store, query, filter, rank, replay, display)

5. Information retrieval


