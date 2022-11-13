import random
import string
def get_random_password(size=8):
    pandom = string.ascii_letters + string.ascii_lowercase + string.digits
    parol = " ".join(random.sample(pandom,size))
    return parol
print(get_random_password())
