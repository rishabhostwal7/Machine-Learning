import pandas as pd
from sklearn import linear_model

# function to get data
def get_data(file_name):
    data = pd.read_csv(file_name)
    flash_x_parameter = []
    flash_y_parameter = []
    got_x_parameter = []
    got_y_parameter = []
    for x1, y1, x2, y2 in zip(data['Flash_episode_number'],
                           data['Flash_us_viewers'],
                           data['GoT_episode_number'],
                           data['GoT_us_viewers'] ):

        flash_x_parameter.append( [float(x1)] )
        flash_y_parameter.append( float(y1) )
        got_x_parameter.append( [float(x2)] )
        got_y_parameter.append( float(y2) )
    return flash_x_parameter, flash_y_parameter, got_x_parameter, got_y_parameter

# function to know which tv series will have more viewers
def find_more_viewers(x1, y1, x2, y2):
    regr1 = linear_model.LinearRegression()     # Used to calculate best fit hypothesis parameter
    regr1.fit(x1, y1)    # train the machine    and m and c is calculated
    predicted_value1 = regr1.predict( [ [10] ] )
    print("Prediction of Flash = ", predicted_value1)
    regr2 = linear_model.LinearRegression()
    regr2.fit(x2, y2)
    predicted_value2 = regr2.predict( [ [10] ] )
    print("Prediction of GOT = ", predicted_value2)


    if(predicted_value1 > predicted_value2):
        print("Next Episode of Flash TV Show will have more viewers for next week")
    else:
        print("Next Episode of GOT TV Show will have more viewers for next week")


if __name__ == '__main__':
    x1,y1,x2,y2 = get_data('LR_Episodes.csv')
    # CAll the function more viewers to predict te more viewers
    find_more_viewers(x1, y1, x2, y2)

