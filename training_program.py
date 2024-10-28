import pandas as pd
import numpy as np
from predict_price import predict_price

def feature_scaling(mileage):
    mean = np.mean(mileage)
    stnd_dev = np.std(mileage)
    mileage_scaled = []
    for km in mileage:
        mileage_scaled.append(float((km - mean) / stnd_dev))
    return mileage_scaled, mean, stnd_dev

def update_cost(mileage, price, theta0, theta1):
    error = 0
    for km, price_value in zip(mileage, price):
        predicted = predict_price(theta0, theta1, km)
        error += (predicted - price_value) ** 2
    return (error / (len(mileage) * 2))

def update_theta(mileage, price, mean, stnd_dev, learning_rate=0.01):
    theta0 = 0
    theta1 = 0
    for x in range(1000):
        cost = update_cost(mileage, price, theta0, theta1)
        grad0 = 0
        grad1 = 0
        for km, price_value in zip(mileage, price):
            predicted = predict_price(theta0, theta1, km)
            grad0 += (predicted - price_value)
            grad1 += (predicted - price_value) * km
        theta0 -= learning_rate * (grad0 / len(mileage))
        theta1 -= learning_rate * (grad1 / len(mileage))
    theta0 = theta0 - (theta1 * mean / stnd_dev)
    theta1 = theta1 / stnd_dev
    return theta0, theta1

def data_file(theta0, theta1):
    file = open("data", "w")
    file.write(f"{theta0},{theta1}")
    file.close()

def main():
    dataset = pd.read_csv("data.csv")
    data_dict = dataset.to_dict(orient='list')
    mileage_scaled, mean, stnd_dev = feature_scaling(data_dict['km'])
    theta0, theta1 = update_theta(mileage_scaled, data_dict['price'], mean, stnd_dev)
    data_file(theta0, theta1)

if __name__ == "__main__":
    main()