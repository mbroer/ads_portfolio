import pandas as pd
from functools import partial
import ads_dataframes as ads_df
#from ads_dataframes import dataframe_get_all, dataframe_get, dataframe_update
from IPython.display import display

import ads_dev as dev

clean_funcs = {}
drop_cols = {}

def cleaner_init():
	_add_cleaner_job("recipes", _rename_recipe_title_column)
	_add_cleaner_job("recipes", _drop_columns, ['stars', 'url', 'image'])

	df_names = ads_df.dataframe_get_all()

	for df_name in df_names:
		_add_cleaner_job(df_name, _reset_index)
		if df_name == 'recipes':
			continue

		_add_cleaner_job(df_name, 	_groupby)
		_add_cleaner_job(df_name, 	_reset_index)

	_add_cleaner_job("tags", _clean_list_tags)
	_add_cleaner_job("ingredients", _replace_ingredient_unit_nan)
	cleaner_init.has_been_called = True

def cleaner_exec():
	if not cleaner_init.has_been_called:
		cleaner_init()

	dataframes = ads_df.dataframe_get_all()
	for key in dataframes:
		cleanfuncs = _get_cleaner_funcs(key)
		if cleanfuncs is not None:
			dataframe = dataframes[key]
			for cleanfunc in cleanfuncs:
				df = dev.get_performance(cleanfunc, dataframe, msg=f"cleaning {key}") #dataframe will be last arg if partial is used
				if df is not None:
					dataframe = df
					ads_df.dataframe_update(key, dataframe)

def _add_cleaner_job(name, func, args=None):
	if name not in clean_funcs:
		clean_funcs[name] = []

	if args is not None:
		func = partial(func, args)

	clean_funcs[name].append(func)

def _get_cleaner_funcs(name):
	if name in clean_funcs:
		return clean_funcs[name]

######### REGION CLEAN FUNCS #########

def _clean_list_tags(df):
	#fix missing tags by inserting empty lists
	missing_index = set(ads_df.dataframe_get(ads_df.MASTER)['recipe'].values) - set(df['recipe'].values)

	for key in missing_index:
		new_row = {'recipe': key, 'tag': []}
		row_to_df = pd.DataFrame.from_dict(new_row, orient='index').T
		df = pd.concat([df, row_to_df], ignore_index=True)

	# remove dupes
	df['tag'] = df['tag'].apply( lambda x: list(set(x)) ) 	
	return df  

def _rename_recipe_title_column(df):
	df.rename(columns={'title':'recipe'}, inplace=True)

def _reset_index(df):
	df.reset_index(drop=True, inplace=True)

""" 
	nan values in ingredients_units zijn dingen zoals "eieren" of "eetlepels suiker", dus hiervoor zijn geen units beschikbaar
	vul alle nan values met "x" zodat we dit krijgen: "eetlepels suiker 2x" ipv "eetlepels suiker 2nan"   
"""
def _replace_ingredient_unit_nan(df):
	df['unit'] = df['unit'].apply(lambda x: pd.Series(x).fillna('x').to_list())

######### ENDREGION CLEAN FUNCS #########

def _drop_columns(columns, df):
	df.drop(columns, axis=1, inplace=True) 	#delete garbage data

def _groupby(df):
	rows = len(df.index)
	df = df.groupby('recipe', sort=False, as_index=False).agg(lambda x: list(x))
	print(f'Grouped {rows} rows into {len(df.index)} rows')
	return df

cleaner_init.has_been_called = False
