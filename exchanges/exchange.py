import random

class Exchange(object):

	def __str__(self):
		return "Exchange: {}".format(self.exchangeName)

	def __init__(self, apiKey):
		self.apiKey = apiKey
		self.exchangeName = "Default Exchange"

	def getUSDPrice(self, coin):
		return random.random()
