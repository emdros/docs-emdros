# Origins of EMdF and MQL

EMdF and MQL are based on two PhD dissertations.  Thus they both rest
on solid theoretical foundations.

Most of the ideas underlying the EMdF model and the MQL query language
are to be found in the PhD thesis of **Crist-Jan Doedens**, published
in 1994 [1]. This thesis described, among other things, the *MdF*
database model and the *QL* query language.

As one might guess, EMdF stems from MdF, and MQL stems from QL.  The
EMdF model takes over the MdF model in its entirety, but adds a few
concepts which are useful when implementing the MdF model in real
life. Thus the ‘E’ in ‘EMdF’ stands for “Extended”, yielding the
“Extended MdF model”. The EMdF model is the subject of chapter 2.

“MQL” stands for “Mini QL.”  Originally, MQL was devised by Ulrik
Sandborg-Petersen as a subset of the QL query language developed in
Dr. Doedens’ PhD thesis, hence the “Mini” modifier. Since then,
however, MQL has grown. QL was not a full access language, but
specified only how to *query* an MdF database, i.e., how to ask
questions of it. MQL, by contrast, is a *full access language*,
supporting not only querying, but also creation, update, and deletion
of the data domains of the EMdF model. The MQL query language is the
subject of chapters 3, 4, 5 and 6.

The core of the MQL query language was originally described in Ulrik
Sandborg-Petersen's B.Sc. thesis [2].  Ulrik then developed Emdros on
the basis of this B.Sc. thesis, and by 2004, he had written an MA
thesis about it [3].  Then, in 2008, he wrote a PhD thesis about
it [4].

## Bibliograpy

[1]: Doedens, Crist-Jan (1994): "Text Databases: One Database Model,
and Several Query Languages", Editions Rodopi.

[2]: Petersen, Ulrik (2000): "The EMdF model and the MQL query
language". Unpublished B.Sc. thesis, Aarhus University, Denmark.

[3]: Petersen, Ulrik (2004): "Creation in Graphs", MA thesis, Aalborg
University, Denmark.

[4]: Sandborg-Petersen, Ulrik (2008): "Text databases in the context
of the Kaj Munk Archive", PhD thesis, Aalborg University, Denmark.
