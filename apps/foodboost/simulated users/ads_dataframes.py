import pandas as pd
from functools import reduce
from IPython.display import display


import glob
import os

DATAPATH = r'data/foodboost/'
FILETYPE = '.csv'
MASTER = 'recipes'
MASTERFILE = MASTER + FILETYPE

FILE_NAMES = [os.path.basename(x) for x in glob.glob(f'{DATAPATH}*.csv')]       # get all datasets in folder
if FILE_NAMES:
	FILE_NAMES.insert(0, FILE_NAMES.pop(FILE_NAMES.index(MASTERFILE)))				# move master file to index 0

dataframes = {}

def dataframe_init():
	if not FILE_NAMES:
		print("No datasets found...")
		return

	_dataframe_import(FILE_NAMES)

def _dataframe_import(file_names):
	if not isinstance(file_names, list):
		file_names = [file_names]

	for file_name in file_names:
		df = pd.read_csv(DATAPATH+file_name, index_col=0)
		dataframes[file_name.removesuffix(FILETYPE)] = df
		print(f"loaded {file_name} {len(df.index)} rows...")

	return dataframes

def dataframe_get(filename):
	return dataframes[filename]

def dataframe_get_all():
	return dataframes

def dataframe_update(filename, df):
	dataframes[filename] = df

def dataframe_get_by_id(id):
	key = dataframes['recipes'].iloc[id]['recipe']
	df = reduce(lambda left, right: pd.merge(left, right, on='recipe'), [	dataframe_row_to_frame(dataframes['recipes'], 		key), 
																			dataframe_row_to_frame(dataframes['nutritions'], 	key), 
																			dataframe_row_to_frame(dataframes['ingredients'], 	key),  
																			dataframe_row_to_frame(dataframes['tags'], 			key, ['tag',], [[],]) ])
	return df

def dataframe_row_to_frame(df, key, columns=None, columns_fillnan=None):
	if df[df['recipe'] == key].empty:
		print('INDEX DOESNT EXIST')
	
	return df[df['recipe'] == key]

def dataframe_merge_all():
	df = dataframes['recipes']

	for i in dataframes:
		if i == 'recipes':
			continue

		df = pd.merge(df, dataframes[i], on='recipe', how='outer' )

	return df

def dataframe_drop_common_rows_return(df1, df2):
	df = df1.copy()
	cond = df['recipe'].isin(df2['recipe'])
	df.drop(df[cond].index, inplace = True)
	return df