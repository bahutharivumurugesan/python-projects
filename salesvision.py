import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Read CSV file
data = pd.read_csv("sales.csv")

# Print table
print(data)

# Input data
X = data[["Month"]]

# Output data
y = data["Sales"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict next month sales
prediction = model.predict([[11]])

print("Predicted Sales for Month 11:")
print(prediction[0])

# Draw graph
plt.scatter(X, y)

plt.plot(X, model.predict(X))

plt.title("SalesVision")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()