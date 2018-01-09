from exchange import *
import krakenex

class KrakenExchange(Exchange):

	coinDict = {
		"BTC" : "XXBTZUSD",
		"ETH" : "XETHZUSD",
		"LTC" : "XLTCZUSD"
	}

	def __str__(self):
		return super(KrakenExchange, self).__str__()

	def __init__(self, apiKey):
		super(KrakenExchange, self).__init__(apiKey)
		self.exchangeName = "Kraken"

	def getUSDBidAskPrice(self, coin):
		kraken = krakenex.API()
		
		pair = self.coinDict[coin]

		result = kraken.query_public('Ticker', {'pair' : pair})['result'][pair]
		return [float(result["b"][0]), float(result["a"][0])]

	def getUSDPrice(self, coin):
		bidAskPrices = self.getUSDBidAskPrice(coin)
		return (bidAskPrices[0] + bidAskPrices[1]) * 0.5
