import pandas as pd
import numpy as np
import math

def remove_rows_with_missing_data(df,column_names):
    df.dropna(subset=column_names,inplace=True)
    return df

def combine_strings(df,column_name):
    df[column_name] = ' '.join(eval(df[column_name][0]))
    return df

def fill_empty_values(df,column_names):
    for column in column_names:
        df[column] = df[column].apply(lambda x: 1 if (math.isnan(x) == True) else x)
    return df

def prepare_data(df):
    rating_columns = ['Cleanliness_rate','Accuracy_rate','Communication_rate','Location_rate','Check-in_rate','Value_rate']
    df = remove_rows_with_missing_data(df,rating_columns)

    df = combine_strings(df,"Description")

    count_columns = ["beds","bathrooms","bedrooms","guests"]
    df = fill_empty_values(df,count_columns)

    return(df)

def load_airbnb(data,label):
    df = data.drop(label, axis = 1)
    df = df.drop(['ID','Category','Title','Description','Amenities','Location','url'],axis=1)
    return df, data[label]




if __name__ == "__main__":
    df = pd.read_csv('AirBnbData.csv')
    prepare_data(df)

    print(df.info())

    

