
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Expanded dataset (simulated features)
data = {
    'url_length': [10, 50, 70, 15, 80, 25, 90, 45, 60, 30],
    'has_https': [1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    'num_dots': [1, 3, 4, 1, 5, 2, 6, 2, 4, 1],
    'has_at_symbol': [0, 1, 1, 0, 1, 0, 1, 0, 1, 0],
    'label': [0, 1, 1, 0, 1, 0, 1, 0, 1, 0]  # 0 = safe, 1 = phishing
}

df = pd.DataFrame(data)

# Features and labels
X = df[['url_length', 'has_https', 'num_dots', 'has_at_symbol']]
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Test custom URL
test_url = [[65, 0, 4, 1]]  # suspicious features
prediction = model.predict(test_url)

if prediction[0] == 1:
    print("⚠️ Phishing URL detected")
else:
    print("✅ Safe URL")
