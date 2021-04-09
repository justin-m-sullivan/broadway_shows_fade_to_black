import pandas as pd
import numpy as np
import sklearn.preprocessing
from sklearn.model_selection import train_test_split

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

    df.drop(columns={'Show Type', 'Production Type' }, inplace = True)

    return df

def get_revival_dummies(df):
    '''
    This function takes in the broadway dataframe
    and creates a dummy column called is is_revival
    from the Revival column and then drops the Revival column.
    '''
    #Create the dummy dataframe
    dummy_df = pd.get_dummies(df['Revival'], drop_first=True)

    #Concat back to the original dataframe
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

    #Drop Observations where Show Never Opened
    index_opened = df[df['Show Not Opened'] == True].index
    df.drop(index_opened, inplace = True)

    #Drop coulumns with too many nulls or that are not necessary
    df.drop(columns={'Previews Date', 'Intermissions', 'N Performances', 
    'Run Time', 'Other Titles', 'Official Website', 'Theatre Postal Code',
    'Theatre Year Closed', 'Theatre Year Demolished', 'Theatre Address Locality',
    'Theatre Full Address', 'Theatre Street Address', 'Theatre Address Region', 'Theatre Name', 
    'Show Title', 'Show Not Opened', 'Show Type (Simple)'}, inplace=True)

    #drop any observations with remaining nulls
    df.dropna(inplace=True)

    #Use get_run_length function to calculate run length
    get_run_length(df)

    #Create Dummie for if the show is a revival or not
    df = get_revival_dummies(df)

    #rename the is_revival column
    df.rename(columns={True: 'is_revival'}, inplace=True)

    df.drop(columns={'Revival'}, inplace=True)

    #Get dummies for object columns
    df = create_dummies(df, get_object_cols(df))

    #drop opening and closing date columns
    df.drop(columns={'Opening Date', 'Closing Date'}, inplace=True)

    return df

def split(df, target_var):
    '''
    This function takes in the dataframe and target variable name as arguments and then
    splits the dataframe into train (56%), validate (24%), & test (20%)
    It will return a list containing the following dataframes: train (for exploration), 
    X_train, X_validate, X_test, y_train, y_validate, y_test
    '''
    # split df into train_validate (80%) and test (20%)
    train_validate, test = train_test_split(df, test_size=.20, random_state=13)
    # split train_validate into train(70% of 80% = 56%) and validate (30% of 80% = 24%)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=13)

    # create X_train by dropping the target variable 
    X_train = train.drop(columns=[target_var])
    # create y_train by keeping only the target variable.
    y_train = train[[target_var]]

    # create X_validate by dropping the target variable 
    X_validate = validate.drop(columns=[target_var])
    # create y_validate by keeping only the target variable.
    y_validate = validate[[target_var]]

    # create X_test by dropping the target variable 
    X_test = test.drop(columns=[target_var])
    # create y_test by keeping only the target variable.
    y_test = test[[target_var]]

    partitions = [train, X_train, X_validate, X_test, y_train, y_validate, y_test]
    return partitions