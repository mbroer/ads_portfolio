from ads_dataframes import dataframe_init, dataframe_get_all
from ads_cleaner import cleaner_exec
from ads_cli import cli_start
import ads_dev as dev
from ads_input2 import press_enter_to_cont

if __name__ == "__main__":
	dev.get_performance(dataframe_init, msg="dataframe init")
	dev.get_performance(cleaner_exec, msg="dataframe cleanup")
	press_enter_to_cont()
	cli_start()