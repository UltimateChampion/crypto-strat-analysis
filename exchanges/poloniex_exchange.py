from exchange import *

class PoloniexExchange(Exchange):

	def __str__(self):
		return super(PoloniexExchange, self).__str__()

	def __init__(self, apiKey):
		super(PoloniexExchange, self).__init__(apiKey)
		self.exchangeName = "Coinbase"

	def getUSDPrice(self, coin):
		return random.random() * 16000
