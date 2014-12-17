import numpy as np
from matplotlib.mlab import PCA as mlabPCA
import matplotlib.pyplot as plt
from load_data import read_data
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d


all_samples = read_data("data/train1.csv")

y_train = np.array([x[0] for x in all_samples])
X_train = np.array([x[1:] for x in all_samples])
	
data_array = X_train
mlab_pca = mlabPCA(data_array)

Class0 = [i for i in range(len(y_train)) if y_train[i]==0 ]
Class1 = [i for i in range(len(y_train)) if y_train[i]==1 ]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(mlab_pca.Y[Class0,0], mlab_pca.Y[Class0,1],mlab_pca.Y[Class0,2], 'o', markersize=8, color='blue', alpha=0.5, label='class1')
ax.plot(mlab_pca.Y[Class1,0], mlab_pca.Y[Class1,1],mlab_pca.Y[Class1,2], '^', markersize=8, alpha=0.5, color='red', label='class2')


#plt.plot(mlab_pca.Y[Class0,0],mlab_pca.Y[Class0,1],mlab_pca.Y[Class0,2] ,'o', markersize=7,color='blue', alpha=0.5, label='class1')
#plt.plot(mlab_pca.Y[Class1,0], mlab_pca.Y[Class1,1],mlab_pca.Y[Class1,2], '^', markersize=7,color='red', alpha=0.5, label='class2')

plt.show()
