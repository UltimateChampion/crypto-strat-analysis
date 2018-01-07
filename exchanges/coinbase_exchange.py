from exchange import *

class CoinbaseExchange(Exchange):

	def __str__(self):
		return super(CoinbaseExchange, self).__str__()

	def __init__(self, apiKey):
		super(CoinbaseExchange, self).__init__(apiKey)
		self.exchangeName = "Coinbase"

	def getUSDPrice(self, coin):
		return random.random() * 16000
