import random

class Exchange(object):

	def __str__(self):
		return "Exchange: {}".format(self.exchangeName)

	def __init__(self, apiKey):
		self.apiKey = apiKey
		self.exchangeName = "Default Exchange"

	def getUSDBidAskPrice(self, coin):
		return [getUSDPrice(coin), getUSDPrice(coin)]

	def getUSDPrice(self, coin):
		if coin == "BTC":
			return random.random() * 3000 + 14000
		if coin == "ETH":
			return random.random() * 400 + 800
		if coin == "LTC":
			return random.random() * 100 + 200
