import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# ===============================
# 2️⃣ Load Dataset
# ===============================
# Replace with your file path
file_path = "Prashant.xlsx"

df = pd.read_excel(file_path)

print("Dataset Preview:")
print(df.head())

# ===============================
# 3️⃣ Data Preprocessing
# ===============================
# Keep only numerical columns
X = df.select_dtypes(include=['int64', 'float64'])

# Handle missing values (optional)
X = X.fillna(X.mean())

# Feature scaling (important for clustering)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ===============================
# 4️⃣ Finding Best Number of Clusters (Elbow Method)
# ===============================
inertia = []

for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X_scaled)
    inertia.append(model.inertia_)

plt.plot(range(1, 11), inertia, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.show()

# ===============================
# 5️⃣ Train K-Means Model
# ===============================
k = 3   # Change based on elbow graph
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Add cluster labels to dataset
df["Cluster"] = clusters

print(df.head())

# ===============================
# 6️⃣ Save Output
# ===============================
df.to_excel("clustered_output.xlsx", index=False)
print("Clustering complete! File saved.")