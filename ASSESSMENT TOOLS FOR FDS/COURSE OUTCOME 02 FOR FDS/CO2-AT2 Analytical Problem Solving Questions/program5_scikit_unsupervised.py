from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Load dataset
iris = load_iris()

# Train KMeans model
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(iris.data)

cluster_labels = kmeans.labels_
print("--- KMeans Cluster Labels ---")
print(cluster_labels)