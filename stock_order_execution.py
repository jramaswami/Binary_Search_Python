"""
binarysearch.com :: Stock Order Execution
jramaswami
"""
from collections import namedtuple
import heapq


Order = namedtuple('Order', ['price', 'shares'])


# Constants
BUY = 0
SELL = 1


class Solution:
    def solve(self, orders):
        total_shares_executed = 0
        sell_orders = []
        buy_orders = []
        for order_price, order_shares, order_type in orders:
            if order_type == BUY:
                # Buyer would like to buy as many shares as possible
                # for any price less than or equal to their buy price.
                while order_shares and sell_orders and sell_orders[0].price <= order_price:
                    sell_order = heapq.heappop(sell_orders)
                    if sell_order.shares <= order_shares:
                        # Buy all the shares from this sell order.
                        total_shares_executed += sell_order.shares
                        order_shares -= sell_order.shares
                    else:
                        # Buy shares from this sell order, finishing the buy order.
                        total_shares_executed += order_shares
                        delta = sell_order.shares - order_shares
                        sell_order0 = Order(sell_order.price, delta)
                        heapq.heappush(sell_orders, sell_order0)
                        order_shares = 0
                if order_shares > 0:
                    heapq.heappush(buy_orders, Order(-order_price, order_shares))
            else:
                # Seller would like to sell as many shares as possible for the
                # highest price.
                while order_shares and buy_orders and abs(buy_orders[0].price) >= order_price:
                    buy_order = heapq.heappop(buy_orders)
                    if buy_order.shares <= order_shares:
                        # Buy all the shares from this buy order.
                        total_shares_executed += buy_order.shares
                        order_shares -= buy_order.shares
                    else:
                        # Sell shares to this buy order, finishing the sell order.
                        total_shares_executed += order_shares
                        delta = buy_order.shares - order_shares
                        buy_order0 = Order(buy_order.price, delta)
                        heapq.heappush(buy_orders, buy_order0)
                        order_shares = 0
                if order_shares > 0:
                    heapq.heappush(sell_orders, Order(order_price, order_shares))

        return total_shares_executed


def test_1():
    orders = [
        [150, 5, 0],
        [190, 1, 1],
        [200, 1, 1],
        [100, 9, 0],
        [140, 8, 1],
        [210, 4, 0]
    ]
    assert Solution().solve(orders) == 9

def test_2():
    orders = [
        [2, 3, 1],
        [5, 1, 0]
    ]
    assert Solution().solve(orders) == 1

def test_3():
    orders = [
        [5, 5, 0],
        [3, 4, 1]
    ]
    assert Solution().solve(orders) == 4

def test_4():
    orders = [
        [3, 5, 1],
        [4, 4, 0],
        [4, 2, 0]
    ]
    assert Solution().solve(orders) == 5
