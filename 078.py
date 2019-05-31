import random
import string
def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
print (randomStringDigits(6))
