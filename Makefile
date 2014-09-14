START = noxxxnote draft blue
END = missing

all: paper ABSTRACT

ABSTRACT: $(PYTEX)/bin/clean $(PYTEX)/bin/lib.py abstract.tex
	@$(PYTEX)/bin/clean abstract.tex ABSTRACT

# 16 Nov 2010 : GWA : Add other cleaning rules here.

clean: rulesclean
	@rm -f ABSTRACT paper.pyg

include $(PYTEX)/make/Makerules
