import sys
sys.path.append("exchanges")
from exchange_modules import *

from time import *
from datetime import *

import argparse


class DummyTrader:

	wallets = {
		"BTC" : {"id" : 1, "balance" : 1, "lastBuyPrice" : 15000.0, "lastSellPrice" : 15900.0},
		"ETH" : {"id" : 2, "balance" : 1, "lastBuyPrice" : 1000.0, "lastSellPrice" : 1100.0 },
		"LTC" : {"id" : 3, "balance" : 1, "lastBuyPrice" : 270.0, "lastSellPrice" : 280.0},
		"USD" : {"id" : 0, "balance" : 10000.0}
	}

	tradeStrategy = {
		"maxBuyPct" : 0.93,
		"minSellPct" : 1.07
	}

	def __init__(self):
		pass

	def sellCoin(self, coin, coinAmount, sellPrice):
		if (self.wallets[coin]["balance"] - coinAmount < 0):
			print("Not enough coin {} to sell.".format(coin))
			return

		self.wallets[coin]["balance"] -= coinAmount
		self.wallets[coin]["lastSellPrice"] = sellPrice
		self.wallets["USD"]["balance"] += sellPrice * coinAmount

	def buyCoin(self, coin, coinAmount, buyPrice):
		cost = buyPrice * coinAmount
		if (self.wallets["USD"]["balance"] - cost < 0):
			print("Not enough money to buy.")
			return

		self.wallets["USD"]["balance"] -= cost
		self.wallets[coin]["balance"] += coinAmount
		self.wallets[coin]["lastBuyPrice"] = buyPrice
		

	def trade(self, exchange, coin, amount, tradeStrategy):
		transactionPct = .01

		if ((abs(tradeStrategy["maxBuyPct"] - 1) < transactionPct) or (abs(tradeStrategy["minSellPct"] - 1) < transactionPct)):
			raise Exception("Strategy Guarantees Loss.")
		
		try:
			price = exchange.getUSDPrice(coin)
		except:
			sleep(5)
			return

		sellPrice, buyPrice = price, price
		# sellPrice, buyPrice = exchange.getBidAskPrice(coin)

		sellPriceActual = (sellPrice - (sellPrice * transactionPct))
		buyPriceActual = (buyPrice * (1.0 + transactionPct))

		coinWallet = self.wallets[coin]
		usdWallet = self.wallets["USD"]

		if (buyPrice <= (tradeStrategy["maxBuyPct"] * coinWallet["lastSellPrice"])):
			self.buyCoin(coin, amount, buyPriceActual)

		if (sellPrice >= (tradeStrategy["minSellPct"] * coinWallet["lastBuyPrice"])):
			self.sellCoin(coin, amount, sellPriceActual)

		print("CURRENT PRICES\n Buy: {} Sell {}\nWALLET INFO\n {}\n{}\n".format(buyPrice, sellPrice, coinWallet, usdWallet))

	def autoTrade(self, exchange, coin, amount, interval=5):
		
		i = 0
		iEnd = 1000
		while i < iEnd:
			self.trade(exchange, coin, amount, self.tradeStrategy)
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

	dummy = DummyTrader()
	dummy.autoTrade(k, args.c, 0.2)

if __name__ == '__main__':
	main(sys.argv)
