from py_isear.isear_loader import IsearLoader
import itertools
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn import metrics
import py_isear.enums

import numpy

data = ['TEMPER','TROPHO']
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
                                            alpha=1e-3, n_iter=5, random_state=42)),
                 ])
fitting = text_clf.fit(x_tr_data,y_tr_data)
res = text_clf.predict(x_tst_data)
print res

mn = numpy.mean(res == y_tst_data)
print mn
# report = metrics.classification_report(y_tst_data,re
