import unittest

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    specialOffers = {'3A':130, '2B':45}
    itemPrices = {'A':50, 'B':30, 'C':20, 'D':15}
    return itemPrices.get(skus)


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




if __name__ == '__main__':
    unittest.main()
