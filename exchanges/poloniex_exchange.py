from exchange import *
from poloniex import Poloniex

class PoloniexExchange(Exchange):

	def __str__(self):
		return super(PoloniexExchange, self).__str__()

	def __init__(self, apiKey):
		super(PoloniexExchange, self).__init__(apiKey)
		self.exchangeName = "Poloniex"

	def getUSDPrice(self, coin):
		polo = Poloniex()
		return polo.returnTicker()["USDT_BTC"]["last"]

