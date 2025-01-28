import sys
import math         
import random

def display_help():
##Pensez a rentrer un message pour le menu help
    print("""Menu Cauet Burger
""")
    
def is_prime(num):
    
    if num <=1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime(minimum, maximum):

    while True:
        num = random.randint(minimum, maximum)
        if is_prime(num):
            return num
    
def gcd(a, b):

    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):

    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def mod_inverse(e, phi):

    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("L'inverse modulo n'existe pas.")
    return x % phi