from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
x,y = make_blobs(n_samples=500, n_features=2, centers=3)


from sklearn.cluster import KMeans
y_pred = KMeans(n_clusters=4, random_state=9).fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], c=y_pred)
plt.show()
