#!/usr/bin/env python

import sys
import os
from py_isear.isear_loader import IsearLoader
import itertools
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier

import numpy

sys.path.insert(0, os.path.dirname(__file__))


data = ['TEMPER', 'TROPHO']
target = ['EMOT']
loader = IsearLoader(data,target)
dataset = loader.load_isear('isear.csv')

text_data_set = dataset.get_freetext_content()
target_set = dataset.get_target()
target_chain = itertools.chain(*target_set)
target_data = list(target_chain)

x_tr_data = text_data_set[:70]
x_tst_data = text_data_set[70:]
y_tr_data = target_data[:70]
y_tst_data = target_data[70:]

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                           alpha=1e-3, max_iter=5, random_state=42)),
                     ])
fitting = text_clf.fit(x_tr_data, y_tr_data)
res = text_clf.predict(x_tst_data)
print(res)

# turn the set in an array of boolean T|F and take the average of those
# 1.0 = perfect score, 0.0 is all mismatched
mn = numpy.mean(res == y_tst_data)
print(mn)
