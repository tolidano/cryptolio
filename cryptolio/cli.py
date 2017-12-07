#! /usr/bin/env python
"""
This helper is used as an entry point in setuptools.
"""
from __future__ import print_function, absolute_import
import argparse
from nyc_countdown_clock.clock import Clock


def add_args(parser):
    """
    Add command line arguments
    """
    parser.add_argument('-f', '--config', required=True, help='YAML configuration file for NYC CC')
    parser.add_argument('-s', '--stop', help='Stop on a line')
    parser.add_argument('-l', '--line', help='Subway line or bus route')
    parser.add_argument('-t', '--list', action='store_true', help='List all available lines')


def run_cli():
    """
    Entry point in setup tools and argument parser builder.
    """
    parser = argparse.ArgumentParser(description='CLI tool for NYC CC')
    add_args(parser)
    parsed_args = parser.parse_args()

    cli = Clock(config=parsed_args.config)
    if parsed_args.list is True:
        cli.list()
    elif parsed_args.stop is not None:
        if parsed_args.line is not None:
            print(cli.get_times_for_stop_on_line(stop=parsed_args.stop, line=parsed_args.line))
        else:
            print(cli.get_times_for_stop_on_line(stop=parsed_args.stop))
    else:
        if parsed_args.line is not None:
            print(cli.get_times_for_stop_on_line(line=parsed_args.line))
        else:
            print('You have to specify something to retrieve')
