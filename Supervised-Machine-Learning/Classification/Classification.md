Below are **Week 3 notes** for **Supervised Machine Learning: Regression and Classification**, written in **clear `.md` format**, with **concise-but-detailed explanations** and **well-placed images** to build intuition—matching the style of Weeks 1 & 2.

You can **save this as `Week3_Supervised_ML.md`**.

---

```markdown
# Supervised Machine Learning: Regression and Classification
## Week 3 — Classification & Logistic Regression

---

## 1. Overview of Week 3

In Week 3, we move from predicting numbers (**regression**) to predicting **categories** (**classification**).
The primary model introduced is **Logistic Regression**, widely used for binary classification problems.

---

## 2. What is Classification?

**Classification** predicts a **discrete label** rather than a continuous value.

### Examples:
- Email → Spam / Not Spam
- Tumor → Benign / Malignant
- Transaction → Fraud / Not Fraud


::contentReference[oaicite:0]{index=0}


---

## 3. Why Not Use Linear Regression for Classification?

Problems with linear regression:
- Predictions can be **less than 0 or greater than 1**
- Outputs do not represent probabilities
- Poor decision boundaries

Hence, we use **Logistic Regression**, which outputs values between **0 and 1**.


::contentReference[oaicite:1]{index=1}


---

## 4. Logistic Regression Model

### Hypothesis Function

Logistic regression uses the **sigmoid function**:

\[
h_\theta(x) = g(\theta^T x)
\]

Where the sigmoid function is:

\[
g(z) = \frac{1}{1 + e^{-z}}
\]

- Output is always between **0 and 1**
- Interpreted as **probability**


::contentReference[oaicite:2]{index=2}


---

## 5. Interpretation of Logistic Regression Output

\[
h_\theta(x) = P(y = 1 \mid x)
\]

- If \( h_\theta(x) \ge 0.5 \) → predict **class 1**
- If \( h_\theta(x) < 0.5 \) → predict **class 0**

The threshold (usually 0.5) can be adjusted.

---

## 6. Decision Boundary

The **decision boundary** is the line (or surface) that separates classes.

- Defined by: \( \theta^T x = 0 \)
- Can be **linear or nonlinear**


::contentReference[oaicite:3]{index=3}


---

## 7. Logistic Regression Cost Function

Squared error does **not work well** for classification.

Instead, we use **log loss**:

### Cost Function
\[
J(\theta) = -\frac{1}{m} \sum_{i=1}^{m}
\left[
y^{(i)} \log(h_\theta(x^{(i)})) +
(1 - y^{(i)}) \log(1 - h_\theta(x^{(i)}))
\right]
\]

### Why This Cost?
- Convex function
- Penalizes confident wrong predictions heavily
- Works well with gradient descent


::contentReference[oaicite:4]{index=4}


---

## 8. Gradient Descent for Logistic Regression

Gradient descent is used to minimize the cost function.

### Update Rule:
\[
\theta_j := \theta_j - \alpha \frac{1}{m}
\sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) x_j^{(i)}
\]

This looks similar to linear regression but uses the **sigmoid hypothesis**.

---

## 9. Feature Mapping (Nonlinear Decision Boundaries)

To handle nonlinear data:
- Create new features like \( x_1^2, x_2^2, x_1x_2 \)
- Allows curved decision boundaries

⚠️ Feature scaling is important here.


::contentReference[oaicite:5]{index=5}


---

## 10. Overfitting and Underfitting

### Underfitting
- Model is too simple
- High bias
- Poor performance on training data

### Overfitting
- Model is too complex
- Fits noise
- Poor generalization


::contentReference[oaicite:6]{index=6}


---

## 11. Regularization

**Regularization** helps prevent overfitting by penalizing large parameters.

### Regularized Cost Function
\[
J(\theta) =
-\frac{1}{m} \sum \text{(log loss)}
+ \frac{\lambda}{2m} \sum_{j=1}^{n} \theta_j^2
\]

Where:
- \( \lambda \) = regularization parameter
- Larger \( \lambda \) → simpler model


::contentReference[oaicite:7]{index=7}


---

## 12. Effect of Regularization Parameter (λ)

- λ too small → overfitting
- λ too large → underfitting
- Choose λ using validation data

---

## 13. Week 3 Key Takeaways

✔ What classification problems are  
✔ Logistic regression hypothesis  
✔ Sigmoid function & probability interpretation  
✔ Decision boundaries  
✔ Cost function for classification  
✔ Regularization to reduce overfitting  

---

## 🚀 What Comes Next

- Multiclass classification
- Neural networks basics
- Advanced models

---

📘 **End of Week 3 Notes**
```

---

### Want next?

✅ **Week 4 / Neural Networks**
✅ **Python (NumPy) implementation for logistic regression**
✅ **Exam-focused revision sheets**
✅ **Combined Week 1–3 printable PDF**

Just tell me 👍
