import os
import psutil

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # Convert bytes to MB


print(f"Baseline RAM: {get_memory_usage():.2f} MB")

# --- Simulate what main.py loads at startup ---
import joblib
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

print(f"RAM after importing heavy libraries: {get_memory_usage():.2f} MB")

pipeline = joblib.load('../joblib_files/pipeline.joblib')
knn = joblib.load('../joblib_files/knn_model.joblib')
cluster_means_minmax = joblib.load('../joblib_files/cluster_means_minmax.joblib')
x_train = joblib.load('../joblib_files/x_train.joblib')
y_train = joblib.load('../joblib_files/y_train.joblib')
print(f"Final RAM after loading models: {get_memory_usage():.2f} MB")
