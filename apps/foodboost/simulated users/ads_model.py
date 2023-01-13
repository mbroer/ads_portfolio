import ads_dev as dev
import pandas as pd
import numpy as np
import names
import time
import pycountry
import random
from ads_dataframes import dataframe_merge_all
from IPython.display import display
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
from ads_dataframes import dataframe_drop_common_rows_return

pd.set_option('display.max_columns', 4)
pd.set_option('display.min_rows', 100)
pd.set_option('display.width', 2000)

dataframe_merged = None
dataframe_merged_short = None
dataframe_merged_short_unique_tags = None
dataframe_merged_short_unique_ingredients = None

users = []

def init():
	if init.has_been_called:
		return

	global dataframe_merged
	global dataframe_merged_short
	global dataframe_merged_short_unique_tags
	global dataframe_merged_short_unique_ingredients

	dataframe_merged = dev.get_performance(dataframe_merge_all, msg="dataframe merge")

	cols_to_remove =  ['persons', 'time', 'calories' ,'nutrition', 'value', 'unit', 'quantity']

	dataframe_merged = dataframe_merged.loc[:, ~dataframe_merged.columns.isin(cols_to_remove)]

	dataframe_merged_short = dataframe_merged# dataframe_merged.sample(n=100)

	dataframe_merged_short = dataframe_merged_short.loc[:, ~dataframe_merged_short.columns.isin(cols_to_remove)]
	dataframe_merged_short_unique_tags  = dataframe_merged_short["tag"].explode().unique().tolist()
	dataframe_merged_short_unique_ingredients = dataframe_merged_short["ingredient"].explode().unique().tolist()

	init.has_been_called = True

init.has_been_called = False

def generate_sim_user(favorite_threshold):
	if not init.has_been_called:
		print("Dataframe not merged yet, merging now..")
		init()

	user = SimUser( favorite_threshold )

	return user

class SimUser():
	def __init__(self, favorite_threshold):
		self.name = create_sim_user_name()
		self.age = random.randint(16, 80)
		self.nationality = random.choice(list(pycountry.countries)).name

		self.favorite_threshold = favorite_threshold

		self.favorite_base_recepes = self.select_random_recipes(10)
		self.favorite_tags 		   = [i[0] for i in get_most_common_in_list(self.favorite_base_recepes["tag"])[0:3]]
		self.favorite_ingredients  = [i[0] for i in get_most_common_in_list(self.favorite_base_recepes["ingredient"])[0:3]]
		
		self.dataframe = simulate_favorite_list(self)

		nat = self.nationality
		nat = (nat[:15] + '...' if len(nat) > 15 else nat)
		name = (self.name[:12] + '...' if len(self.name) > 12 else self.name)

		print('{0:<15} {1:<2} {2:<18} {3:>13} {4:>20}'.format(name, self.age, nat, "simmed with:", f"{(self.dataframe['favorite'] == 1).sum()}/{len(dataframe_merged_short.index)} favorites"))
		#print('{0:<50} {1:>50}'.format(f"tags: {self.favorite_tags}", f"ingr: {self.favorite_ingredients}"))

		users.append(self)
	def select_random_recipes(self, amount):
		return dataframe_merged_short.sample(n=amount)

	#def blacklist_tags(self):
	#	self.blacklist_tags_list = random.sample( set(dataframe_merged_short_unique_tags) - set(self.favorite_tags_list) , 3) # so favorites cant be blacklisted

def create_sim_user_name():
	list_names = []

	for user in users:
		list_names.append(user.name)

	name = names.get_first_name()

	while name in list_names:
		name = names.get_first_name()

	return name

def simulate_favorite_list(user):
	dataframe = dataframe_merged_short.copy()

	non_favorited_recepes = dataframe_drop_common_rows_return(dataframe, user.favorite_base_recepes) #remove favorite recipes from dataframe
	user.favorite_base_recepes['tag_score']  = 1 # set default value
	user.favorite_base_recepes['ingr_score'] = 1 # set default value
	user.favorite_base_recepes['mean_score'] = 1 # set default value
	user.favorite_base_recepes['favorite']   = 1 # set default value

	tag_values = []
	ingr_values = []
	mean_scores = []
	favorite_values = []

	for i in range(len(non_favorited_recepes.index)):
		row = non_favorited_recepes.iloc[i]

		scores = [
			calculate_simularity(row['tag'], 		user.favorite_tags),
			calculate_simularity(row['ingredient'], user.favorite_ingredients)
		]

		mean_score = np.mean(scores)
		favorite_values.append(1 if mean_score >= user.favorite_threshold else 0)

		tag_values.append(scores[0])
		ingr_values.append(scores[1])
		mean_scores.append(mean_score)


	non_favorited_recepes['tag_score']  = tag_values
	non_favorited_recepes['ingr_score'] = ingr_values
	non_favorited_recepes['mean_score'] = mean_scores
	non_favorited_recepes['favorite']   = favorite_values

	return pd.concat([user.favorite_base_recepes, non_favorited_recepes], ignore_index=True) # merge favorite base and non favorite to get filled df with populated favorite column

def get_most_common_in_list(_list):
	return  Counter( _list.explode().tolist() ).most_common()

def calculate_simularity(list1, list2):
	#convert to counters
	list1_vals = Counter(list1)
	list2_vals = Counter(list2)

	# convert to word-vectors
	words  = list(list1_vals.keys() | list2_vals.keys())
	vect1 = [list1_vals.get(word, 0) for word in words]       
	vect2 = [list2_vals.get(word, 0) for word in words]  

	return cosine_similarity([vect1], [vect2])[0][0] #returns float in range 0.0 - 1.0

# convert all to lowercase
# remove stopwords

def train_model():
	if not users:
		print("Geen data om model te trainen.. sim gebruikers eerst")
		return

	print('Train model on users:', users)

	print("Not implemented yet...")

def clear_users():
	global users
	users = []
