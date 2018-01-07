from coinbase_exchange import *
from dummy_exchange import *
from poloniex_exchange import *
from kraken_exchange import *

def main():
	e = Exchange("apiKey")
	cb = CoinbaseExchange("apiKey")
	d = DummyExchange("apiKey")
	p = PoloniexExchange("apiKey")
	k = KrakenExchange("apiKey")

	#print(e.getUSDPrice("BTC"))
	#print(cb.getUSDPrice("BTC"))
	#print(d.getUSDPrice("BTC"))
	print(p.getUSDPrice("BTC"))
	print(k.getUSDPrice("BTC"))

if __name__ == '__main__':
	main()
