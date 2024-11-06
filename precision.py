from training_program import LinearRegression
from predict_price import predict_price

def mse(model):
    """
    Calculates the mean squared error of the model
    """
    mse_value = (sum((price - predict_price(model.theta0, model.theta1, km)) for km, price in zip(model.mileage , model.price)) ** 2) / len(model.mileage)
    print(f"Mean Squared Error: {mse_value:.2f}")
    return mse_value

def rmse(mse_value):
    """
    Calculates the root mean squared error of the model
    """
    rmse_value = mse_value ** 0.5
    print(f"Root Mean Squared Error: {rmse_value:.2f}")

def mean_abs_error(model):
    """
    Calculates the mean absolute error of the model
    """
    mae = sum(abs(price - predict_price(model.theta0, model.theta1, km)) for km, price in zip(model.mileage , model.price)) / len(model.mileage)
    print(f"Mean Absolute Error: {mae:.2f}")

def r2_score(model):
    """
    Calculates the r2 score of the model
    """
    price_mean = sum(model.price) / len(model.price)
    rss = sum((price - predict_price(model.theta0, model.theta1, km)) ** 2 for km, price in zip(model.mileage , model.price))
    tss = sum((price - price_mean) ** 2 for price in model.price)
    r2 = 1 - (rss / tss)
    print(f"R2 score: {r2:.2f}")

def main():
    model = LinearRegression()
    model.feature_scaling()
    model.update_theta()
    
    mse_value = mse(model)
    rmse(mse_value)
    mean_abs_error(model)
    r2_score(model)

if __name__ == "__main__":
    main()