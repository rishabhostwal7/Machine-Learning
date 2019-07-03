import pandas as pd
import matplotlib.pyplot as plt

from sklearn import linear_model        # sklearn stands for "Scientific kit for machine learning

import warnings
warnings.filterwarnings(action="ignore")

# Function to get data
def get_data(file_name):
    dataframe = pd.read_csv(file_name)
    print(dataframe)
    x_parameters = []
    y_parameters = []
    for single_square_feet, single_price_value in zip(
        dataframe['square_feet'], dataframe['price'] ):

        x_parameters.append( [float(single_square_feet)] )
        y_parameters.append( float(single_price_value) )
    return x_parameters, y_parameters

# Function for fitting data to Linear Model
def linear_model_main(X_parameters, Y_parameters, quest_value):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    print("Area : ", X_parameters)
    print("Price : ", Y_parameters)
    regr.fit(X_parameters, Y_parameters)        # this is used to to train the machine learning algorithm ( best fir training or to find m and c)
    predicted_ans = regr.predict([ [quest_value] ])     # this is used to train the algorithm and to used the trained algorithm
    predictions = {}
    predictions['coefficient'] = regr.coef_     # m or slope        m =coef_
    predictions['intercept'] = regr.intercept_      # c=intercept_
    predictions['predicted_ans'] = predicted_ans

    print("Output from Machine = ", predicted_ans)

    plt.scatter(X_parameters, Y_parameters, color="m", marker="o", s=30)

    all_predicted_Y = regr.predict(X_parameters)
    plt.scatter(X_parameters, all_predicted_Y, color="b")
    plt.plot(X_parameters, all_predicted_Y, color="r")
    plt.scatter(quest_value, predicted_ans, color="g")
    plt.show()
    return predictions

# predicting house price for house of 700 square feet area
if __name__ == "__main__":
    x, y = get_data("LR_House_price.csv")
    question_value = 700    # this is the question
    result = linear_model_main(x,y,question_value)
    print("Intercept value : ", result['intercept'])
    print("Coefficient : ", result['coefficient'])
    print("Predicted house price value : ", result['predicted_ans'])

