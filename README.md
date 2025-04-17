# Secure CLI Password Manager 🔐

A serverless, secure **Command-Line Password Manager** built with **Python** and **AWS Cloud Services** — Lambda, API Gateway, and DynamoDB.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![AWS](https://img.shields.io/badge/Hosted_on-AWS_Lambda-yellow)
![License](https://img.shields.io/github/license/AnkurNahar/CLI-Password-Manager)

---

## 📜 Overview

This project allows you to **store** and **retrieve** encrypted passwords using a simple Python CLI. Data is encrypted **locally** using `cryptography.fernet`, then sent securely to a **serverless backend** via AWS API Gateway.

**Source Code**: [GitHub Repository](https://github.com/AnkurNahar/CLI-Password-Manager)

---

## 🚧 Architecture

```text
[ User CLI ]
     ↓
[ Python Script ]
     ↓
[ API Gateway (GET/POST) ]
     ↓
[ AWS Lambda ]
     ↓
[ DynamoDB Table ]
```
## 💡 Features

- 🔐 **Local encryption/decryption** using `cryptography.fernet`
- ☁️ **Serverless backend** using AWS Lambda + API Gateway
- 🧾 **Encrypted credential storage** in AWS DynamoDB
- 🧑‍💻 Clean and simple **command-line interface (CLI)**
- 🛡️ The encryption key is **never sent to the cloud**
- ✅ **Lambda function is included** in the project — can be hosted and used directly
- ⭐ Designed to be easily extendable for future

---

## ⚙️ Setup & Usage

### 1. Clone the repository
```bash
git clone https://github.com/AnkurNahar/CLI-Password-Manager.git
cd CLI-Password-Manager
```
### 2. Set Up AWS Lambda Hosting (Backend)

The Lambda function code is included in the project. You can host it using the AWS Console or AWS CLI:

1. Go to the [AWS Lambda Console](https://console.aws.amazon.com/lambda/).
2. Create a new Lambda function (Python 3.x runtime).
3. Upload the included Lambda function code (`lambda_function.py` or similar).
4. Set up an **API Gateway**:
   - Create a REST API with **POST** and **GET** methods.
   - Link them to your Lambda function.
5. Create a **DynamoDB table** with:
   - Partition Key: `service` (String)
   - Attributes: `username`, `password`
### 3. Set Up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```
### 4. Install Dependencies
```bash
pip install -r requirements.txt
```
### 5. Generate and Securely Store Your Encryption Key
```bash
from cryptography.fernet import Fernet
key = Fernet.generate_key()
# Save this key in a secure local location
# DO NOT upload this key to GitHub or include it in your Lambda code
```
### 6. Run the CLI Script
```bash
python cli.py
```
Follow the CLI prompts to store or retrieve credentials securely.

## 🔐 Security
- 🔒 Client-side encryption: Passwords are encrypted before they leave your device.
- 🔑 Key privacy: Your encryption key stays on your machine — never stored in the cloud.
- 🔁 Symmetric encryption: Uses Fernet from the cryptography library to securely encrypt/decrypt passwords.
- ❌ No plain text storage: All data stored in DynamoDB is encrypted.
