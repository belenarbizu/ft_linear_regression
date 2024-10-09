import sys

def predict_price(mileage):
    theta0 = 0
    theta1 = 0
    return (theta0 + (theta1 * mileage))

def check_input(mileage)-> int:
    """
    This function checks if the input is a number
    """
    try:
        num = int(mileage)
    except ValueError:
        print("The input is not a number")
        sys.exit(1)
    return num

def main():
    print("Enter a mileage:")
    mileage = input()
    num = check_input(mileage)
    estimate_price = predict_price(num)
    print("The estimate price is", estimate_price)

if __name__ == "__main__":
    main()