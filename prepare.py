import pandas as pd
import numpy as np
import sklearn.preprocessing

def get_run_length(df):
    '''
    This function takes in the broadway dataframe with columns
    for show opening date and show closing date
    and converts those to the correct format to 
    calculate the run of show in days
    '''
    #Convert Closing Date to Datetime dtype
    df['Closing Date'] = pd.to_datetime(df['Closing Date'], format='%Y-%m-%d')

    #Convert Opening Date to Datetime dtype by first coercing error
    pd.to_datetime(['Opening Date'], errors='coerce')
    df['Opening Date'] = pd.to_datetime(df['Opening Date'], format='%Y-%m-%d')

    #Calculate the length of run in days...return dtype in datetime format that needs further conversion
    df['length_of_run'] = df['Closing Date'] - df['Opening Date']

    #Convert length of run to str dtype
    df['length_of_run'] = df.length_of_run.astype('str')

    #Strip 'days' from column observations in length of run and return column dtype as int
    df['length_of_run'] = df['length_of_run'].str.replace(r'\D', '').astype(int)

    return df

def get_object_cols(df):
    '''
    This function takes in a dataframe and identifies the columns that are object types
    and returns a list of those column names. 
    '''
    # create a mask of columns whether they are object type or not
    mask = np.array(df.dtypes == "object")

        
    # get a list of the column names that are objects (from the mask)
    object_cols = df.iloc[:, mask].columns.tolist()
    
    return object_cols

def create_dummies(df, object_cols):
    '''
    This function takes in a dataframe and list of object column names,
    and creates dummy variables of each of those columns. 
    It then appends the dummy variables to the original dataframe. 
    It returns the original df with the appended dummy variables. 
    '''

    # run pd.get_dummies() to create dummy vars for the object columns. 
    # we will drop the column representing the first unique value of each variable
    # we will opt to not create na columns for each variable with missing values 
    # (all missing values have been removed.)
    dummy_df = pd.get_dummies(df[object_cols], dummy_na=False, drop_first=False)
    
    # concatenate the dataframe with dummies to our original dataframe
    # via column (axis=1)
    df = pd.concat([df, dummy_df], axis=1)

    return df


def prep_bway(df):
    '''
    This function takes in the broadway dataframe
    and prepares it for analysis by:
    

    '''
    #reset the index to show_id
    df = df.set_index('show_id')

    #Drop observations with a show type == Benefit knowing these are single day events by nature
    index_names = df[df['Show Type'] == 'Benefit'].index
    df.drop(index_names, inplace=True)

    #Drop Observations where the Theatre is Not in NY
    index_locality = df[df['Theatre Address Locality'] != 'New York'].index
    df.drop(index_locality, inplace = True)

    #Drop coulumns with too many nulls or that are not necessary
    df.drop(columns={'Previews Date', 'Intermissions', 'N Performances', 
    'Run Time', 'Other Titles', 'Official Website', 'Theatre Postal Code',
    'Theatre Year Closed', 'Theatre Year Demolished', 'Theatre Address Locality',
    'Theatre Full Address', 'Theatre Street Address', 'Theatre Address Region', 'Theatre Name', 
    'Show Title'}, inplace=True)


    #drop any observations with remaining nulls
    df.dropna(inplace=True)

    #Use get_run_length function to calculate run length
    df = get_run_length(df)

    #Get dummies for object columns
    df = create_dummies(df, get_object_cols(df))

    return df