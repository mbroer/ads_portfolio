import keyboard
import msvcrt
import time
import ads_cli

def wait_for_button_press(page_funcs=None):
	key = get_key()

	if key is not None:
		valid = _input_press_internal(key, page_funcs)

		if not valid:
			wait_for_button_press(page_funcs)

def _input_press_internal(key, page_funcs):

	if key is None:
		return

	try:
		maxrange = len(page_funcs)
		
		if key.isnumeric():
			key = int(key) -1 # display 1 = index 0 etc

			if 0 <= key < maxrange:
				ads_cli._cli_clear()
				page_funcs[key]['func'](*page_funcs[key]['args']) #exec func defined in cli_init()
				return True
			elif key == -1 and ads_cli.current_page != 'main':
				ads_cli.open_prev_page()
			else:
				print(f"{key+1} not in range, correct input: 1-{maxrange}")
		else:
			print(f"Wrong input {key}, correct input range: 1-{maxrange}")

		return False

	except AttributeError as ex:
		print(ex)


def wait_for_input(func, msg):
	_input = ''
	while True:
		_input = input(f"{msg}\n")

		if _input is None:
			continue

		if _input == '':
			print("Vul een geldige waarde in")
			continue

		if _input.isnumeric():
			_input = int(_input)

		return func(_input)

def get_key():

	while True:
		msvcrt.getwch() #prevent typing

		pressed_key = keyboard.read_key()
		keyboard.release(pressed_key)

		pressed_key_str = str(pressed_key)

		if keyboard.is_pressed(pressed_key_str):
			continue
	
		break

	return pressed_key

def press_enter_to_cont(page_name=None):
	input("Press Enter to continue")

	if page_name is not None:
		ads_cli.show_page(page_name)