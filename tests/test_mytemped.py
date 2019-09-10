

#!/usr/bin/python
# -*- coding=utf-8 -*-
#
"""
Arabic Named enteties recognation pyarabic.named
@author: Taha Zerrouki
@contact: taha dot zerrouki at gmail dot com
@copyright: Arabtechies,  Arabeyes,   Taha Zerrouki
@license: GPL
@date:2017/02/14
@version: 0.3
"""
from __future__ import (
    absolute_import,
    print_function,

    unicode_literals,
    division,
    )
import pyarabic.araby as araby

import sys
sys.path.append('../')
import mishtar.mytemped as mytemped
import pandas as pd

if __name__ == '__main__':
    xls=pd.ExcelFile("C:/Users/user/Documents/Dataset1.xlsx")


    pageX=xls.parse(0)
    var = pageX['Input']
    

    text=var[4]
    texte=araby.strip_tashkeel(text)
    chunker = mytemped.myTemped()
    word_list = araby.tokenize(texte)
    tag_list2 = chunker.detect_chunks(word_list)
    result = chunker.extract_chunks(texte)
    

    tuples = (zip(tag_list2, word_list))
    for tup in tuples:
        print(repr(tup)           )
            #~ print(tup)




        


