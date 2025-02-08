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

def generate_key(): 
    print ("Génération des clefs publicque et privé")
    p = generate_prime(10, 100)
    q = generate_prime(10, 100)
    while p == q:
        q = generate_prime(10, 100)

    n = p * q 
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) !=1:
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)

    print(f"Clef publique : (e = {e}, n = {n})")
    print(f"clef privé : (d = {d}, n = {n})")

def encrypt(message, e, n): 
    "Chiffrage le message avec la clef publique"
encrypted_message = [pow(ord(char), e, n)for char in message]
print(f"Message chiffré : {''.join(map(str, encrypted_message)) }")

def decrypt(encrypted_message, d, n):
    "Déchiffre un message avec la clé privée."
    decrypted_message = ''.join(
        chr(pow(int(char), d, n)) for char in encrypted_message.split())
    print(f"Message déchiffré : {decrypted_message}")
