Preprocessed texts used for analysis with PMI and fastText in Svärd et al., “Fear in Akkadian Texts”.

Level 1 is made with minimal preprocessing. Only lemmas (dictionary forms) of verbs, nouns, and adjectives have been used. All other words have been replaced with a placeholder (_). Divine names have been standardized (see lists/gods_combined_variants.txt). Place names tagged in Oracc GN (geographical name), SN (settlement name), and TN (temple name) have also been standardized (lists/places_combined_variants.txt). Place names have also been marked with a trailing ‘_p’. Personal names (PN) and royal names (RN) have been replaced with PERSON and ROYALTY respectively.

For level 2, homonymous words have been separated automatically based on translations given in Oracc metadata. Words with synonymous translations are kept together automatically and with a partly manually compiled list (see lists/notHomonyms). Derivatives of the emotion words under scrutiny have also been collapsed to their verbal roots. 

Both files contain one document per line. For the metadata on the documents see textInformation/documents_used.
