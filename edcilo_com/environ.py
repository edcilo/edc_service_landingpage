import environ
from pathlib import Path

env = environ.Env(
    # set casting, default value
    APP_DEBUG=(bool, True)
)

# two folders back (/a/b/ - 2 = /)
base = environ.Path(__file__) - 2

# reading .env file
environ.Env.read_env(env_file=base('.env'))
