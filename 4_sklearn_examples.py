import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.cluster import KMeans

print("--- Scikit-learn Logistic Regression Example ---")
iris = datasets.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

log_reg = LogisticRegression(max_iter=200)
log_reg.fit(X_train, y_train)

y_pred = log_reg.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Classification report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names), "\n")

print("--- Scikit-learn KMeans Clustering Example ---")
iris2 = datasets.load_iris()
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(iris2.data)
cluster_labels = kmeans.labels_
print("Cluster Labels:", cluster_labels, "\n")

fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(iris2.data[:, 0], iris2.data[:, 1], c=cluster_labels, cmap='viridis')
legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
ax.add_artist(legend1)
ax.set_title("KMeans Clustering on Iris")
ax.set_xlabel(iris2.feature_names[0])
ax.set_ylabel(iris2.feature_names[1])
plt.savefig("C:\\Users\\V B KHANISHK\\data_analysis_scripts\\data_analysis_4_kmeans.png")
print("Saved KMeans plot to data_analysis_4_kmeans.png")
plt.close(fig)
