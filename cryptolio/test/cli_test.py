"""
Tests for CLI.
"""
import unittest
import mock
from nyc_countdown_clock.cli import run_cli


class CliTest(unittest.TestCase):

    @mock.patch('nyc_countdown_clock.cli.Clock')
    @mock.patch('nyc_countdown_clock.cli.argparse.ArgumentParser')
    def test_run_cli_no_conf(self, arg_mock, clock_mock):
        arg_mock.return_value.parse_args.return_value.conf = None
        arg_mock.return_value.parse_args.return_value.stop = 'TEST_STOP'
        arg_mock.return_value.parse_args.return_value.line = 'TEST_LINE'
        run_cli()

    @mock.patch('nyc_countdown_clock.cli.Clock')
    @mock.patch('nyc_countdown_clock.cli.argparse.ArgumentParser')
    def test_run_cli_get(self, arg_mock, clock_mock):
        arg_mock.return_value.parse_args.return_value.conf = 'TEST_FILE'
        arg_mock.return_value.parse_args.return_value.stop = 'TEST_STOP'
        arg_mock.return_value.parse_args.return_value.line = 'TEST_LINE'
        run_cli()

    @mock.patch('nyc_countdown_clock.cli.Clock')
    @mock.patch('nyc_countdown_clock.cli.argparse.ArgumentParser')
    def test_run_cli_list(self, arg_mock, clock_mock):
        arg_mock.return_value.parse_args.return_value.list = True
        run_cli()