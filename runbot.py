#!/usr/bin/env python
# coding: UTF-8

import signal
import time
import src.strategy as strategy

if __name__ == "__main__":
    cls = getattr(strategy, 'SMA')
    bot = cls()
    bot.test_net  = False
    bot.back_test = False
    bot.stub_test = False
    bot.hyperopt  = False
    bot.account = 'binanceaccount2'
    bot.exchange_arg = 'binance'
    bot.pair = 'ETHUSDT'
    bot.run()

    signal.signal(signal.SIGINT, lambda x, y: bot.stop())
    while True:
        time.sleep(1)