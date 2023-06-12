import pyshorteners
from colorama import Fore, Style
import os
import platform

class url_curta():
	def __init__(self):

		self.sistema = platform.system()


		while True:

			if self.sistema == 'Windows':
				os.system('cls')
			else:
				os.system('clear')

			print(Fore.GREEN + '__  _____  __     _______  _____  _________ ')
			print(' / / / / _ \/ /    / ___/ / / / _ \/_  __/ _ |')
			print('/ /_/ / , _/ /__  / /__/ /_/ / , _/ / / / __ |')
			print('\____/_/|_/____/  \___/\____/_/|_| /_/ /_/ |_|' + Style.RESET_ALL)

			user_input_url = input('Ensira a URL completa incluido http, https : ')

			short = pyshorteners.Shortener()
			print(short.tinyurl.short(user_input_url))

			continuar = input('Continuar: ').lower()
			if continuar.startswith('s'):
				continue
			else:
				break




iniciar = url_curta()