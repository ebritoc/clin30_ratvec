# -*- coding: utf-8 -*-

"""Constants module."""

import os

HERE = os.path.dirname(os.path.abspath(__file__))

DATA_DIRECTORY = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir, 'data'))
RESULTS_DIRECTORY = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir, 'results'))


EMOJI = '🐀'

MIN_CLASS_SAMPLES = 50
UNKNOWN_NGRAM = "UNK"

def make_data_directory():
    """Ensure that the data directory exists."""
    os.makedirs(DATA_DIRECTORY, exist_ok=True)
