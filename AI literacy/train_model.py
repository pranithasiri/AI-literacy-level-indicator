import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Load dataset
df = pd.read_csv("ai_literacy_dataset.csv")

X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Controlled depth so tree structure resembles paper
model = DecisionTreeClassifier(
    max_depth=4,
    min_samples_split=20,
    random_state=42
)

model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print("Accuracy:", accuracy)
print("\nClassification Report:\n")
print(classification_report(y_test, model.predict(X_test)))

joblib.dump(model, "ai_literacy_model.pkl")

print("\nModel saved as ai_literacy_model.pkl")

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(18,10))
plot_tree(
    model,
    feature_names=X.columns,
    class_names=model.classes_,
    filled=True
)
plt.show()