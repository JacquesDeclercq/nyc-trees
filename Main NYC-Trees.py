from function_catalogue import *

file = '2015_Street_Tree_Census_-_Tree_Data.csv'
df_original = pd.read_csv(file, sep =",")
df_copy = df_original.copy()

strip_strings_in_whole_dataset(df_copy)
strings_to_lower_in_whole_dataset(df_copy)

    # column manipulation
drop_duplicate_columns(df_copy)
merge_tree_diam_stump_diam(df_copy)

    # dtypes conversion
converting_date(df_copy)
convert_binary_string_columns_to_int(df_copy)
convert_binary_string_columns_to_bool(df_copy)
convert_steward_to_string_of_numbers(df_copy)

    # fix nan for column health for one alive tree
fill_nan_health_alive_tree(df_copy)


#def create_csv_file():
df_copy.to_csv('NYC_trees_XL', sep=',', encoding='utf-8')


print(df_copy.info())
