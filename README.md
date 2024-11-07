# ft_linear_regression
In this project, I implemented a simple linear regression model with a single feature: car mileage. There are three programs:<br/>
<br/>
The prediction program: This program allows the user to input a car's mileage and, based on the linear regression model, calculates the estimated price of the car. It uses the formula estimatePrice(mileage) = θ0 + (θ1 * mileage).<br/>
Usage: python3 ./predict_price.py<br/>
<br/>
The training program: This program reads a dataset file and performs linear regression on the data. During the training process. It saves the values of θ0 and θ1, which are then used in the prediction program. You can also visualize its distribution (-p flag) and the resulting regression line (-l flag).<br/>
Usage: python3 ./training_program.py [-l --plot-line] [-p --plot-data]<br/>
<br/>
The precision program: Calculate the model's accuracy and evaluate its performance.<br/>
Usage: python3 ./precision<br/>
<br/>
This project allowed me to work with concepts of linear regression, parameter updating through optimization algorithms like gradient descent, and also data visualization.
