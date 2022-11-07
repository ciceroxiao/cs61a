import unittest

from lab07 import Account, FreeChecking


class TestAccount(unittest.TestCase):
    def test_time_to_retire(self):
        a = Account("John")
        a.balance = 10
        balnace_to_retire = [10.25, 11, 100]
        years_to_retire = [2, 5, 117]
        for i, j in zip(balnace_to_retire, years_to_retire):
            with self.subTest(i=i, j=j):
                self.assertEqual(a.time_to_retire(amount=i), j)


class TestFreeChecking(unittest.TestCase):
    def test_withdraw_fee(self):
        ch = FreeChecking("Jack")
        ch.balance = 20
        amount_withdraw = [100, 3, 3, 3]
        amount_balance = [20, 17, 13, 9]
        for i, j in zip(amount_withdraw, amount_balance):
            with self.subTest(i=i, j=j):
                ch.withdraw(i)
                self.assertEqual(ch.balance, j)

        ch2 = FreeChecking("John")
        ch2.balance = 10
        self.assertEqual(ch2.withdraw(3), 7)
        self.assertEqual(ch.withdraw(3), 5)
        self.assertEqual(ch.withdraw(5), "Insufficient funds")


if __name__ == "__main__":
    unittest.main()
