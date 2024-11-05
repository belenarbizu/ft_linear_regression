import pandas as pd
import numpy as np
from predict_price import predict_price
import matplotlib.pyplot as plt
import argparse


def read_file():
    """
    Try to read the dataset and return a dict oriented list of the data
    """
    try:
        dataset = pd.read_csv("data.csv")
        data_dict = dataset.to_dict(orient='list')
    except:
        print("Coludn't read the dataset")
        sys.exit(1)
    return data_dict

def feature_scaling(mileage):
    """
    Standardize the mileage data
    """
    mean = np.mean(mileage)
    stnd_dev = np.std(mileage)
    mileage_scaled = []
    for km in mileage:
        mileage_scaled.append(float((km - mean) / stnd_dev))
    return mileage_scaled, mean, stnd_dev

def update_cost(mileage, price, theta0, theta1):
    """
    Calculate the cost and returns it
    """
    error = 0
    for km, price_value in zip(mileage, price):
        predicted = predict_price(theta0, theta1, km)
        error += (predicted - price_value) ** 2
    return (error / (len(mileage) * 2))

def update_theta(mileage, price, mean, stnd_dev, learning_rate=0.01, iteractions=1000):
    """
    Calculate theta0 and theta1
    """
    theta0 = 0
    theta1 = 0
    for x in range(iteractions):
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
    """
    Try to store the data into a file
    """
    try:
        file = open("data", "w")
        file.write(f"{theta0},{theta1}")
        file.close()
    except:
        print("Couldn't store the data into the file")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Predicts the price of a car by using a linear function")
    parser.add_argument('-p', '--plot-data', action='store_true', help="Plot the data")
    parser.add_argument('-l', '--plot-line', action='store_true', help="Plot the linear regression's line")
    args = parser.parse_args()

    data_dict = read_file()
    mileage_scaled, mean, stnd_dev = feature_scaling(data_dict['km'])
    theta0, theta1 = update_theta(mileage_scaled, data_dict['price'], mean, stnd_dev)
    data_file(theta0, theta1)
    
    if args.plot_data:
        plt.scatter(data_dict['km'], data_dict['price'])
        plt.xlabel('Mileage (km)')
        plt.ylabel('Price (euros)')
        plt.show()

    if args.plot_line:
        plt.plot(data_dict['km'], data_dict['price'], 'o')
        plt.plot(data_dict['km'], [predict_price(theta0, theta1, km) for km in data_dict['km']])
        plt.xlabel('Mileage (km)')
        plt.ylabel('Price (euros)')
        plt.show()

if __name__ == "__main__":
    main()