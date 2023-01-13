from IPython.display import display
import ads_dataframes as ads_df
import ads_cli as ads_cli
import ads_input2 as inpt
import ads_model as model
import ads_dev as dev
import os
import time

def print_dataframe_headers():
	dataframes = ads_df.dataframe_get_all()

	for i in dataframes:
		print(i)
		print(dataframes[i].head(), "\n")

	inpt.press_enter_to_cont("Dataframes")

def print_dataframe_colums():
	dataframes = ads_df.dataframe_get_all()

	for i in dataframes:
		_str = f"{i}: "
		for col in dataframes[i].columns:
			_str += col + ', '
		print( _str.rstrip(', ') )

	inpt.press_enter_to_cont("Dataframes")

def show_recipe_list():
	dataframes = ads_df.dataframe_get_all()

	if not dataframes:
		print("No dataframes loaded")

	for i in dataframes:
		display(dataframes[i])

def search_recipe_list(_input):
	df = ads_df.dataframe_get('recipes')

	if df.empty:
		print("Geen recepten geladen..")
		inpt.press_enter_to_cont("Recept submenu")
		return

	df = df[df['recipe'].str.contains(_input, case=False)][['recipe']]

	if df.empty:
		print("Geen resultaten")
		inpt.press_enter_to_cont("Recept submenu")
		return

	display(df)

	id = ""
	while not id.isnumeric():
		id = inpt.wait_for_input(enter_recipe_id, "Vul recept id in")

def enter_recipe_id(id):
	df = ads_df.dataframe_get_by_id(int(id))
	display(df)
	inpt.press_enter_to_cont("Recept submenu")


def create_sim_users(amount_users):
	if not isinstance(amount_users, int):
		print(f"Ongeldige waarde: {amount_users}")
		return

	threshold = -1
	while threshold == -1:
		threshold = inpt.wait_for_input(parse_threshold_value, "Threshold voor favorieten (0.0 - 1.0):")

	dev.get_performance(_create_sim_users_internal, amount_users, threshold, msg="user favorite simulation")
	
	print("done'd")
	inpt.press_enter_to_cont("Model training")

def parse_threshold_value(threshold):
	try:
		threshold = float(threshold)
	except ValueError:
		return -1

	if 0 <= int(threshold) <= 1:
		return threshold

	print("Verkeerde input")
	return -1

def _create_sim_users_internal(amount_users, favorite_threshold):
	model.clear_users()

	for i in range(amount_users):
		model.generate_sim_user(favorite_threshold) #could try processpool/threading

def train_model():
	model.train_model()
	inpt.press_enter_to_cont("Model training")

def import_model(id):
	print("import", id)
	print("not implemented yet")
	inpt.press_enter_to_cont("Model training")


def export_loaded_model():
	timestamp = time.strftime("%Y%m%d-%H%M%S")

	print(f'exporting data from {len(model.users)} users')

	for user in model.users:
		_dir = f'usergen_export/{timestamp}'
		filepath = f'{_dir}/{user.name}.csv'

		os.makedirs(_dir, exist_ok=True) 
		user.dataframe.to_csv(filepath)  
		print(f"Exported to {filepath}")

	print("done'd")
	inpt.press_enter_to_cont("Model training")