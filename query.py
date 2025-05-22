# File: query_table.py

import os
import logging
import yaml
import sys

# Setup logging
logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s [%(levelname)s] %(message)s',
  handlers=[
    logging.StreamHandler()
  ]
)

DATA_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]

with open(DATA_FILE, 'r') as file:
  data = yaml.load(file, Loader=yaml.FullLoader)

data[0]['test'] = 'MTG'

with open(OUTPUT_FILE, 'w') as file:
  file.write(yaml.dump(data, default_flow_style=None, width=70))