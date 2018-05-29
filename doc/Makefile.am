SUBDIRS = progref


LYXFILES = lyx/Monad-Sets.lyx \
           lyx/MQL-Programmers-Guide.lyx \
           lyx/MQL-Query-Guide.lyx \
           lyx/New-EMdF.lyx \
           lyx/Rel-EMdF.lyx \
           lyx/Standard-MdF.lyx

PDFFILES = $(LYXFILES:.lyx=.pdf)

TXTFILES = 

WIN32FILES = 

EXTRA_DIST = $(TXTFILES) $(WIN32FILES) \
             $(LYXFILES) $(PDFFILES) \
             lyx/TheDoor.fig lyx/TheDoor.eps

CLEANFILES = *~ core $(PDFFILES)

DISTCLEANFILES = 

BUILT_SOURCES = $(PDFFILES)

dist_doc_DATA = $(PDFFILES) $(TXTFILES)


#lyx/TheDoor.eps: lyx/TheDoor.fig
#	fig2dev -L eps lyx/TheDoor.fig lyx/TheDoor.eps

lyx/Monad-Sets.pdf : lyx/Monad-Sets.lyx
	$(LYX) -e pdf2 lyx/Monad-Sets.lyx

lyx/MQL-Query-subset.pdf: lyx/MQL-Query-subset.lyx lyx/TheDoor.eps
	$(LYX) -e pdf2 lyx/MQL-Query-subset.lyx

lyx/MQL-Programmers-Guide.pdf: lyx/MQL-Programmers-Guide.lyx  lyx/TheDoor.eps
	$(LYX) -e pdf2 lyx/MQL-Programmers-Guide.lyx

lyx/MQL-Query-Guide.pdf: lyx/MQL-Query-Guide.lyx  lyx/TheDoor.eps
	$(LYX) -e pdf2 lyx/MQL-Query-Guide.lyx

lyx/New-EMdF.pdf: lyx/New-EMdF.lyx
	$(LYX) -e pdf2 lyx/New-EMdF.lyx

lyx/Rel-EMdF.pdf: lyx/Rel-EMdF.lyx
	$(LYX) -e pdf2 lyx/Rel-EMdF.lyx

lyx/Standard-MdF.pdf: lyx/Standard-MdF.lyx  lyx/TheDoor.eps
	$(LYX) -e pdf2 lyx/Standard-MdF.lyx



MACDOCDISTDIR = $(MACDISTDIR)/doc

macdist: all 
	cp $(PDFFILES) $(MACDOCDISTDIR)/PDF
	cd progref ; make macdist MACDISTDIR=../$(MACDISTDIR) ; cd ..

