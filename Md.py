#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

a=pd.read_csv("New_dataset_com.csv")

a

a.describe()

pd.unique(a["label"])

a['label'].nunique()

a['label'].value_counts()

import seaborn as sns

a["N"].plot(kind="kde",legend=True),
a["P"].plot(kind="kde",legend=True),
a["K"].plot(kind="kde",legend=True)

a["temperature"].plot(kind="hist",bins=20)

a["humidity"].plot(kind="hist",bins=20)

a["ph"].plot(kind="hist",bins=20)

a["rainfall"].plot(kind="hist",bins=20)

Y=a["label"]
X=a.drop(["label"],axis=1)

X,Y

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X_train_scaled, y_train)
knn.score(X_test_scaled, y_test)

from sklearn.ensemble import GradientBoostingClassifier
grad = GradientBoostingClassifier().fit(X_train, y_train)
print('Gradient Boosting accuracy : {}'.format(grad.score(X_test,y_test)))

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(max_depth=8,n_estimators=100).fit(X_train, y_train)

print('RF Accuracy on training set: {:.2f}'.format(clf.score(X_train, y_train)))
print('RF Accuracy on test set: {:.2f}'.format(clf.score(X_test, y_test)))

# import pickle
# saved_model1 = pickle.dumps(knn)
# saved_model2 = pickle.dumps(grad)
# saved_model3 = pickle.dumps(clf)

# knn_from_pickle = pickle.loads(saved_model1)

# knn_from_pickle.predict(X_test)

# grad_from_pickle = pickle.loads(saved_model2)

# grad_from_pickle.predict(X_test)

# clf_from_pickle = pickle.loads(saved_model2)

# clf_from_pickle.predict(X_test)


# In[7]:


import pickle 


# In[20]:


filename = 'crop_predic_model'
pickle.dump(clf,open(filename,'wb'))
# model = pickle.load(open(filename,'rb'))
# model.predict(X_test)


# In[22]:


# new = model.predict([[30,74,78,19.72502284,16.07490517,7.808946831,68.30637204]])
# print(new)


# In[18]:


# result = knn.predict(X_test)
# result1=clf.predict(X_test)
# result2=grad.predict(X_test)

# print(result)
# print(result1)
# print(result2)
# print(clf.score(X_train, y_train))
# print(knn.score(X_train, y_train))
# print(grad.score(X_train, y_train))


# In[ ]:




