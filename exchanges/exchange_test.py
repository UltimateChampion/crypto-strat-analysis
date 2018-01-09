from coinbase_exchange import *
from dummy_exchange import *
from poloniex_exchange import *
from kraken_exchange import *
from time import *
from datetime import *

import sys
import argparse

def visitExchanges(exchanges, coin):
	exchangePriceDict = {}
	for exchange in exchanges:
		try:
			exchangePriceDict[exchange] = exchange.getUSDPrice(coin)
		except:
			raise
			return None
	return exchangePriceDict
		
def generatePriceReport(exchanges, coin, interval = 5):
	exchangeList = ",".join([exchange.__str__() for exchange in exchanges])
	header = "Time,{}".format(exchangeList)
	print(header)
		
	i = 0
	iEnd = 10
	while i < iEnd:
		exchangeVisitResult = visitExchanges(exchanges, coin)
		if exchangeVisitResult:
			dataPoint = [datetime.now().strftime('%Y-%m-%d %H:%M:%S')] + [str(exchangeVisitResult[ex]) for ex in exchanges]
			print(",".join(dataPoint))
			i += 1
		sleep(interval)
		

def main(argv):
	parser = argparse.ArgumentParser(description='Generate Price Information for Exchanges over 50 seconds at 5 second intervals')
	parser.add_argument('-c', type=str, choices=["BTC", "ETH", "LTC"], help='Coin to Check Price For', required=True)

	args = parser.parse_args()

	e = Exchange("apiKey")
	cb = CoinbaseExchange("apiKey")
	d = DummyExchange("apiKey")
	p = PoloniexExchange("apiKey")
	k = KrakenExchange("apiKey")

	generatePriceReport([p, k], args.c)

if __name__ == '__main__':
	main(sys.argv)
