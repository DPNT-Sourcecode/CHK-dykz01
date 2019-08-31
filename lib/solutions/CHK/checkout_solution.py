import collections
import unittest

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    itemPrices = {}
    itemPrices['A'] = {1:50, 3:130}
    itemPrices['B'] = {1:30, 2:45}
    itemPrices['C'] = {1:20}
    itemPrices['D'] = {1:15}

    itemCounts = collections.defaultdict(int)
    for item in skus:
        itemCounts[item] += 1

    totalCost = 0
    for item, count in itemCounts.items():

        prices = itemPrices[item]
        for n in reversed(list(prices.keys())):
            price = prices[n]

            if count >= n:
                offerCount = count/n
                totalCost += offerCount * price
                count -= offerCount * n

    return totalCost


class TestCheckOut(unittest.TestCase):
    def test_singleAPrice(self):
        self.assertEqual(checkout('A'), 50)

    def test_singleBPrice(self):
        self.assertEqual(checkout('B'), 30)

    def test_singleCPrice(self):
        self.assertEqual(checkout('C'), 20)

    def test_singleDPrice(self):
        self.assertEqual(checkout('D'), 15)

    def test_specialOfferAPriceOnly(self):
        self.assertEqual(checkout('AAA'), 130)

    def test_specialOfferBPriceOnly(self):
        self.assertEqual(checkout('BB'), 45)

    def test_mixedSingleItems(self):
        self.assertEqual(checkout("BADC"), checkout("A") + checkout("B") + checkout("C") + checkout("D"))

    def test_multipleASpecialOffsers(self):
        self.assertEqual(checkout("AAAAAAAAA"), checkout("AAA") * 3)




if __name__ == '__main__':
    unittest.main()
