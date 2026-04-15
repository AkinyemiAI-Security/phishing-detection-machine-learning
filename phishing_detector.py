---

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Sample dataset
data = {
    'url_length': [10, 50, 70, 15, 80, 25, 90],
    'has_https': [1, 0, 0, 1, 0, 1, 0],
    'num_dots': [1, 3, 4, 1, 5, 2, 6],
    'label': [0, 1, 1, 0, 1, 0, 1]  # 0 = safe, 1 = phishing
}

df = pd.DataFrame(data)

# Features and labels
X = df[['url_length', 'has_https', 'num_dots']]
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test prediction
test_url = [[65, 0, 4]]  # Example suspicious URL
prediction = model.predict(test_url)

if prediction[0] == 1:
    print("⚠️ Phishing URL detected")
else:
    print("✅ Safe URL")
