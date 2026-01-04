Below are **Week 2 notes** for **Supervised Machine Learning: Regression and Classification**, written in **clear `.md` format**, with **moderate detail** (concept + intuition) and **well-placed images** for visual understanding—matching the style and depth of Week 1.

You can **save this as `Week2_Supervised_ML.md`**.

---

```markdown
# Supervised Machine Learning: Regression and Classification
## Week 2 — Multiple Linear Regression & Feature Scaling

---

## 1. Overview of Week 2

In Week 2, we extend **linear regression** to handle **multiple input features**, learn how to **efficiently train models**, and understand why **feature scaling** and **vectorization** are critical for performance.

---

## 2. Multiple Linear Regression

### What is Multiple Linear Regression?

Multiple linear regression is used when:
- There are **multiple input features**
- Each feature contributes to predicting the output

### Example:
Predicting house price using:
- Size (sqft)
- Number of bedrooms
- Number of floors
- Age of the house


::contentReference[oaicite:0]{index=0}


---

## 3. Hypothesis Function (Multiple Variables)

The hypothesis for multiple features is:

\[
h_\theta(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_n
\]

Where:
- \( x_1, x_2, \dots, x_n \) are features
- \( \theta_0 \) is the bias (intercept)
- \( \theta_1, \dots, \theta_n \) are feature weights

Each parameter controls **how strongly a feature influences the output**.

---

## 4. Vectorized Representation

To simplify notation, we use vectors:

\[
h_\theta(x) = \theta^T x
\]

Where:
- \( \theta = [\theta_0, \theta_1, \dots, \theta_n] \)
- \( x = [1, x_1, x_2, \dots, x_n] \)

This form allows **efficient computation** using linear algebra.


::contentReference[oaicite:1]{index=1}


---

## 5. Gradient Descent for Multiple Variables

Gradient descent updates **all parameters simultaneously**.

### Update Rule:
\[
\theta_j := \theta_j - \alpha \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) x_j^{(i)}
\]

Where:
- \( j = 0, 1, 2, \dots, n \)
- Each parameter learns from its corresponding feature

---

## 6. Feature Scaling

### Why Feature Scaling?

When features have **very different ranges**, gradient descent:
- Converges slowly
- May oscillate or behave unstably

### Example:
- Size: 0 – 2000 sqft
- Bedrooms: 1 – 5

Scaling brings features into **similar ranges**.


::contentReference[oaicite:2]{index=2}


---

## 7. Mean Normalization & Standardization

### Mean Normalization
\[
x := \frac{x - \mu}{\text{range}}
\]

### Standardization
\[
x := \frac{x - \mu}{\sigma}
\]

Where:
- \( \mu \) = mean
- \( \sigma \) = standard deviation

🎯 Goal: Make features roughly in range **[-1, 1]**

---

## 8. Choosing the Learning Rate

To verify gradient descent is working:
- Plot **cost vs iterations**
- Cost should **decrease smoothly**

Signs of problems:
- Cost increases → learning rate too large
- Cost decreases very slowly → learning rate too small


::contentReference[oaicite:3]{index=3}


---

## 9. Polynomial Regression

Sometimes data is **not linear**.

### Idea:
- Create new features like \( x^2, x^3 \)
- Use linear regression on these features

Example hypothesis:
\[
h_\theta(x) = \theta_0 + \theta_1 x + \theta_2 x^2
\]

⚠️ Always apply **feature scaling** when using polynomial features.


::contentReference[oaicite:4]{index=4}


---

## 10. Normal Equation (Alternative to Gradient Descent)

The **Normal Equation** computes parameters directly:

\[
\theta = (X^T X)^{-1} X^T y
\]

### When to Use:
- Small to medium datasets
- No need to choose learning rate
- No iterations required

### When NOT to Use:
- Very large number of features (computationally expensive)


::contentReference[oaicite:5]{index=5}


---

## 11. Gradient Descent vs Normal Equation

| Gradient Descent | Normal Equation |
|-----------------|----------------|
| Needs learning rate | No learning rate |
| Iterative | Direct solution |
| Works for large features | Slow for large features |
| Requires feature scaling | No scaling needed |

---

## 12. Week 2 Key Takeaways

✔ Multiple linear regression  
✔ Vectorized hypothesis  
✔ Gradient descent with many features  
✔ Feature scaling & normalization  
✔ Polynomial regression  
✔ Normal equation vs gradient descent  

---

## 🚀 What’s Next (Week 3 Preview)

- Classification problems  
- Logistic regression  
- Decision boundaries  
- Cost function for classification  

---

📘 **End of Week 2 Notes**
```

---

### Want me to continue?

✅ **Week 3 (Logistic Regression)**
✅ **Python implementation examples**
✅ **Exam-oriented revision notes**
✅ **Combined Week 1–3 PDF**

Just tell me 👍
