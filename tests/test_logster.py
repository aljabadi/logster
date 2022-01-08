#!/usr/bin/env python

"""Tests for `logster` package."""
import unittest
from logster import setup_logger
import logging


class TestLogster(unittest.TestCase):
    def test_logger_object(self):
        self.logger = setup_logger("app", "DEBUG")
        self.assertIsInstance(self.logger, logging.Logger)
        self.assertIsInstance(self.logger.handlers[0], logging.StreamHandler)
        self.assertEqual(self.logger.name, "app")


if __name__ == "__main__":
    unittest.main()
