import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self) -> None:
        print('setUp')
        self.emp_1 = Employee('MayYi', 'Aung', 60000)
        self.emp_2 = Employee('Julia', 'Thet', 70000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_main')
        self.assertEqual(self.emp_1.email, 'MayYi.Aung@gmail.com')
        self.assertEqual(self.emp_2.email, 'Julia.Thet@gmail.com')

        self.emp_1.first = 'Kyi'
        self.emp_2.first = 'Aung'
        self.assertEqual(self.emp_1.email, 'Kyi.Aung@gmail.com')
        self.assertEqual(self.emp_2.email, 'Aung.Thet@gmail.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'MayYi Aung')
        self.assertEqual(self.emp_2.fullname, 'Julia Thet')

        self.emp_1.first = 'Kyi'
        self.emp_2.first = 'Aung'

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        self.assertEqual(self.emp_1.pay, 63000)
        self.assertEqual(self.emp_2.pay, 73500)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            schedule = self.emp_1.monthly_schedule('Hnin')
            mocked_get.assert_called_with('http://company.com/Aung/Hnin')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('Jone')
            mocked_get.assert_called_with('http://company.com/Thet/Jone')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
