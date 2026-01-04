Below are **complete Week-1 additions** for the Coursera *Machine Learning* course, exactly as requested:

* 🧮 **Numerical solved examples**
* 🧑‍💻 **Python code (Week-1 level)**
* 📊 **Exam questions with answers**

All content matches **Week 1 scope** (Supervised Learning + Linear Regression basics).

---

# 🧮 PART 1: NUMERICAL SOLVED EXAMPLES (WEEK 1)

---

## ✅ Example 1: Simple Linear Regression Prediction

### **Problem**

A dataset shows the relationship between **house size (x)** and **price (y)**.

| x (size in 1000 sq.ft) | y (price in $1000) |
| ---------------------- | ------------------ |
| 1                      | 300                |
| 2                      | 500                |

Assume the hypothesis:
[
h_\theta(x) = \theta_0 + \theta_1 x
]

Given:

* ( \theta_0 = 100 )
* ( \theta_1 = 200 )

### **Find**

Predict price for a house of size **x = 1.5**

### **Solution**

[
h_\theta(1.5) = 100 + 200(1.5)
]
[
= 100 + 300 = 400
]

### ✅ **Answer**

Predicted price = **$400,000**

---

## ✅ Example 2: Cost Function Calculation (MSE)

### **Problem**

Given:

* ( h_\theta(x) = 100 + 200x )
* Training data:

| x | y   |
| - | --- |
| 1 | 300 |
| 2 | 500 |

### **Cost Function**

[
J(\theta) = \frac{1}{2m} \sum (h_\theta(x^{(i)}) - y^{(i)})^2
]

### **Step 1: Predictions**

* ( h(1) = 300 )
* ( h(2) = 500 )

### **Step 2: Errors**

* ( (300 - 300)^2 = 0 )
* ( (500 - 500)^2 = 0 )

### **Step 3: Cost**

[
J = \frac{1}{2(2)}(0 + 0) = 0
]

### ✅ **Answer**

Cost = **0** (perfect model)

---

## ✅ Example 3: One Step of Gradient Descent

### **Given**

* ( \theta_0 = 0 ), ( \theta_1 = 0 )
* Learning rate ( \alpha = 0.1 )
* One data point: ( x = 1, y = 2 )

### **Gradient Descent Update**

[
\theta_1 := \theta_1 - \alpha (h(x)-y)x
]

### **Compute**

* ( h(x) = 0 )
* Error = ( 0 - 2 = -2 )

[
\theta_1 := 0 - 0.1(-2)(1) = 0.2
]

### ✅ **Answer**

Updated ( \theta_1 = 0.2 )

---

# 🧑‍💻 PART 2: PYTHON CODE (WEEK 1 LEVEL)

> No libraries beyond **NumPy**
> No scikit-learn (introduced later)

---

## ✅ Example 1: Linear Regression Prediction

```python
# Hypothesis function
def predict(x, theta0, theta1):
    return theta0 + theta1 * x

# Given values
theta0 = 100
theta1 = 200
x = 1.5

y_pred = predict(x, theta0, theta1)
print("Predicted value:", y_pred)
```

### Output

```
Predicted value: 400.0
```

---

## ✅ Example 2: Cost Function (MSE)

```python
import numpy as np

# Data
x = np.array([1, 2])
y = np.array([300, 500])

theta0 = 100
theta1 = 200
m = len(x)

# Predictions
h = theta0 + theta1 * x

# Cost function
J = (1 / (2 * m)) * np.sum((h - y) ** 2)
print("Cost:", J)
```

---

## ✅ Example 3: One Iteration of Gradient Descent

```python
# Single data point
x = 1
y = 2

theta0 = 0
theta1 = 0
alpha = 0.1

# Prediction
h = theta0 + theta1 * x

# Gradient descent update
theta1 = theta1 - alpha * (h - y) * x

print("Updated theta1:", theta1)
```

---

# 📊 PART 3: EXAM QUESTIONS & ANSWERS (WEEK 1)

---

## 🔹 Very Short Answer (1–2 marks)

### Q1. Define Machine Learning.

**Answer:**
Machine Learning is the field of study that enables computers to learn from data without being explicitly programmed.

---

### Q2. What is supervised learning?

**Answer:**
Supervised learning uses labeled data to learn a mapping from inputs to outputs.

---

### Q3. What is regression?

**Answer:**
Regression is a supervised learning task used to predict continuous values.

---

## 🔹 Short Answer (3–5 marks)

### Q4. Differentiate between regression and classification.

**Answer:**

| Regression                 | Classification           |
| -------------------------- | ------------------------ |
| Predicts continuous values | Predicts discrete labels |
| Example: house prices      | Example: spam detection  |

---

### Q5. What is a hypothesis in machine learning?

**Answer:**
A hypothesis is a function that maps input features to predicted outputs and represents the model.

---

## 🔹 Long Answer (8–10 marks)

### Q6. Explain the cost function used in linear regression.

**Answer:**
The cost function measures how well a model fits training data. In linear regression, Mean Squared Error is used:

[
J(\theta) = \frac{1}{2m}\sum (h_\theta(x) - y)^2
]

It penalizes large errors and helps guide optimization.

---

### Q7. Explain gradient descent with formula.

**Answer:**
Gradient descent is an iterative optimization algorithm used to minimize the cost function by updating parameters in the direction of steepest descent.

[
\theta_j := \theta_j - \alpha \frac{\partial J}{\partial \theta_j}
]

Where α is the learning rate.

---

## 🔹 MCQs (Common in Coursera)

**Q8. Which learning rate causes divergence?**
A. Very small
B. Moderate
C. Very large ✅
D. Zero

---

**Q9. What does m denote?**
A. Number of features
B. Number of parameters
C. Number of training examples ✅
D. Learning rate

---

# ✅ WEEK 1 COMPLETE ✔️

You now have:

* ✔ Numerical problems
* ✔ Python code
* ✔ Exam Q&A

---

If you want next:
➡ **Week 2 notes**
➡ **PDF notes**
➡ **Interview-focused questions**
➡ **Handwritten-style diagrams**

Just tell me 👍
