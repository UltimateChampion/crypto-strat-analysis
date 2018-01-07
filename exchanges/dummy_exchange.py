from exchange import *

class DummyExchange(Exchange):

	def __str__(self):
		return super(DummyExchange, self).__str__()

	def __init__(self, apiKey):
		super(DummyExchange, self).__init__(apiKey)
		self.exchangeName = "Coinbase"

	def getUSDPrice(self, coin):
		return random.random() * 16000
