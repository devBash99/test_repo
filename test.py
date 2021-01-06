from os import getenv
from dotenv import load_dotenv

load_dotenv()
key = getenv("KEY")

print(key)
