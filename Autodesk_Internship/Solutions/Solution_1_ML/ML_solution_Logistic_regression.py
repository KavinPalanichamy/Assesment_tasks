import numpy as np
import pandas as pd


# Load the dataset, which was collected during the previous sales [Age,Salary,Outcome]

dataset = pd.read_csv('Customers.csv')

# Split the dataset into training and test sets 

def train_test_split(X, y, test_size=0.2, random_state=0):
    np.random.seed(random_state)
    shuffled_indices = np.random.permutation(len(y))
    test_set_size = int(len(y) * test_size)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)


# Standardize the input features; This sets the mean of the data to 0 and standard deviation to 1. It ensures that every set of data contributes equally to the model
def standardize(X_train, X_test):
    mean = np.mean(X_train, axis=0)
    std = np.std(X_train, axis=0)
    X_train = (X_train - mean) / std
    X_test = (X_test - mean) / std
    X_train = np.concatenate((np.ones((len(X_train), 1)), X_train), axis=1)
    X_test = np.concatenate((np.ones((len(X_test), 1)), X_test), axis=1)
    return X_train, X_test



X_train, X_test = standardize(X_train, X_test)

# Define the sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

#To standardize single input variables, the data from the excel sheet is used.
# As in the final equation, salary contibutes significantly more than age; The final sum is standardized rather than individual standardization.
def standardize_single_input_return_sigmoid(z,x_mean=70000,x_std=34000):
        x_scaled = (z - x_mean) / x_std
        return sigmoid(x_scaled)

# Define the cost function
def cost_function(X, y, theta):
    m = len(y)
    h = sigmoid(np.dot(X, theta))
    J = (-1/m) * np.sum(y*np.log(h) + (1-y)*np.log(1-h))
    return J

# Define the gradient descent function
def gradient_descent(X, y, theta, alpha, num_iters):
    m = len(y)
    J_history = np.zeros(num_iters)
    
    for i in range(num_iters):
        h = sigmoid(np.dot(X, theta))
        theta = theta - (alpha/m) * np.dot(X.T, (h - y))
        J_history[i] = cost_function(X, y, theta)
    
    return theta, J_history

# Initialize the parameters of the model
theta = np.zeros((X_train.shape[1], 1))

# Train the model using the training data
alpha = 0.001
num_iters = 100000
theta, J_history = gradient_descent(X_train, y_train.reshape(-1, 1), theta, alpha, num_iters)

# Test the model using the test data and calculate its accuracy
y_pred = sigmoid(np.dot(X_test, theta))
y_pred = [1 if i >= 0.5 else 0 for i in y_pred]
accuracy = np.mean(y_pred == y_test)

# Output Delivery
print("------------------- Regressive, Pre-collected data based marketing target predictor ------------------------------","\n\n\n")
print("***************** Learning model stats ******************","\n\n")
print('Accuracy of the model used to predict the possibility of the outcome  (0 to 1 Scale) : ', accuracy,"\n")
print("Weight of the age   :  ", theta[1],"\n")
print("Weight of the Salary   :  ", theta[2],"\n\n")
print("*********************************************************","\n\n")
print("*-*-*-*-*--*-*-* Details of the prospective customer -*-*-*-*-*--*-*-*-*-*-","\n")
age_ask = int(input("Enter the age of the person    -->   "))
salary_ask = int(input("Enter the salary of the person  -->  "))

# The bias term, weight of age and weight of salary has been applied in the equation to get the prediction
asked_prediction = theta[0]+theta[1]*age_ask+theta[2]*salary_ask
# The prediction is fed to the standardizer and the function returns the prediction between 0 and 1 using sigmoid  
sig_asked_prediction = standardize_single_input_return_sigmoid(asked_prediction)
# Rounding off the probability to get a binary output
result=(1 if sig_asked_prediction >= 0.5 else 0) 
print("\n\n( 1 - Customer buys the product, 0 - The customer wont buy the product )")
print("\n\nThe binary response is   --  ", result, "   -- \n")
print("The customer is ", sig_asked_prediction*100," % "," likely to be a potential buyer")
