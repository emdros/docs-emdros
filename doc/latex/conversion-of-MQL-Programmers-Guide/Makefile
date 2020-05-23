MARKDOWN_FORMAT = gfm

TARGETS = MQL1.tex MQL1.md MQL1.html MQL.html

all: $(TARGETS) MQL.md 

clean:
	rm -f *~ $(TARGETS)

MQL1.tex: MQL-Programmers-Guide.tex  convlatex.py
	python3 convlatex.py $< $@


MQL1.md: MQL1.tex
	pandoc -f latex -t $(MARKDOWN_FORMAT) -o $@ $<

MQL.md: MQL1.md convmd.py
	python3  convmd.py $< $@

MQL1.html: MQL.md
	pandoc -f $(MARKDOWN_FORMAT) -t html -o $@ $<

MQL.html: MQL1.html header.html footer.html
	cat header.html MQL1.html footer.html | sed -e 's_&lt;sub&gt;_<sub>_g;s_&lt;/sub&gt;_</sub>_g' > $@
