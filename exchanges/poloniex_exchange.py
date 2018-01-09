from exchange import *
from poloniex import Poloniex

class PoloniexExchange(Exchange):

	coinDict = {
		"BTC" : "BTC",
		"ETH" : "ETH",
		"LTC" : "LTC"
	}

	def __str__(self):
		return super(PoloniexExchange, self).__str__()

	def __init__(self, apiKey):
		super(PoloniexExchange, self).__init__(apiKey)
		self.exchangeName = "Poloniex"

	def getUSDBidAskPrice(self, coin):
		polo = Poloniex()

		pair = "USDT_{}".format(self.coinDict[coin])
		result = polo.returnTicker()[pair]
		return [result["bid"], result["ask"]]

	def getUSDPrice(self, coin):
		polo = Poloniex()

		pair = "USDT_{}".format(self.coinDict[coin])
		return polo.returnTicker()[pair]["last"]

