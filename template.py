
import tables
import tkinter as tk
import database


class Interface:

	def __init__(self):
		self.echa = 0

	def display_help(self, menu):
		self.menu = menu

		self.txt_main = "		########## Menu principal ##########\n \
		Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
			1 : Sélectionnez une catégorie \n \
			2 : Choisir un aliment à substitué. \n \
			q : Quitter le programme."

		self.txt_main_path = "\n 		########## Menu {0} ###########\n \
		Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
			r : retour \n \
			q : Quitter \n \
		".format(self.menu)

		self.txt_feature ="\n 		########## Menu {0} ########## \n \
		Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
			r : retour \n \
			q : Quitter \n \
			e : Enregistrer \n \
		".format(self.menu)

		self.text_favorite ="\n 		########## Menu {0} ########## \n \
		Mode d'emploi : Pour modifier ou supprimer un favori, rentrez le numéro correspondant au choix. \n \
			r : retour \n \
			q : Quitter \n \
			s : Supprimer\n \
		".format(self.menu)


		if self.menu == 'main':
			print(self.txt_main)
		if self.menu == 'category':
			print(self.txt_main_path)
		if self.menu == 'product':
			print(self.txt_main_path)
		if self.menu == 'feature':
			print(self.txt_feature)
		if self.menu == 'favorite':
			print(self.text_favorite)


	def category_menu(self, category_id, category_name):
		self.category_id = category_id
		self.category_name = category_name
		print("			{0} : {1}".format(self.category_id, self.category_name))


	def products_menu(self, product_id, product_name):
		self.product_id = product_id
		self.product_name = product_name
		print("			{0} : {1}".format(self.product_id, self.product_name))

	def display_feature(self, feature_list):
		self.feature_list = feature_list

		for feature in feature_list:
			print("Nom : {0}".format(feature[1]))
			print("Marque : {0}".format(feature[2]))
			print("Nutriments : {0} \n".format(feature[3]))


	
	def display_favorite(self, list_index, list_id_food, list_id_substitue):
		self.list_fav_index = list_index
		self.list_fav_food = list_id_food
		self.list_fav_sub = list_id_substitue
	
		for tuple_favorite in zip(self.list_fav_index, self.list_fav_food, self.list_fav_sub):
			print("	{0} :{1} : {2}".format(tuple_favorite[0], tuple_favorite[1], tuple_favorite[2]))
				









	





	


