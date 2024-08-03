# app/tests/utils/utils.py

import random
import string

def random_email() -> str:
    return f"{random_lower_string()}@test.com"

def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=12))
