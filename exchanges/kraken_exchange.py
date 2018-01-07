from exchange import *
import krakenex

class KrakenExchange(Exchange):

	def __str__(self):
		return super(KrakenExchange, self).__str__()

	def __init__(self, apiKey):
		super(KrakenExchange, self).__init__(apiKey)
		self.exchangeName = "Kraken"

	def getUSDPrice(self, coin):
		kraken = krakenex.API()
		result = kraken.query_public('Ticker', {'pair' : 'XXBTZUSD'})['result']['XXBTZUSD']
		return (float(result["b"][0]) + float(result["a"][0]))*0.5

