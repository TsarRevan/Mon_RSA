import sys
import math
import random
import json
import time

KEYS_FILE = "keys.json"

def is_prime(num):
    if num <= 1:
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
    gcd_val, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd_val, x, y

def mod_inverse(e, phi):
    gcd_val, x, _ = extended_gcd(e, phi)
    if gcd_val != 1:
        raise ValueError("L'inverse modulo n'existe pas.")
    return x % phi

def save_keys(e, d, n):
    keys = {"public": {"e": e, "n": n}, "private": {"d": d, "n": n}}
    with open(KEYS_FILE, "w") as file:
        json.dump(keys, file)
    print("✅ Clés sauvegardées dans 'keys.json'.")

def load_keys():
    try:
        with open(KEYS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("❌ Aucune clé trouvée. Veuillez d'abord générer des clés avec 'generate_keys'.")
        sys.exit(1)

def generate_keys():
    print("🔑 Génération des clés RSA...")
    time.sleep(1)

    p = generate_prime(10, 100)
    q = generate_prime(10, 100)
    while p == q:
        q = generate_prime(10, 100)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)

    print("✅ Clés générées avec succès !")
    print(f"🔐 Clé publique : (e = {e}, n = {n})")
    print(f"🔓 Clé privée : (d = {d}, n = {n})")

    save_keys(e, d, n)

def encrypt(message):
    keys = load_keys()
    e, n = keys["public"]["e"], keys["public"]["n"]
    encrypted_message = [pow(ord(char), e, n) for char in message]
    encrypted_string = ' '.join(map(str, encrypted_message))
    print(f"🔒 Message chiffré : {encrypted_string}")
    return encrypted_string

def decrypt(encrypted_message):
    keys = load_keys()
    d, n = keys["private"]["d"], keys["private"]["n"]
    decrypted_message = ''.join(chr(pow(int(char), d, n)) for char in encrypted_message.split())
    print(f"🔓 Message déchiffré : {decrypted_message}")
    return decrypted_message

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"help", "-h", "--help"}:
        print("""
        === Menu RSA Simplifié ===
        Commandes disponibles :
        - generate_keys : Génère une paire de clés RSA.
        - encrypt "<message>" : Chiffre un message (utilise la clé publique enregistrée).
        - decrypt "<message_chiffré>" : Déchiffre un message (utilise la clé privée enregistrée).
        
        Exemples :
        python rsa.py generate_keys
        python rsa.py encrypt "Kebab succulent"
        python rsa.py decrypt "2701 3225 1101 452 1101 1239 1668 1628 1268 1268 1628 463 3225 3376 471"
        """)
        return

    command = sys.argv[1]

    if command == "generate_keys":
        generate_keys()

    elif command == "encrypt":
        if len(sys.argv) != 3:
            print("Usage : python rsa.py encrypt \"<message>\"")
            return
        message = sys.argv[2]
        encrypt(message)

    elif command == "decrypt":
        if len(sys.argv) != 3:
            print("Usage : python rsa.py decrypt \"<message_chiffré>\"")
            return
        encrypted_message = sys.argv[2]
        decrypt(encrypted_message)

    else:
        print("Commande inconnue. Utilisez 'help' pour afficher le manuel.")

if __name__ == "__main__":
    main()
