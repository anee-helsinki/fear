#!/usr/bin/python
# -*- coding: utf-8 -*-

import pmizer

#noHomonyms_text_Mar19    50 + 10
#rootsNoHomonyms_text_Mar19     50 + 10
#someSynonyms_text_Mar19
#noSynonyms_text_Mar19


set1 = {'words': ['râmu','narāmtu','narāmu','rāʾimu','adāru','ādiru','adru','galātu',
                         'gilittu','palāhu','palhu','pulhu','puluhtu','parādu','pirittu',
                         'šahātu','šahtu','agāgu ','uggatu','ezēzu','ezzu','uzzu','kimiltu',
                         'libbātu','raʾābu','šabāsu','šamāru','šamru','šitmuru','zenû'],
                         'source': 'noHomonyms_text_Mar19',
                         'dict': 'words_noHomonyms_text_Mar19'}

set2 = {'words': ['râmu','adāru','galātu','palāhu','parādu','šahātu','agāgu','ezēzu',
                              'kamālu','labābu','raʾābu','šabāsu','šamāru','zenû'],
                              'source': 'rootsNoHomonyms_text_Mar19',
                              'dict': 'words_rootsNoHomonyms_text_Mar19'}


set3 = {'words': ['râmu_1','adāru_2','galātu_1','palāhu_1','parādu_1','šahātu_1','agāgu_1',
                           'ezēzu_1','kamālu_1','labābu_1','raʾābu_1','šabāsu_1','šamāru_1','zenû_1'],
                           'source': 'someSynonyms_text_Mar19',
                           'dict': 'words_someSynonyms_text_Mar19'}

set4 = {'words': ['râmu_1','adāru_2','galātu_1','palāhu_1','parādu_1','šahātu_1','agāgu_1',
                         'ezēzu_1','kamālu_1','labābu_1','raʾābu_1','šabāsu_1','šamāru_1','zenû_1'],
                         'source': 'noSynonyms_text_Mar19',
                         'dict': 'words_noSynonyms_text_Mar19'}


inputfile = './emotions_data/emotionsMar19/rootsNoHomonyms_text_Mar19'
dictionary = './emotions_data/emotionsMar19/wordlist_not_separated'

def make(setti, top):
    words = setti['words']
    source = setti['source']
    dictionary = setti['dict']
    e = pmizer.Associations()
    e.set_window(size=10, symmetry=True)
    e.read_raw('./emotions_data/emotionsMar19/' + source)
    e.read_dictionary('./emotions_data/emotionsMar19/' + dictionary)
    e.set_constraints(freq_threshold=2,
                      freq_threshold_collocate=5,
                      distance_scaling=False,
                      words1=words)
    e.score_bigrams(pmizer.PPMI2)
    e.print_scores(top, gephi=True)
    e.write_tsv(source + '_' + str(top) + '.csv')

make(set1, 10)
'''
make(set1, 50)
make(set2, 10)
make(set2, 50)
make(set3, 10)
make(set3, 50)
make(set4, 10)
make(set4, 50)
'''
