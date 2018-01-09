from exchange import *

class DummyExchange(Exchange):

	def __str__(self):
		return super(DummyExchange, self).__str__()

	def __init__(self, apiKey):
		super(DummyExchange, self).__init__(apiKey)
		self.exchangeName = "Dummy Exchange"

	def getBidAskPrice(self, coin):
		super(DummyExchange, self).getBidAskPrice(coin)

	def getUSDPrice(self, coin):
		super(DummyExchange, self).getUSDPrice(coin)
