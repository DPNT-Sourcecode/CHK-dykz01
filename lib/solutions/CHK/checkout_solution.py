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
    itemPrices['F'] = {1:10}
    itemPrices['G'] = {1:20}
    itemPrices['H'] = {1:10, 5:45, 10:80}
    itemPrices['I'] = {1:35}
    itemPrices['J'] = {1:60}
    itemPrices['K'] = {1:80, 2:150}
    itemPrices['L'] = {1:90}
    itemPrices['M'] = {1:15}
    itemPrices['N'] = {1:40}
    itemPrices['O'] = {1:10}
    itemPrices['P'] = {1:50, 5:200}
    itemPrices['Q'] = {1:30, 3:80}
    itemPrices['R'] = {1:50}
    itemPrices['S'] = {1:30}
    itemPrices['T'] = {1:20}
    itemPrices['U'] = {1:40}

    itemFreebies = {}
    itemFreebies['E'] = {2:'B'}
    itemFreebies['F'] = {3:'F'}
    itemFreebies['N'] = {3:'M'}
    itemFreebies['R'] = {3:'Q'}
    itemFreebies['U'] = {4:'U'}

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

    def test_singlePrices(self):
        self.assertEqual(checkout('A'), 50)
        self.assertEqual(checkout('B'), 30)
        self.assertEqual(checkout('C'), 20)
        self.assertEqual(checkout('D'), 15)
        self.assertEqual(checkout('E'), 40)
        self.assertEqual(checkout('F'), 10)
        self.assertEqual(checkout('G'), 20)
        self.assertEqual(checkout('H'), 10)
        self.assertEqual(checkout('I'), 35)
        self.assertEqual(checkout('J'), 60)
        self.assertEqual(checkout('K'), 80)
        self.assertEqual(checkout('L'), 90)
        self.assertEqual(checkout('M'), 15)
        self.assertEqual(checkout('N'), 40)
        self.assertEqual(checkout('O'), 10)
        self.assertEqual(checkout('P'), 50)
        self.assertEqual(checkout('Q'), 30)
        self.assertEqual(checkout('R'), 50)
        self.assertEqual(checkout('S'), 30)
        self.assertEqual(checkout('T'), 20)
        self.assertEqual(checkout('U'), 40)

    def test_multipleItemOffers(self):
        self.assertEqual(checkout('AAA'), 130)
        self.assertEqual(checkout('AAAAA'), 200)
        self.assertEqual(checkout('BB'), 45)
        self.assertEqual(checkout("HHHHH"), 45)
        self.assertEqual(checkout("HHHHHHHHHH"), 80)
        self.assertEqual(checkout("KK"), 150)
        self.assertEqual(checkout("PPPPP"), 200)
        self.assertEqual(checkout("QQQ"), 80)

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

    def test_3FSpecialOfferGivesOneFreeF(self):
        self.assertEqual(checkout("FFF"), checkout("F") * 2)
        self.assertEqual(checkout("FFFFF"), checkout("F") * 4)
        self.assertEqual(checkout("FFFFFF"), checkout("F") * 4)

    def test_3NSpecialOfferGivesOneFreeM(self):
        self.assertEqual(checkout("NNNM"), checkout("NNN"))

    def test_3RSpecialOfferGivesOneFreeQ(self):
        self.assertEqual(checkout("RRRQ"), checkout("RRR"))

    def test_4USpecialOfferGivesOneFreeQ(self):
        self.assertEqual(checkout("QQQQ"), checkout("QQQ"))



if __name__ == '__main__':
    unittest.main()



