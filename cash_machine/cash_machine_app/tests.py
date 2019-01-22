
# Create your tests here.
from django.test import TestCase
from .models import AccountUser, Bill
from .utils.utils import get_notes
from .utils.errors import NoteUnavailableException


class UtilTestCase(TestCase):
    def test_bank_note_calc_function(self):
        self.assertEquals(get_notes(30), [20.0, 10.0], msg="30 -> [20, 10]")
        self.assertEquals(get_notes(80), [50.0, 20.0, 10.0], msg="80 -> [50, 20, 10]")
        self.assertRaisesMessage(ValueError, "amount must be positive", get_notes, -130)
        self.assertRaisesMessage(NoteUnavailableException,
                                 "that amount cannot be given with the available banknote denominations", get_notes,
                                 125)
        self.assertEquals(get_notes(0), [])
        self.assertEquals(get_notes(None), [])


class UserTestCase(TestCase):
    def setUp(self):
        self.user1 = AccountUser.objects.create_user('test', 'abcd@efg.com', 'password')

    def test_user_create(self):
        self.assertTrue(self.user1.account_number is not None)
        self.assertTrue(self.user1.account_number in range(1000000000, 9999999999))

    def tearDown(self):
        self.user1.delete()

class BillsTestCase(TestCase):
    def setUp(self):
        self.d100 = Bill.objects.create(denomination=100)
        self.d50 = Bill.objects.create(denomination=50)
        self.d20 = Bill.objects.create(denomination=20)
        self.d10 = Bill.objects.create(denomination=10)

    def test_bills(self):
        pass

    def tearDown(self):
        self.d100.delete()
        self.d50.delete()
        self.d20.delete()
        self.d10.delete()