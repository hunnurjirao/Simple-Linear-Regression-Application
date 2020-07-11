import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


w = int(input("Enter weight in Kgs: "))
p = int(input("Enter price for the given weight: "))

weights = []
price = []

w = w * 10 ** 10

while w > 0:
  w = w // 1.1
  wp = (p * w)

  weights.append(w)
  price.append(wp)

X = np.array(weights)
y = np.array(price)
X = X.reshape(X.shape[0],1)
Y = Y.reshape(Y.shape[0],1)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33,random_state=3)
model = LinearRegression()
model.fit(X_train,y_train)

pred = float(input('Enter the weight to know the price: '))
a = np.array([[pred]])
print("Amoutn to be paid: " + str(np.round(model.predict(a))))
