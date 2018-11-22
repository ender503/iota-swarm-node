import os
from dotenv import load_dotenv

config_file = '.env'
if os.path.isfile('.env.local'):
  config_file = '.env.local'
load_dotenv(config_file)

PORT = os.getenv('PORT')
FULLNODE = os.getenv('FULLNODE')
SEED = os.getenv('SEED')
