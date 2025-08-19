import unittest
from unittest.mock import patch
from health import vitals_ok  # assuming your code is saved as health.py


class TestVitals(unittest.TestCase):

    @patch("health.sleep", return_value=None)
    @patch("health.blink_alert")
    def test_temperature_out_of_range(self, mock_blink, mock_sleep):
        result = vitals_ok(104, 80, 95)
        self.assertFalse(result)
        mock_blink.assert_called_once()

    @patch("health.sleep", return_value=None)
    @patch("health.blink_alert")
    def test_pulse_out_of_range(self, mock_blink, mock_sleep):
        result = vitals_ok(98, 50, 95)
        self.assertFalse(result)
        mock_blink.assert_called_once()

    @patch("health.sleep", return_value=None)
    @patch("health.blink_alert")
    def test_spo2_out_of_range(self, mock_blink, mock_sleep):
        result = vitals_ok(98, 80, 85)
        self.assertFalse(result)
        mock_blink.assert_called_once()

    @patch("health.sleep", return_value=None)
    @patch("health.blink_alert")
    def test_all_vitals_ok(self, mock_blink, mock_sleep):
        result = vitals_ok(98, 75, 96)
        self.assertTrue(result)
        mock_blink.assert_not_called()


if __name__ == "__main__":
    unittest.main()
