import sys

def predict_price(theta0, theta1, mileage):
    """
    Function to calculate the predicted price
    """
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
    if (num < 0):
        print("The mileage can't be negative")
        sys.exit(1)
    return num

def read_file():
    """
    Read and open the file and return the theta data
    """
    try:
        file = open("data", "r")
        s = file.read()
        data = s.split(",")
    except:
        print("Couldn't read the data file")
        sys.exit(1)
    return float(data[0]), float(data[1])

def main():
    print("Enter a mileage:")
    mileage = input()
    num = check_input(mileage)
    theta0, theta1 = read_file()
    estimate_price = predict_price(theta0, theta1, num)
    print("The estimate price is", f'{estimate_price:.2f}')

if __name__ == "__main__":
    main()