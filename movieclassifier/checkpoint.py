## Checkpoint - to load and test pickle

# import pickle
# import re
# import os
# from vectorizer import vect
# clf = pickle.load(open(os.path.join('pkl_objects','classifier.pkl'), 'rb'))
#
# import numpy as np
# label = {0:'negative', 1:'positive'}
# example = ['I love this movie']
# X = vect.transform(example)
# print('Prediction: %s\nProbability: %.2f%%' % (label[clf.predict(X)[0]],np.max(clf.predict_proba(X))*100))

## Checkpoint - sqlite db

import sqlite3
conn = sqlite3.connect('reviews.sqlite')
c = conn.cursor()
c.execute("SELECT * FROM review_db WHERE date"\
    " BETWEEN '2017-01-01 00:00:00' AND DATETIME('now')")
results = c.fetchall()
conn.close()
print(results)