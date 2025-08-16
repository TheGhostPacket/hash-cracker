# 🔓 Enhanced Hash Cracker v2.0

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-Educational-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

*An advanced educational tool for understanding password security and cryptographic hash functions*

</div>

## 🌟 Features

### ✨ **Enhanced User Experience**
- **Colorful Terminal Interface** - Beautiful ANSI colors and emojis
- **Real-time Progress Tracking** - Live attempts counter and speed indicator
- **Professional Banner** - Clean, attractive startup display
- **Smart Input Validation** - Automatic hash format verification

### 🔧 **Technical Improvements**
- **Multiple Hash Algorithms** - SHA256, MD5, SHA1, SHA512 support
- **Command Line Arguments** - Full CLI interface with argparse
- **Threading Support** - Non-blocking progress indicators
- **Error Handling** - Robust file and encoding error management
- **Performance Metrics** - Detailed timing and rate statistics

### 🛠️ **Additional Tools**
- **Sample Hash Generator** - Create test hashes for practice
- **File Size Detection** - Wordlist size information
- **Keyboard Interrupt Handling** - Graceful exit with Ctrl+C

## 🚀 Installation & Usage

### Basic Usage (Interactive Mode)
```bash
python hash_cracker.py
```

### Advanced Usage (Command Line)
```bash
# Crack a SHA256 hash with rockyou.txt
python hash_cracker.py --hash 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 --wordlist rockyou.txt

# Use different algorithm
python hash_cracker.py -H ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f -w passwords.txt -a sha256

# Generate sample hashes for testing
python hash_cracker.py --samples

# Run without progress indicator (for scripting)
python hash_cracker.py --no-progress --hash [HASH] --wordlist [FILE]
```

## 📊 Example Output

```
╔══════════════════════════════════════════════════════════════╗
║                    🔓 HASH CRACKER v2.0                     ║
║                  Educational Security Tool                   ║
╚══════════════════════════════════════════════════════════════╝

🔍 Starting SHA256 crack attack...
📁 Wordlist: rockyou.txt (133.4 MB)
🎯 Target: 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8

⠋ Attempts: 2,847 | Rate: 15,230/sec | Time: 0.2s

🎉 SUCCESS! Password found!
📝 Password: hello
⏱️  Time taken: 0.19 seconds
🔢 Attempts: 2,847
📊 Rate: 15,037 attempts/sec
```

## 🎓 What You'll Learn

### **Cybersecurity Concepts**
- How dictionary attacks work in practice
- Why password complexity matters
- The role of salt in password security
- Hash function properties and differences

### **Programming Skills**
- File I/O with proper encoding handling
- Threading for non-blocking operations
- Command-line argument parsing
- Error handling and user input validation
- ANSI color codes and terminal formatting

### **Performance Analysis**
- Algorithm efficiency comparison
- I/O bottlenecks in brute force attacks
- Memory vs. speed trade-offs

## 🔍 Supported Hash Algorithms

| Algorithm | Output Length | Strength | Common Uses |
|-----------|---------------|----------|-------------|
| **MD5** | 32 chars | ⚠️ Weak | Legacy systems |
| **SHA1** | 40 chars | ⚠️ Deprecated | Git commits |
| **SHA256** | 64 chars | ✅ Strong | Bitcoin, SSL |
| **SHA512** | 128 chars | ✅ Very Strong | High security |

## 📁 Project Structure

```
hash-cracker/
├── hash_cracker.py      # Main enhanced script
├── README.md           # This documentation
├── wordlists/          # Sample wordlists
│   ├── common.txt
│   └── rockyou.txt
└── examples/           # Sample hashes
    └── test_hashes.txt
```

## 🧪 Testing with Sample Hashes

The tool includes a sample hash generator for practice:

```bash
python hash_cracker.py --samples
```

**Sample Targets:**
- `hello` → `2cf24dba4f21d4288094c85b66a5a6c59e9fe49a9ce0e473e8bba76ec1abb0fb` (SHA256)
- `password` → `5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8` (SHA256)

## ⚡ Performance Tips

1. **Use SSD storage** for faster wordlist reading
2. **Smaller wordlists first** - try common passwords before massive lists
3. **Multiple algorithms** - some hashes might be easier to crack with different functions
4. **Sort wordlists** by frequency for better hit rates

## 🛡️ Security Lessons

### **Why This Matters:**
- **Weak passwords** can be cracked in seconds
- **Dictionary attacks** are still highly effective
- **Password reuse** amplifies the risk
- **Proper hashing** with salt prevents these attacks

### **Best Practices:**
- Use **long, complex passwords** (12+ characters)
- Enable **two-factor authentication**
- Use **unique passwords** for each account
- Consider **password managers**

## ⚠️ Important Disclaimers

### **Educational Use Only**
This tool is designed for:
- ✅ Learning cybersecurity concepts
- ✅ Testing your own systems
- ✅ Authorized penetration testing
- ✅ Security research

### **Prohibited Uses**
- ❌ Attacking systems without permission
- ❌ Illegal password cracking
- ❌ Unauthorized access attempts
- ❌ Any malicious activities

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional hash algorithms
- GPU acceleration support
- Hybrid attack modes
- Rule-based transformations
- Web interface

## 📚 Further Learning

### **Recommended Resources:**
- [OWASP Password Security](https://owasp.org/www-project-cheat-sheets/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [Hashcat Documentation](https://hashcat.net/hashcat/)
- [John the Ripper](https://www.openwall.com/john/)
- [Cryptography Engineering](https://www.schneier.com/books/cryptography_engineering/)

### **Next Steps:**
1. Study rainbow tables and their prevention
2. Learn about bcrypt, scrypt, and Argon2
3. Explore GPU-accelerated cracking
4. Understand timing attacks

## 👤 Built by [PacketWhisperer](https://github.com/PacketWhisperer)

*Remember: With great power comes great responsibility. Use this knowledge to build more secure systems, not to break them.*

---

<div align="center">

**🛡️ Stay Ethical • 🧠 Keep Learning • 🔒 Build Secure**

</div>
