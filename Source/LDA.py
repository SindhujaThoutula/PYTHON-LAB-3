import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
iris = datasets.load_iris()
A=iris.data
B=iris.target
target_names = iris.target_names
A_train, A_test, B_train, B_test = train_test_split(A, B,test_size=0.20)
cf = KNeighborsClassifier(n_neighbors=3)
cf.fit(A_train,B_train)
B_pred = cf.predict(A_test)
l = LinearDiscriminantAnalysis(n_components=3)
A_R = l.fit(A_test, B_pred).transform(A)
colors=['blue','red','black']
for color,i,target_name in zip(colors,[0, 1, 2],target_names):
 plt.scatter(A_R[B == i,0],A_R[B == i,1],alpha=1,color=color,label=target_name)
plt.legend(loc='best',shadow=False,scatterpoints=1)
plt.show()