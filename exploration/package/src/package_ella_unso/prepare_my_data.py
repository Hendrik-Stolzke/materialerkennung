import pandas as pd    
from pandas import DataFrame            
import glob

def prepare_data():

    # Step 1: list all csv files only
    csv_files = glob.glob('*.{}'.format('csv'))
    csv_files = csv_files[0:-1]

    # Step 2: choose the 'material' column in 'measurements.csv' 
    measure = pd.read_csv('measurements.csv')
    df_measure_target = DataFrame(measure).material.tolist()

    # Step 3: concatenate each target value with every csv-data + add an id
    l = [] 
    i = 0
    for file in csv_files:
        data = pd.read_csv(file)
        df = DataFrame(data)
        df['id'] = i
        l.append(df)
        i += 1

    # Step 4: convert to a DataFrame 
    # muss noch vektorisiert werden aber stehe grad auf dem Schlauch...
    df_full = DataFrame(columns=['Audio', 'Voltage', 'Current','id'])
    for elem in l:
        df_full = pd.concat([df_full, elem], ignore_index=True)

    # Step 5: convert to Series
    measure_Series = pd.Series(df_measure_target)

    return df_full, measure_Series         # df_full: Dataframe of drill data; measure_Series: Series of the target column

# Check
# prepare_data()