1.1 Classification vs Regression:
- Classification: Predicts discrete labels. Example: Predicting if an email is spam or not (spam/ham).
- Regression: Predicts continuous values. Example: Predicting house prices based on features like size and location.

1.2 Median vs Mean Imputation:
- Prefer median imputation when data has outliers or is skewed, as the median is less affected by extreme values than the mean.

1.3 Five Python ML Libraries:
- scikit-learn
- TensorFlow
- Keras
- PyTorch
- XGBoost

1.4 Bias-Variance Trade-off Example:
- High bias: Underfitting, e.g., using a linear model for non-linear data (model too simple).
- High variance: Overfitting, e.g., using a very deep decision tree (model too complex).
- Trade-off: Find a model that balances both for best generalization.

2.1 Using Unlabeled Data in Supervised Learning:
- Unlabeled data can be used for semi-supervised learning or clustering, but supervised algorithms require labeled data for training.

2.2 Standardize 'Age' Feature:
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['Age_scaled'] = scaler.fit_transform(df[['Age']])

2.3 Overfitting vs Underfitting:
- Overfitting: Model fits training data too well, poor on new data. Example: Memorizing training set.
- Underfitting: Model too simple, poor on both training and test data. Example: Linear model for non-linear data.
Mitigation (Overfitting):
1. Use simpler models
2. Regularization
3. More training data
4. Cross-validation
Mitigation (Underfitting):
1. Use more complex models
2. Feature engineering
3. Reduce regularization
4. Train longer

2.4 Metrics Formulas & Calculation:
- Accuracy = (TP+TN)/(TP+TN+FP+FN)
- Precision = TP/(TP+FP)
- Recall = TP/(TP+FN)
- F1-score = 2*(Precision*Recall)/(Precision+Recall)
- Specificity = TN/(TN+FP)
Given: TP=40, FN=10, FP=20, TN=30
Accuracy = (40+30)/(40+30+20+10) = 70/100 = 0.7
Precision = 40/(40+20) = 40/60 = 0.67
Recall = 40/(40+10) = 40/50 = 0.8
F1 = 2*(0.67*0.8)/(0.67+0.8) ≈ 0.73
Specificity = 30/(30+20) = 30/50 = 0.6

3.1 (a) Load DataFrame:
```python
data = {'square_footage': [800,1200,1500,1800,2500,900,1100,2200],
        'num_bedrooms': [2,3,4,3,4,2,5,4],
        'age': [10,5,10,20,7,25,15,17],
        'location': ['Urban','Suburban','Urban','Urban','Rural','Urban','Suburban','Rural'],
        'price': [350000,245000,400000,300000,200000,250000,320000,280000]}
df = pd.DataFrame(data)

# (b) Separate Features/Target:
X = df.drop('price', axis=1)
y = df['price']

# (c) Label Encoding (One-hot):
df = pd.get_dummies(df, columns=['location'])

# (d) Train/Test Split:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# (e) Train Linear Regression & Predict:
model = LinearRegression()
model.fit(X_train, y_train)
new_house = pd.DataFrame({'square_footage':[2000], 'num_bedrooms':[5], 'age':[5], 'location':['Urban']})
new_house = pd.get_dummies(new_house)
pred_price = model.predict(new_house)
```
4.1 K-means Pseudocode:
1. Initialize k centroids randomly
2. Assign each point to nearest centroid
3. Update centroids as mean of assigned points
4. Repeat steps 2-3 until convergence

4.2 Accuracy Limitation:
- Accuracy can be misleading with imbalanced datasets; e.g., 95% accuracy if 95% of data is one class, even if model ignores minority class.

4.3 Decision Tree & Logistic Regression Training:
from sklearn.tree import DecisionTreeClassifier
# Decision Tree
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)
print('Decision Tree:', classification_report(y_test, y_pred_dt))
# Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
print('Logistic Regression:', classification_report(y_test, y_pred_lr))
