

# 🛡️ Security Mechanism in AI-Based Medical Image Encryption(30% implemented till now)

## 🏥 Project Overview

This project establishes a **privacy-preserving, blockchain-enabled, and attack-resilient framework** for collaborative medical image analysis. While Electronic Health Records (EHRs) advance diagnostics, they are vulnerable to **backdoor attacks** and data poisoning. This framework combines **Federated Learning (FL)** and **Differential Privacy (DP)** to enable multi-hospital collaboration without sharing sensitive raw patient data.

### ✨ Key Innovations

**Decentralized Trust**: Integration of **Blockchain technology** to provide decentralized trust, tamper-proof record-keeping, and transparent verification.
**End-to-End Encryption**: Use of **Fully Homomorphic Encryption (FHE)** to perform secure model aggregation directly on encrypted model updates.
**Attack Resilience**: Specialized modules for **Backdoor Attack Detection** to identify subtle triggers designed to mislead ML models.



---

## 🛠️ Tech Stack

**Deep Learning**: TensorFlow 2.15.0, Keras 2.15.0.
**Encryption**: Microsoft SEAL (via Pyfhel 2.3.1).
**Privacy**: Differential Privacy (Gaussian mechanism).
**Data Science**: Scikit-learn, NumPy, Pandas.
**Infrastructure**: Federated Learning (FedAvg) and Private Blockchain.



---

## 🧪 Key Technical Features

### 🏗️ Proposed System Architecture

The architecture is designed to handle local training at multiple hospital nodes while ensuring a global model is aggregated safely:

**Local Nodes**: Hospitals perform model training on local datasets without transmitting raw data.

**Differential Privacy**: Noise is added to model updates before sharing to prevent sensitive information leakage.

**Aggregation Block**: Encrypted updates are aggregated on the central server to form a global model.

**Blockchain Layer**: Records all updates via smart contracts to ensure an immutable audit trail.



---

## 🚀 Getting Started

### 1. Prerequisites

Install the required hardware and software dependencies:


**Hardware**: Min 8GB RAM (16GB recommended) and Intel i7 processor or higher.


* **Libraries**:

```bash
pip install tensorflow==2.15.0 keras==2.15.0 scikit-learn numpy pandas pyfhel

```

### 2. Prepare Data

The project includes a structured pipeline for medical images (X-rays, MRIs):
 
**Preprocessing**: Normalization, resizing, and patient data anonymization for privacy compliance.
**Dataset Division**: Partitioning data into training, testing, and validation samples across federated nodes.



```bash
python data_preprocessing.py

```

### 3. Training & Evaluation

The training phase integrates security protocols with performance tracking:

**Federated Execution**: Clients encrypt local updates using FHE and send them to the server.
**Security Verification**: Smart contracts verify the authenticity of updates before they are added to the global model.
**Evaluation**: Performance is assessed using Accuracy, Precision, Recall, and F1-Score.



```bash
python main.py

```

---

## 📊 Evaluation Metrics

The framework is designed to achieve:

**Accuracy**: Targeted above 90% for medical datasets.
**Integrity**: Resilience against data poisoning and inference attacks.
**Confidentiality**: End-to-end encryption using Homomorphic Encryption.



---

## 📂 Repository Structure
`client.py`: Handles local model training and weight encryption.
`server.py`: Manages communication and aggregates encrypted updates.
`encryption.py`: Implements homomorphic encryption/decryption methods.
`main.py`: Controls workflow initialization, aggregation, and evaluation.




