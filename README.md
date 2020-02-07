FEAR IN AKKADIAN TEXTS

This repository contains the data used for and generated during our research for the article Svärd et al., "Fear in Akkadian Texts" to be published in Shih-Wei Hsu and Jaume Llop-Raduà (eds.), The Expression of Emotions in Ancient Egypt and Mesopotamia. Culture and History of the Ancient Near East (Chane), Brill.

We studied five Akkadian words for fear - adāru, galātu, palāḫu, parādu and šaḫātu - and their derivatives. We used two language technological methods Pointwise Mutual Information (PMI) and fastText to study the meaning of these words and the contexts their are used in in all monolingual Akkadian documents in Open Richly Annotated Cuneiform Corpus (Oracc, http://oracc.museum.upenn.edu, see oracc_data/ and textInformation/).

We made two textfiles from our dataset, each with a different pre-processing level (see textsAnalysed/):
Level 1 is made with minimal preprocessing. Only lemmas (dictionary forms) of verbs, nouns, and adjectives have been used. All other words have been replaced with a placeholder (_). Divine names have been standardized (see lists/gods_combined_variants.txt). Place names tagged in Oracc GN (geographical name), SN (settlement name), and TN (temple name) have also been standardized (see lists/places_combined_variants.txt). Place names have also been marked with a trailing ‘_p’. Personal names (PN) and royal names (RN) have been replaced with PERSON and ROYALTY respectively.
For level 2, homonymous words have been separated automatically based on translations given in Oracc metadata. Words with synonymous translations are kept together automatically and with a partly manually compiled list (see lists/notHomonyms). Derivatives of the emotion words under scrutiny have then been collapsed to their verbal roots.

In order to analyse the results we got from our methods, we used Gephi to visualize them (see network_data/ and visualizations/).

The folders contain:

<b>network-data:</b> Gephi datasets and raw data used to create the graphs

<b>scripts:</b> scripts created to analyze our data

<b>texts:</b> text corpus from which the network data was extracted

<b>visualizations:</b> visualizations of the networks

<b>lists:</b> lists of standardized divine and place names; frequency lists of the words analyzed

<br><br>

<p align="center">
<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a><br />These files are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.</p>
