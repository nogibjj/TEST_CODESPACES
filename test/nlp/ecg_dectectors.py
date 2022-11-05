import csv
import logging
import math
from ecg_dectectors import Detectors

def read_data(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def parse_data(filereader,file):
    """Parse data from csv file into a list of floats."""
    logging.basicConfig(filename='ecg.log', level=logging.DEBUG)

    time=list()
    voltage=list()
    for row in filereader:
        line =r.strip().split(',')
        for r in row:
        try:
            t_line = float(line[0])
            v_line = float(line[1])
        except ValueError:
            logging.warning('Could not convert data to float: %s', line)
            


