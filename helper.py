import random, string
from models import ShortUrl


def generate_id():
    n = 5
    res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase , k = n))
    return res

 