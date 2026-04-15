# Phishing Detection using Machine Learning 🎯

This project implements a machine learning-based system for detecting phishing URLs using extracted features and classification models.

## 🚀 Features
- URL-based phishing detection
- Feature extraction (URL length, HTTPS, special characters)
- Machine learning classification using Random Forest
- Model evaluation (accuracy score)

## 🛠 Technologies Used
- Python
- Scikit-learn
- Pandas

## 📊 Model Used
- Random Forest Classifier

## 🧠 Feature Explanation
- URL Length: Longer URLs may indicate obfuscation
- HTTPS: Absence of HTTPS can indicate insecurity
- Number of Dots: Excessive dots may signal malicious domains
- '@' Symbol: Often used in phishing URLs to confuse users

  ## 📈 Future Improvements
- Use real-world phishing datasets
- Improve feature engineering
- Apply deep learning models
- Integrate real-time detection system
  
⚠️ Disclaimer
This project is for educational and cybersecurity research purposes only.

👨‍💻 Author
Dr. Abiola Akinyemi

## ▶️ How to Run
```bash
python phishing_detector.py
