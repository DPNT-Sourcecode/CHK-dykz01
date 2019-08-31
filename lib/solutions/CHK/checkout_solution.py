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
        if count in itemPrices[item]:
            totalCost += itemPrices[item][count]
        else:
            totalCost += count * itemPrices[item][1]

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
        self.assertEqual(checkout("ABCD"), checkout("A") + checkout("B") + checkout("C") + checkout("D"))




if __name__ == '__main__':
    unittest.main()

