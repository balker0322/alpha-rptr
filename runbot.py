#!/usr/bin/env python
# coding: UTF-8

import signal
import time
import src.strategy as strategy

from tkinter import *

cls = getattr(strategy, 'test_bot')
bot = cls()
bot.test_net  = False
bot.back_test = False
bot.stub_test = False
bot.hyperopt  = False
bot.account = 'binanceaccount2'
bot.exchange_arg = 'binance'
bot.pair = 'ETHUSDT'
bot.run()

# signal.signal(signal.SIGINT, lambda x, y: bot.stop())
# while True:
#     time.sleep(1)

decimal_num = 3
price_decimal_num = 2
rr_ratio = 1.5
risk = 0.3
actual_leverage = 10.0

def get_calc_lot(lot, decimal_num:int, leverage:float, actual_leverage:float):
    calc_lot = lot / leverage
    calc_lot *= actual_leverage
    calc_lot -= calc_lot%(10**-decimal_num)
    calc_lot = round(calc_lot, decimal_num)
    return calc_lot 

def long_func():
    print('long_func')
    reward = risk*rr_ratio
    bot.exchange.sltp(profit_long=reward, profit_short=reward, stop_long=risk, stop_short=risk,round_decimals=price_decimal_num)
    lot = bot.exchange.get_lot()
    lot = get_calc_lot(lot=lot, decimal_num=decimal_num, leverage=20.0, actual_leverage=actual_leverage)
    bot.exchange.entry("Long", True, lot)

def short_func():
    print('short_func')
    reward = risk*rr_ratio
    bot.exchange.sltp(profit_long=reward, profit_short=reward, stop_long=risk, stop_short=risk,round_decimals=price_decimal_num)
    lot = bot.exchange.get_lot()
    lot = get_calc_lot(lot=lot, decimal_num=decimal_num, leverage=20.0, actual_leverage=actual_leverage)
    bot.exchange.entry("Short", False, lot)

def close_func():
    print('close_func')
    bot.exchange.cancel_all()
    bot.exchange.close_all()


top = Tk()  
  
top.geometry("200x100")    

long_button = Button(top, text="long", command=long_func)
short_button = Button(top, text="short", command=short_func)
close_button = Button(top, text="close", command=close_func)
long_button.pack()
short_button.pack()
close_button.pack()

top.mainloop()  