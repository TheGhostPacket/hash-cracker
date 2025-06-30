import hashlib

def crack_hash(target_hash, wordlist):
    with open(wordlist, 'r', encoding='utf-8', errors='ignore') as file:
        for word in file:
            word = word.strip()
            hashed_word = hashlib.sha256(word.encode()).hexdigest()
            if hashed_word == target_hash:
                print(f"[✅] Password found: {word}")
                return
    print("[❌] Password not found in wordlist.")

# Example usage
if __name__ == "__main__":
    print("Hash Cracker - SHA256")
    target_hash = input("Enter the SHA256 hash to crack: ")
    wordlist_file = input("Enter path to wordlist (e.g., rockyou.txt): ")
    crack_hash(target_hash, wordlist_file)