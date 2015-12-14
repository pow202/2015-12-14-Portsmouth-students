include config.mk

TXT_FILES=$(wildcard books/*.txt)
DAT_FILES=$(patsubst books/%.txt, %.dat, $(TXT_FILES))
PLT_FILES=$(patsubst books/%.txt, %.jpg, $(TXT_FILES))

# Count words.
%.dat : books/%.txt $(COUNT_SRC)
	$(COUNT_EXEC) $< $@

%.jpg : %.dat $(PLT_SOURCE)
	$(PLT_EXEC) $< $@

analysis.tar.gz : $(DAT_FILES) $(COUNT_SRC) $(PLT_FILES) $(PLT_SRC)
	tar -czf $@ $^

.PHONY : dats
dats : $(DAT_FILES)

.PHONY : plts
plts : $(PLT_FILES)

.PHONY : clean
clean : 
	rm -f *~
	rm -f $(DAT_FILES)
	rm -f $(PLT_FILES)
	rm -f analysis.tar.gz
