#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = -1
  buy_price = 0
  sell_price = 0
  change = True
  for i in range(0, len(prices) - 1):
    sell_price = prices[i+1]

    if change:
      buy_price = prices[i]

    if sell_price < buy_price:
      max_profit = sell_price - buy_price


    else:
      temp_profit = sell_price - buy_price
      if temp_profit > max_profit:
        max_profit = temp_profit
        change = False

  return max_profit

print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]), 94)

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))