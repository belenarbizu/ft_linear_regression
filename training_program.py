import pandas as pd
import numpy as np
import sys
from predict_price import predict_price
import matplotlib.pyplot as plt
import argparse

class LinearRegression:
    def __init__(self):
        self.theta0 = 0
        self.theta1 = 0
        self.learning_rate = 0.01
        self.iteractions = 1000

        self.data_dict = []
        self.mileage = []
        self.price = []
        self.mileage_scaled = []

        self.read_file()

        self.mean = sum(km for km in self.mileage) / len(self.mileage)
        self.stnd_dev = (sum((km - self.mean) ** 2 for km in self.mileage) / len(self.mileage)) ** 0.5

    def read_file(self):
        """
        Try to read the dataset and return a dict oriented list of the data
        """
        try:
            dataset = pd.read_csv("data.csv")
            self.data_dict = dataset.to_dict(orient='list')
            self.mileage = [float(key) for key in self.data_dict['km']]
            self.price = [float(key) for key in self.data_dict['price']]
        except:
            print("Coludn't read the dataset")
            sys.exit(1)

    def feature_scaling(self):
        """
        Standardize the mileage data
        """
        for km in self.mileage:
            self.mileage_scaled.append((km - self.mean) / self.stnd_dev)

    def update_cost(self):
        """
        Calculate the cost and returns it
        """
        error = 0
        for km, price_value in zip(self.mileage_scaled, self.price):
            predicted = predict_price(self.theta0, self.theta1, km)
            error += (predicted - price_value) ** 2
        return (error / (len(self.mileage_scaled) * 2))

    def update_theta(self):
        """
        Calculate theta0 and theta1
        """
        for x in range(self.iteractions):
            cost = self.update_cost()
            grad0 = 0
            grad1 = 0
            for km, price_value in zip(self.mileage_scaled, self.price):
                predicted = predict_price(self.theta0, self.theta1, km)
                grad0 += (predicted - price_value)
                grad1 += (predicted - price_value) * km
            self.theta0 -= self.learning_rate * (grad0 / len(self.mileage_scaled))
            self.theta1 -= self.learning_rate * (grad1 / len(self.mileage_scaled))
        self.theta0 = self.theta0 - (self.theta1 * self.mean / self.stnd_dev)
        self.theta1 = self.theta1 / self.stnd_dev

    def data_file(self):
        """
        Try to store the data into a file
        """
        try:
            file = open("data", "w")
            file.write(f"{self.theta0},{self.theta1}")
            file.close()
        except:
            print("Couldn't store the data into the file")
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Predicts the price of a car by using a linear function")
    parser.add_argument('-p', '--plot-data', action='store_true', help="Plot the data")
    parser.add_argument('-l', '--plot-line', action='store_true', help="Plot the linear regression's line")
    args = parser.parse_args()

    model = LinearRegression()
    model.feature_scaling()
    model.update_theta()
    model.data_file()
    
    if args.plot_data:
        plt.scatter(model.mileage, model.price)
        plt.xlabel('Mileage (km)')
        plt.ylabel('Price (euros)')
        plt.show()

    if args.plot_line:
        plt.plot(model.mileage, model.price, 'o')
        plt.plot(model.mileage, [predict_price(model.theta0, model.theta1, km) for km in model.mileage])
        plt.xlabel('Mileage (km)')
        plt.ylabel('Price (euros)')
        plt.show()

if __name__ == "__main__":
    main()