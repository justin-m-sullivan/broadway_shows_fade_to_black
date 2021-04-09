import pandas as pd
import numpy as np

def get_broadway_data():
    '''
    This function reads in broadway data
    gathered from openbroadwaydata.com
    that was saved locally as a .csv file
    '''
    return pd.read_csv('open-broadway-data 2021-04-08.csv')