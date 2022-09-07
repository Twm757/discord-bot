
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

username =  os.getenv("username")

print(username)