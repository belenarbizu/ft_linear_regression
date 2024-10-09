import pandas as pd
def tmp0(learningRate, mileage, price):
    return (learningRate * estimatePrice(mileage - price))

def tmp1(learningRate, mileage, price):
    return (learningRate * estimatePrice(mileage - price) * mileage)

def main():
    dataset = pd.read_csv("data.csv")
    print(dataset.describe())

if __name__ == "__main__":
    main()