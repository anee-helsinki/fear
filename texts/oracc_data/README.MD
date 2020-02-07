Text corpus from which the data was extracted for analysis.

The corpus was extracted from the json files downloaded from Open Richly Annotated Cuneiform Corpus in February 2019. For extracting the words from those files we used a modified version of a script that was originally composed by Niek Veldhuis (https://github.com/niekveldhuis/ORACC-JSON/blob/master/json-corpus.ipynb).

Each file contains a word per line. Each line starts with the document number with the line number and the word number on the line. After the wordform comes the different metadata of the word in question.

E.g. suhu/Q006206.6.2	form:{GIŠ}TUKUL.MEŠ	lemma:kakku	gw:stick	wclass:N	norm:kakkī	sense:weapon 	epos:N	lang:akk	signs:𒄑𒆪𒈨𒌍

lemma = dictionary form;
gw = guide word = translation of the dictionary form;
wclass = wordclass of the dictionary form;
norm = transcription of the word;
sense = translation of the transcription;
epos = wordclass of the transcription;
lang = language of the word;
signs = cuneiform signs forming the word;
