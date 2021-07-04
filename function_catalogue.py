import pandas as pd
import numpy as np
import seaborn as sns


######### Setting up the Copy Dataframe ##########
def strip_strings_in_whole_dataset(df):
    for column in df.columns:
        try:
            df[column] = df[column].str.strip()
        except:
            continue

def strings_to_lower_in_whole_dataset(df):
    for column in df.columns:
        try:
            df[column] = df[column].str.lower()
        except:
            continue

######### Dropping Columns in Copy Dataframe ##########

def drop_duplicate_columns(df):
    df.drop(columns=['tree_id',
                     'block_id',
                     'spc_common',
                     'problems',
                     'zip_city',
                     'borocode',
                     'community board',
                     'cncldist',
                     'st_assem',
                     'st_senate',
                     'nta',
                     'boro_ct',
                     'state',
                     'x_sp',
                     'y_sp',
                     'council district',
                     'census tract',
                     'bin',
                     'bbl',
                     'address'],
                     inplace=True)

######### Convert DTypes Copy Dataframe ##########

def converting_date(df):
    df['created_at'] = df['created_at'].astype('datetime64[ns]')

def converting_stewards(df):
    df.loc[df.steward == "None", 'steward'] = 0
    df.loc[df.steward == "1or2", 'steward'] = 1
    df.loc[df.steward == "3or4", 'steward'] = 1
    df.loc[df.steward == "4orMore", 'steward'] = 1
    df['steward'] = df['steward'].astype('bool')


def merge_tree_diam_stump_diam(df):
    alive = (df.status == 'Alive')
    column_name = 'stump_diam'
    df.loc[alive, column_name] = 'None'

    dead = (df.status == 'Dead')## Converting Dtypes of Columns - deleting and changing names of columns ##
    column_name = 'stump_diam'
    df.loc[dead, column_name] = 'None'

def check_for_binary_columns(df):
    for column in df.columns:
        if (len(df[column].unique())) == 2:
            print('COLUMN', column)
            print('How many unique values : ', len(df[column].unique()))
            print(df[column].value_counts())

def convert_binary_string_columns_to_int(df):
    for column in df.columns:
        if df[column].dtype == object:
            if len(df[column].unique()) in [2, 3]:
                if 'nodamage' in df[column].unique():
                    df[column] = df[column].replace('nodamage', 0)
                    df[column] = df[column].replace('damage', 1)

 # curb_loc
                    df[column] = df[column].replace('oncurb', 1)
                    df[column] = df[column].replace('offsetfromcurb', 0)

    take_measures_for_nan_in_sidewalk(df)


def take_measures_for_nan_in_sidewalk(df):
    df['sidewalk'].fillna(-1, inplace=True)
    df['sidewalk'] = df.sidewalk.astype(int)


def convert_binary_string_columns_to_bool(df):
    for column in df.columns:
        if df[column].dtype == object:
            if len(df[column].unique()) in [2, 3]: # take into account nan as a third unique value problem columns
                df[column] = df[column].replace('yes', True)
                df[column] = df[column].replace('no', False)


def convert_steward_to_string_of_numbers(df):
    # still a string, a bit easier to extract
    df.steward = df.steward.replace('none', '0')
    df.steward = df.steward.replace('1or2', '1, 2')
    df.steward = df.steward.replace('3or4', '>=3') # overlapping
    df.steward = df.steward.replace('4ormore', '>=3') # overlapping


def fill_nan_health_alive_tree(df):
    condition_one = (df.status == 'alive')
    condition_two = (df.health.isnull())
    index_to_change = df[condition_one & condition_two].index
    df.loc[index_to_change, 'health'] = 'unknown'

######### Original Dataframe information ##########

def original_dataframe_info(df):
    print(df.info())
    print(df)
    print(df.head())
    print(df.describe())
    print(df.dtypes)


def check_for_duplicates(df):
    print('Check Original Dataframe for Duplicates\n'
          '####################################')
    print(df.duplicated().value_counts())


def value_counts_original_dataframe(df):
    print('Value counts for columns in Original Dataframe\n'
        '##########################')
    for column in df.columns:
        print('COLUMN', column)
        print('how many unique values:', len(df[column].unique()))
        print(df[column].value_counts())

def print_check_nulls(df):
    print('Total missing data:', end=' ')
    print(df.isnull().sum().sum())
    print('Missing values per column:')
    print(df.isnull().sum())


def print_check_unique_values(df):
    for column in df.columns:
        print('UNIQUE VALUES IN:', column)
        print(df[column].unique())
