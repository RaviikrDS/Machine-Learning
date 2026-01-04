https://chatgpt.com/s/t_695a25e47b8081919fa77bbc0e72b8e9

Week 3 primarily introduces **Classification** with a focus on **Logistic Regression**.

---

# 📘 **Week 3: Classification & Logistic Regression**

---

## 1️⃣ Why Classification?

In many real-world problems, the output is **categorical**, not continuous.

### Examples:

* Email → *Spam / Not Spam*
* Medical test → *Disease / No Disease*
* Transaction → *Fraud / Not Fraud*

📌 Linear regression is **not suitable** for such problems because its output is unbounded.

---

## 2️⃣ Classification Problem Setup

* Input features: ( x )
* Output labels: ( y \in {0, 1} )

  * 0 → Negative class
  * 1 → Positive class

Goal: **Estimate the probability that y = 1 given x**

[
P(y=1 \mid x)
]

![Image](https://www.researchgate.net/publication/285653348/figure/fig5/AS%3A669589956460558%401536654094794/This-illustration-present-a-binary-classification-that-is-performed-on-two-features-The.png)

![Image](https://towardsdatascience.com/wp-content/uploads/2022/02/1R6Rbcks-pGO0SkhCINrP0g.png)

---

## 3️⃣ Logistic Regression

Despite the name, **logistic regression is a classification algorithm**.

### Key Idea:

Instead of predicting a number directly, it predicts a **probability** between 0 and 1.

---

## 4️⃣ Sigmoid (Logistic) Function

The sigmoid function maps any real number into the range (0,1).

[
g(z) = \frac{1}{1 + e^{-z}}
]

Where:
[
z = \theta^T x
]

### Properties:

* Output ∈ (0,1)
* Smooth and differentiable
* Ideal for probability modeling

![Image](https://upload.wikimedia.org/wikipedia/commons/8/88/Logistic-curve.svg)

![Image](https://cdn1.byjus.com/wp-content/uploads/2019/12/logistic-curve.png)

---

## 5️⃣ Hypothesis Function (Logistic Regression)

[
h_\theta(x) = g(\theta^T x) = \frac{1}{1 + e^{-\theta^T x}}
]

### Interpretation:

[
h_\theta(x) = P(y=1 \mid x; \theta)
]

Decision rule:

* If ( h_\theta(x) \ge 0.5 ) → predict **1**
* Else → predict **0**

---

## 6️⃣ Decision Boundary

A **decision boundary** separates regions where the model predicts different classes.

For logistic regression:
[
\theta^T x = 0
]

* Linear decision boundary → line / plane
* Non-linear boundary → curve (with feature mapping)

![Image](https://codefinity-content-media.s3.eu-west-1.amazonaws.com/b71ff7ac-3932-41d2-a4d8-060e24b00129/DecisionBoundary.png)

![Image](https://scipython.com/media/old_blog/logistic_regression/decision-boundary.png)

---

## 7️⃣ Cost Function for Logistic Regression

Mean Squared Error is **not suitable** for classification.

### Logistic (Cross-Entropy) Cost Function:

For a single example:
[
\text{Cost}(h_\theta(x), y) =
\begin{cases}
-\log(h_\theta(x)) & \text{if } y=1 \
-\log(1 - h_\theta(x)) & \text{if } y=0
\end{cases}
]

### Overall Cost:

[
J(\theta) = \frac{1}{m}\sum_{i=1}^{m} \text{Cost}(h_\theta(x^{(i)}), y^{(i)})
]

📌 This cost function is **convex**, ensuring a global minimum.

---

## 8️⃣ Gradient Descent for Logistic Regression

Gradient descent is used to minimize the logistic cost function.

### Update Rule:

[
\theta_j := \theta_j - \alpha \frac{1}{m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})x_j^{(i)}
]

✔ Formula looks similar to linear regression
✔ Difference lies in hypothesis function

![Image](https://global.discourse-cdn.com/dlai/original/3X/7/0/70c5465fc42124eb141aba290dfea2fa6ec2122b.jpeg)

![Image](https://i.sstatic.net/osnXh.png)

---

## 9️⃣ Interpretation of Output

* ( h_\theta(x) = 0.9 ) → 90% probability of class 1
* ( h_\theta(x) = 0.2 ) → 20% probability of class 1

Logistic regression is a **probabilistic classifier**.

---

## 🔟 Advantages of Logistic Regression

* Simple and efficient
* Probabilistic interpretation
* Works well for linearly separable data
* Foundation for advanced classifiers

---

## 1️⃣1️⃣ Limitations

* Assumes linear decision boundary
* Performs poorly on complex non-linear problems (without feature mapping)

---

## 🔑 Key Takeaways (Exam-Focused)

* Classification predicts discrete labels
* Logistic regression uses sigmoid function
* Output is a probability
* Uses cross-entropy cost function
* Decision boundary defined by ( \theta^T x = 0 )

---

## 📌 Quick Revision Box

* **Sigmoid:** ( \frac{1}{1+e^{-z}} )
* **Hypothesis:** ( h_\theta(x) = P(y=1|x) )
* **Threshold:** 0.5
* **Cost:** Log loss (cross-entropy)

---
For Numerical Example, Code and Interview question, click the below URL
https://chatgpt.com/s/t_695a263b8248819197103ede5627fe65