# UNQ_C4
# GRADED FUNCTION: predict

def predict(X, w, b): 
    """
    Predict whether the label is 0 or 1 using learned logistic
    regression parameters w
    
    Args:
      X : (ndarray Shape (m,n)) data, m examples by n features
      w : (ndarray Shape (n,))  values of parameters of the model      
      b : (scalar)              value of bias parameter of the model

    Returns:
      p : (ndarray (m,)) The predictions for X using a threshold at 0.5
    """
    # number of training examples
    m, n = X.shape   
    p = np.zeros(m)
   
#     ### START CODE HERE ### 
#     # Loop over each example
#     for i in range(m):   
#         z_wb = None
#         # Loop over each feature
#         for j in range(n): 
#             # Add the corresponding term to z_wb
#             z_wb += None
        
#         # Add bias term 
#         z_wb += None
        
#         # Calculate the prediction for this example
#         f_wb = sigmoid(z_wb)
    for i in range(m):
        
                 # Calculate f_wb (exactly how you did it in the compute_cost function above)
        z_wb = 0
                 # Loop over each feature
        for j in range(n): 
                     # Add the corresponding term to z_wb
            z_wb_ij = X[i, j] * w[j]
            z_wb += z_wb_ij

             # Add bias term 
        z_wb += b

             # Calculate the prediction from the model
        f_wb = sigmoid(z_wb)

        # Apply the threshold
        p[i] = f_wb >= 0.5
        
    ### END CODE HERE ### 
    return p