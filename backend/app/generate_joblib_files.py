import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer, StandardScaler, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import OPTICS

# Import data
data = pd.read_csv('../dataset/data.csv')
normal_data = pd.read_csv('../dataset/normal_data.csv')

# Build and fit pipeline
log_cols = ['avg_throughput_TPS', 'peak_throughput_TPS', 'RAM_size_GB']
preprocessor = ColumnTransformer(
    transformers=[
        ('pass', 'passthrough', ['idle_CPU_usage', 'peak_CPU_usage']),
        ('log', FunctionTransformer(np.log1p), log_cols)
    ],
)
pipeline = make_pipeline(preprocessor, StandardScaler())
pipeline.set_output(transform="pandas")

pipeline.fit(data)

# Fit OPTICS model
model = OPTICS(min_samples=20, xi=0.09, cluster_method='xi')
labels = model.fit_predict(normal_data)

# Find cluster means
cluster_means = []
for label in sorted(set(labels)):
    if label == -1:  # Skip noise points
        continue
    cluster_mean = normal_data[labels == label].mean(axis=0)
    cluster_means.append(cluster_mean)

# MinMax normalize the extracted cluster means
scaler = MinMaxScaler()
scaler.fit(normal_data)  # Fit on baseline normal data
cluster_means_minmax = scaler.transform(cluster_means)

# Create train sets
mask = labels != -1
X_train = normal_data[mask]
Y_train = labels[mask]

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, Y_train)

joblib.dump(pipeline, '../joblib_files/pipeline.joblib')
joblib.dump(knn, '../joblib_files/knn_model.joblib')
joblib.dump(X_train, '../joblib_files/x_train.joblib')
joblib.dump(Y_train, '../joblib_files/y_train.joblib')
joblib.dump(cluster_means_minmax, '../joblib_files/cluster_means_minmax.joblib')
