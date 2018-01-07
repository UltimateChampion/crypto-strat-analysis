from coinbase_exchange import *
from dummy_exchange import *
from poloniex_exchange import *
from kraken_exchange import *
from time import *
from datetime import *

def visitExchanges(exchanges):
	exchangePriceDict = {}
	for exchange in exchanges:
		try:
			exchangePriceDict[exchange] = exchange.getUSDPrice("BTC")
		except:
			return None
	return exchangePriceDict
		
def generatePriceReport(exchanges, interval = 5):
	exchangeList = ",".join([exchange.__str__() for exchange in exchanges])
	header = "Time,{}".format(exchangeList)
	print(header)
		
	i = 0
	iEnd = 20
	while i < iEnd:
		exchangeVisitResult = visitExchanges(exchanges)
		if exchangeVisitResult:
			dataPoint = [datetime.now().strftime('%Y-%m-%d %H:%M:%S')] + [exchangeVisitResult[ex] for ex in exchanges]
			print(",".join(dataPoint))
			i += 1
		sleep(interval)
		

def main():
	e = Exchange("apiKey")
	cb = CoinbaseExchange("apiKey")
	d = DummyExchange("apiKey")
	p = PoloniexExchange("apiKey")
	k = KrakenExchange("apiKey")

	#print(e.getUSDPrice("BTC"))
	#print(cb.getUSDPrice("BTC"))
	#print(d.getUSDPrice("BTC"))
	#print(p.getUSDPrice("BTC"))
	#print(k.getUSDPrice("BTC"))

	generatePriceReport([p, k])

if __name__ == '__main__':
	main()
