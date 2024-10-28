import sys

def predict_price(theta0, theta1, mileage):
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

def read_file():
    file = open("data", "r")
    s = file.read()
    data = s.split(",")
    return float(data[0]), float(data[1])

def main():
    print("Enter a mileage:")
    mileage = input()
    num = check_input(mileage)
    theta0, theta1 = read_file()
    estimate_price = predict_price(theta0, theta1, num)
    print("The estimate price is", estimate_price)

if __name__ == "__main__":
    main()