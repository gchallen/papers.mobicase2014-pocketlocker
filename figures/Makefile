TARGETS = single.pdf thin.pdf square.pdf double.pdf downloadtimes.pdf

all: $(TARGETS)
	@echo > /dev/null

single.pdf: $(PYTEX)/bin/blank
	@$< $@ 3.15 2.0

thin.pdf: $(PYTEX)/bin/blank
	@$< $@ 3.15 1.0

square.pdf: $(PYTEX)/bin/blank
	@$< $@ 2.5 2.5

double.pdf: $(PYTEX)/bin/blank
	@$< $@ 6.5 2.0

downloadtimes.pdf: downloadtimes.py
	@./$<

clean:
	@rm -f $(TARGETS)

.PHONY: clean all
