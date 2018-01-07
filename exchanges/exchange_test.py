from coinbase_exchange import *
from dummy_exchange import *
from poloniex_exchange import *

def main():
	e = Exchange("apiKey")
	cb = CoinbaseExchange("apiKey")
	d = DummyExchange("apiKey")
	p = PoloniexExchange("apiKey")

	print e.getUSDPrice("BTC")
	print cb.getUSDPrice("BTC")
	print d.getUSDPrice("BTC")
	print p.getUSDPrice("BTC")

main()
