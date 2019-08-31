import collections
import string
import unittest

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    itemPrices = {}
    itemPrices['A'] = {1:50, 3:130, 5:200}
    itemPrices['B'] = {1:30, 2:45}
    itemPrices['C'] = {1:20}
    itemPrices['D'] = {1:15}
    itemPrices['E'] = {1:40}

    itemFreebies = {}
    itemFreebies['E'] = {2:'B'}

    itemCounts = collections.defaultdict(int)
    for item in skus:
        invalidItem = not item in string.ascii_uppercase
        if invalidItem:
            return -1

        itemCounts[item] += 1

    freeItems = {}
    for item in itemCounts:
        itemFreebe = itemFreebies.get(item, {})
        for n, freeItem in itemFreebe.items():
            count = itemCounts[item]
            freebeeCount = int(count/n)
            freeItems[freeItem] = freebeeCount

    for item, count in freeItems.items():
        itemCounts[item] = max(0, itemCounts[item] - count)

    totalCost = 0
    for item, count in itemCounts.items():

        prices = itemPrices[item]
        for n in reversed(list(prices.keys())):
            price = prices[n]

            offerCount = int(count/n)
            totalCost += offerCount * price
            count -= offerCount * n

    return totalCost


class TestCheckOut(unittest.TestCase):
    def test_invalidSKUItemReturnsMinus1(self):
        self.assertEqual(checkout("AB32"), -1)
        self.assertEqual(checkout("ABc"), -1)
        self.assertEqual(checkout("AB!"), -1)

    def test_emptySKUCostsNothing(self):
        self.assertEqual(checkout(""), 0)

    def test_singleAPrice(self):
        self.assertEqual(checkout('A'), 50)

    def test_singleBPrice(self):
        self.assertEqual(checkout('B'), 30)

    def test_singleCPrice(self):
        self.assertEqual(checkout('C'), 20)

    def test_singleDPrice(self):
        self.assertEqual(checkout('D'), 15)

    def test_singleEPrice(self):
        self.assertEqual(checkout('E'), 40)

    def test_3AItemsMatchesSpecialOfferPrice(self):
        self.assertEqual(checkout('AAA'), 130)

    def test_5AItemsMatchesSpecialOfferPrice(self):
        self.assertEqual(checkout('AAAAA'), 200)

    def test_2BItemsMatchesSpecialOfferPrice(self):
        self.assertEqual(checkout('BB'), 45)

    def test_multipleNonOfferItemsAreMultiplesOfSingleItemPrice(self):
        self.assertEqual(checkout('CC'), checkout('C') * 2)
        self.assertEqual(checkout('DD'), checkout('D') * 2)

    def test_mixedSingleItemsAreSumOfIndividualPrices(self):
        self.assertEqual(checkout("BADC"), checkout("A") + checkout("B") + checkout("C") + checkout("D"))

    def test_multipleSpecialOffserAreMultipleOfSpecialOfferPrice(self):
        self.assertEqual(checkout("AAAAAAAAAA"), checkout("AAAAA") * 2)
        self.assertEqual(checkout("BBBB"), checkout("BB") * 2)

    def test_mixedOffersAreSumOfSpecialAndIndividualPrices(self):
        self.assertEqual(checkout("AAAAAAA"), checkout("AAAAA") + checkout("AA"))
        self.assertEqual(checkout("BBB"), checkout("BB") + checkout("B"))

    def test_mixedSpecialOffersAreSumsOfOffers(self):
        self.assertEqual(checkout("ABABA"), checkout("BB") + checkout("AAA"))

    def test_mixedItemsAreSumed(self):
        self.assertEqual(checkout("ABCCABADDA"), checkout("BB") + checkout("AAA") + checkout("A") + checkout("CC") + checkout("DD"))

    def test_specialOfferCombinationsMinimisePrice(self):
        self.assertEqual(checkout("AAAAAAAAA"), checkout("AAAAA") + checkout("AAA") + checkout("A"))

    def test_2ESpecialOfferGivesOneFreeB(self):
        self.assertEqual(checkout("EE"), checkout("E") + checkout("E"))
        self.assertEqual(checkout("EEB"), checkout("E") + checkout("E"))
        self.assertEqual(checkout("EEBEE"), checkout("E") * 4)
        self.assertEqual(checkout("EEBEEB"), checkout("E") * 4)
        self.assertEqual(checkout("EEBEEBB"), checkout("E") * 4 + checkout("B"))


if __name__ == '__main__':
    unittest.main()
