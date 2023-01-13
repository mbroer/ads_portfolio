import time
from functools import partial

def print_divider(str):
	print('='*5, str.upper(), '='*5)

def get_performance(func, *args, msg):
	print_divider(msg)
	timer_val = time.perf_counter()
	result = func(*args)
	func_name = func.func.__name__ if isinstance(func, partial) else func.__name__
	print(f"{func_name} took".upper(), "{:.2f}".format(time.perf_counter() - timer_val), 'seconds'.upper() )
	return result