ARTNAME = desiderata

TEXNAME = $(ARTNAME).tex

PDFNAME = $(ARTNAME).pdf

CLEANFILES = $(ARTNAME).aux $(ARTNAME).log $(PDFNAME) *~


all: $(PDFNAME)

clean:
	rm -f $(CLEANFILES)

$(PDFNAME): $(TEXNAME)
	pdflatex $(TEXNAME)
	pdflatex $(TEXNAME)
