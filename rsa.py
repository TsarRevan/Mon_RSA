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
