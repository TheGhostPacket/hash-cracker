# 🔓 Hash Cracker (SHA256)

This Python tool attempts to crack SHA256 hashed passwords using a wordlist (dictionary attack). It helps you understand how brute force attacks work and why password hashing is essential.

## 💡 How It Works
- Compares each word in a wordlist to a given hash
- Hashes each word with SHA256
- Stops if a match is found

## 📥 Example
```bash
python hash_cracker.py
```

> Enter SHA256 hash: `5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8`  
> Enter wordlist: `rockyou.txt`

## 🎓 What I Learned
- How hashing functions work (SHA256 in this case)
- Why dictionary attacks succeed on weak passwords
- How to build a basic brute-force loop in Python
- File reading and string encoding

## 🔧 Tools Used
- Python
- hashlib
- rockyou.txt (or any custom wordlist)

## ⚠️ Disclaimer
This tool is for **educational purposes only**. Use responsibly.

## 👤 Built by [PacketWhisperer](https://github.com/PacketWhisperer)
