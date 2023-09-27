"""Unit tests for rate.py Version 0.1.2

Last updated 9/26/2023"""

from unittest import TestCase, mock, main
from datetime import timedelta

from rate import (
    Rate, 
    Timecard
)

# Common hours expressed as integers
HOURS_8_INT = 8
HOURS_10_INT = 10
HOURS_11_INT = 11
HOURS_12_INT = 12
HOURS_14_INT = 14

# Common hours expressed as timedelta
HOURS_8_TIME = timedelta(hours=HOURS_8_INT)
HOURS_10_TIME = timedelta(hours=HOURS_10_INT)
HOURS_12_TIME = timedelta(hours=HOURS_12_INT)

# Double begins expressed as timedelta
HOURS_10_DOUBLE_BEGINS = timedelta(hours=HOURS_10_INT + 2)
HOURS_12_DOUBLE_BEGINS = timedelta(hours=HOURS_12_INT + 2)

# Default rate and hours used for testing
TEST_RATE = 750
TEST_HOURS = HOURS_10_INT

# Static rate calculations
RATE_100_HOURS_10 = round(TEST_RATE / HOURS_11_INT, 2)
RATE_100_HOURS_12 = round(TEST_RATE / HOURS_14_INT, 2)
RATE_150_HOURS_10 = round(RATE_100_HOURS_10 * 1.5, 2)
RATE_150_HOURS_12 = round(RATE_100_HOURS_12 * 1.5, 2)
RATE_200_HOURS_10 = round(RATE_100_HOURS_10 * 2, 2)
RATE_200_HOURS_12 = round(RATE_100_HOURS_12 * 2, 2)


class RateTest(TestCase):
    def test_day_rate(self):
        self.assertEqual(Rate(TEST_RATE, TEST_HOURS).day_rate, TEST_RATE)

    def test_double_begins_default_on_10_hours_int(self):
        result = Rate(TEST_RATE, HOURS_10_INT).double_begins
        expected = HOURS_10_DOUBLE_BEGINS
        self.assertEqual(result, expected)

    def test_double_begins_default_on_12_hours_int(self):
        result = Rate(TEST_RATE, HOURS_12_INT).double_begins
        expected = HOURS_12_DOUBLE_BEGINS
        self.assertEqual(result, expected)

    def test_double_begins_default_on_10_hours_time(self):
        result = Rate(TEST_RATE, HOURS_10_TIME).double_begins
        expected = HOURS_10_DOUBLE_BEGINS
        self.assertEqual(result, expected)

    def test_double_begins_default_on_12_hours_time(self):
        result = Rate(TEST_RATE, HOURS_12_TIME).double_begins
        expected = HOURS_12_DOUBLE_BEGINS
        self.assertEqual(result, expected)

    def test_double_begins_method(self):
        result = Rate(TEST_RATE, TEST_HOURS).get_double_begins(HOURS_10_TIME)
        expected = HOURS_10_DOUBLE_BEGINS
        self.assertEqual(result, expected)

    def test_double_begins_parameter(self):
        result = Rate(TEST_RATE, TEST_HOURS, double_begins=HOURS_12_DOUBLE_BEGINS).double_begins
        expected = HOURS_12_DOUBLE_BEGINS
        self.assertEqual(result, expected)

    def test_guarantee_on_10_hours_int(self):
        result = Rate(TEST_RATE, HOURS_10_INT).guarantee
        expected = HOURS_10_TIME
        self.assertEqual(result, expected)
    
    def test_guarantee_on_12_hours_int(self):
        result = Rate(TEST_RATE, HOURS_12_INT).guarantee
        expected = HOURS_12_TIME
        self.assertEqual(result, expected)

    def test_guarantee_on_10_hours_time(self):
        result = Rate(TEST_RATE, HOURS_10_TIME).guarantee
        expected = HOURS_10_TIME
        self.assertEqual(result, expected)

    def test_guarantee_on_12_hours_time(self):
        result = Rate(TEST_RATE, HOURS_12_TIME).guarantee
        expected = HOURS_12_TIME
        self.assertEqual(result, expected)
   
    def test_rate_100_on_10_hours_time(self):
        result = Rate(TEST_RATE, HOURS_10_TIME).rate_100
        expected = RATE_100_HOURS_10
        self.assertEqual(result, expected)

    def test_rate_100_on_12_hours_time(self):
        result = Rate(TEST_RATE, HOURS_12_TIME).rate_100
        expected = RATE_100_HOURS_12
        self.assertEqual(result, expected)

    def test_rate_150_on_10_hours_time(self):
        result = Rate(TEST_RATE, HOURS_10_TIME).rate_150
        expected = RATE_150_HOURS_10
        self.assertEqual(result, expected)

    def test_rate_150_on_12_hours_time(self):
        result = Rate(TEST_RATE, HOURS_12_TIME).rate_150
        expected = RATE_150_HOURS_12
        self.assertEqual(result, expected)

    def test_rate_200_on_10_hours_time(self):
        result = Rate(TEST_RATE, HOURS_10_TIME).rate_200
        expected = RATE_200_HOURS_10
        self.assertEqual(result, expected)

    def test_rate_200_on_12_hours_time(self):
        result = Rate(TEST_RATE, HOURS_12_TIME).rate_200
        expected = RATE_200_HOURS_12
        self.assertEqual(result, expected)


class TimecardTest(TestCase):
    @mock.patch('rate.input', create=True)
    def test_rate_100_on_10_hours_time(self, mocked_input):
        mocked_input.side_effect = ['8:00', '22:45']
        result = Timecard(TEST_RATE, TEST_HOURS).rate_100
        expected = RATE_100_HOURS_10
        self.assertEqual(result, expected)

    @mock.patch('rate.input', create=True)
    def test_rate_150_on_10_hours_time(self, mocked_input):
        mocked_input.side_effect = ['8:00', '22:45']
        result = Timecard(TEST_RATE, TEST_HOURS).rate_150
        expected = RATE_150_HOURS_10
        self.assertEqual(result, expected)


if __name__ == "__main__":
    main(verbosity=2)
