import os
import ads_cli_functions as clifn
import ads_input2 as inpt

_menu = {}
_submenu_history = []
current_page = None

def cli_init():
	_add_menu_submenu("main", "Dataframes")
	_add_menu_option("Dataframes", "Print columns", clifn.print_dataframe_colums)
	_add_menu_option("Dataframes", "Print headers", clifn.print_dataframe_headers)

	_add_menu_submenu("main", "Recept submenu")
	_add_menu_input_option("Recept submenu", "Zoek recept", clifn.search_recipe_list, "Type recept naam:" )

	_add_menu_submenu("main", "Model training")
	_add_menu_input_option("Model training", "Import existing user data", clifn.import_model, "Data ID to load:" )
	_add_menu_input_option("Model training", "Sim users", clifn.create_sim_users, "Aantal gebruikers:" )
	_add_menu_option("Model training", "Export sim user data", clifn.export_loaded_model)


	_add_menu_option("Model training", "Train model", clifn.train_model )

def cli_start():
	first_page = list(_menu.keys())[0]
	show_page( first_page )

def _add_menu_option(menu_name, display, func, *args):
	if menu_name not in _menu:
		_menu[menu_name] = []

	page_struct = {'display': display, 'func': func, 'args': args}

	_menu[menu_name].append(page_struct)

def _add_menu_submenu(menu_name, display):
	_add_menu_option(menu_name, display, show_page, display)


def _add_menu_input_option(menu_name, display, func, msg):
	_add_menu_option(menu_name, display, inpt.wait_for_input, func, msg)

def show_page(page):
	if page not in _menu:
		print(f"page '{page}' does not exist")
		return
	if not _menu[page]:
		print(f"page '{page}' does not have options")
		return

	global current_page
	current_page = page

	_cli_clear()

	for i in range(1, len(_menu[page])+1):
		print(f"{i}).",_menu[page][i-1]['display'])

	if page != 'main':
		print("0). Vorige menu")

	_submenu_history.append(page)

	inpt.wait_for_button_press(_menu[page])

def _cli_clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def open_prev_page():
	if not _submenu_history:
		return

	_submenu_history.pop() #pop current page

	show_page(_submenu_history.pop()) #pop prev page and open

def _blank(arg1=None, arg2=None):
	print("blank",arg1, arg2)
	return True

cli_init()
#cli_start()