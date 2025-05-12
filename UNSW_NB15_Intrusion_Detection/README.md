# 🚨 Intrusion Detection Using Unsupervised Learning on UNSW-NB15 Dataset

This project explores the application of **unsupervised machine learning techniques** to detect anomalies and potential intrusions in the **UNSW-NB15 network traffic dataset**. The goal is to identify malicious behavior without relying on labeled data in production environments.

## 📂 Dataset

- **Source**: UNSW-NB15 from the Australian Centre for Cyber Security
- **Features**: Network traffic characteristics (both statistical and protocol-level)
- **Target**: Binary classification (0 = normal, 1 = attack)
- **Note**: Only numeric features are used in this notebook.

> ⚠️ Make sure the dataset file `UNSW_NB15_training-set.csv` is available locally or in your Colab environment. Adjust file paths as needed.

## 🧪 Methods Used

### 📊 Preprocessing
- Sampled 2000 normal and 500 attack records for balanced analysis
- Scaled features using `StandardScaler`

### 🤖 Unsupervised Models
- **DBSCAN**:
  - Tuned with K-distance elbow method
  - Noise points interpreted as anomalies
- **Isolation Forest**:
  - Tree-based model for outlier detection
  - Evaluated across multiple threshold settings

### 📈 Evaluation Metrics
- Silhouette Score (DBSCAN)
- Confusion Matrix, Classification Report (Isolation Forest)
- Precision, Recall, F1-score

### 📌 Visualizations
- PCA 2D Projection of Clusters
- Feature Importance Bar Charts
- K-Distance Plot for DBSCAN
- (Optional) Confusion Matrix Heatmap

## 💡 Insights

- Unsupervised models can detect attacks **without prior labels**, making them suitable for real-world anomaly detection systems.
- Feature importance analysis provides visibility into which network attributes contribute most to anomaly scores.
- DBSCAN performs well when clusters are well-separated; Isolation Forest adds robustness for high-dimensional settings.

## 🚀 How to Run

1. Open the notebook in Jupyter or Google Colab.
2. Upload or mount the dataset (`UNSW_NB15_training-set.csv`).
3. Run all cells sequentially.
4. (Optional) Tune parameters like DBSCAN `eps` or Isolation Forest threshold for experimentation.

## 📌 Future Work

- Add more visual diagnostics (t-SNE, UMAP)
- Create reusable functions and modular pipelines
- Integrate supervised models for hybrid approaches
- Package as a lightweight anomaly detection service

## 📜 License

To be added.

---

*Author: Murat Çağrı Özkan*
