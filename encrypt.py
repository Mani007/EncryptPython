import hashlib 
from dotenv import load_dotenv,dotenv_values

load_dotenv()
password = os.getenv("MY_SECRET")
print(hashlib.sha256(password)).hexdigest()
print(hashlib.algorithms_available)