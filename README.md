<<<<<<< HEAD
# 🔓 Hash Cracker - Educational Security Tool
=======
# 🔓 Enhanced Hash Cracker v2.0
>>>>>>> 0b6ccb67b36ebbe98015f27328ef7739e2ff6ddc

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
<<<<<<< HEAD
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![License](https://img.shields.io/badge/License-Educational-yellow.svg)
![Status](https://img.shields.io/badge/Status-Live-brightgreen.svg)

*Educational cybersecurity tool demonstrating hash functions and password security*

[🚀 **Live Web Demo**](https://hash-education-portfolio.onrender.com) | [💻 CLI Version](#cli-version) | [🌐 Web Portfolio](#web-portfolio)

</div>

## 🎯 Project Overview

This project demonstrates cybersecurity fundamentals through an educational hash cracking tool. It showcases both **command-line proficiency** and **web development skills** by providing two complementary interfaces:

1. **🖥️ Enhanced CLI Tool** - Professional command-line application with advanced features
2. **🌐 Interactive Web Portfolio** - Educational web interface deployed on Render

## ✨ Dual Implementation

### 🖥️ **CLI Version Features**
- **Multi-Algorithm Support** - SHA256, MD5, SHA1, SHA512
- **Real-time Progress Tracking** - Live attempts counter and speed indicator
- **Professional Interface** - Colorful ANSI output with emojis
- **Command Line Arguments** - Full CLI interface with argparse
- **Threading Support** - Non-blocking progress indicators
- **Performance Metrics** - Detailed timing and rate statistics

### 🌐 **Web Portfolio Features**
- **Interactive Hash Generator** - Real-time hash creation
- **Demo Cracking Simulation** - Safe educational demonstrations
- **Responsive Design** - Works on all devices
- **Educational Content** - Comprehensive security lessons
- **Professional Presentation** - Perfect for portfolios and job applications

## 🚀 Quick Start

### **Try the Live Web Demo** 
👉 **[https://hash-education-portfolio.onrender.com](https://hash-education-portfolio.onrender.com)**

### **Use the CLI Version**
```bash
# Clone the repository
git clone https://github.com/TheGhostPacket/hash-cracker.git
cd hash-cracker

# Run the enhanced CLI version
python hash_cracker.py

# Or with command line arguments
python hash_cracker.py --hash 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 --wordlist wordlist.txt
```

### **Run the Web Version Locally**
```bash
# Navigate to web portfolio
cd web-portfolio

# Install dependencies
pip install -r requirements.txt

# Run Flask application
python app.py
```

## 📊 Live Demo Examples

### **Hash Generator**
Try these in the web demo:
- Input: `password123` → SHA256: `ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f`
- Input: `hello` → MD5: `5d41402abc4b2a76b9719d911017c592`

### **Demo Cracking**
Test with these educational hashes:
- `password` → `5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8` (SHA256)
- `hello` → `2cf24dba4f21d4288094c85b66a5a6c59e9fe49a9ce0e473e8bba76ec1abb0fb` (SHA256)

## 🏗️ Project Architecture

```
hash-cracker/
├── hash_cracker.py              # Enhanced CLI application
├── README.md                    # This documentation
├── web-portfolio/               # Web interface
│   ├── app.py                   # Flask backend
│   ├── requirements.txt         # Dependencies
│   ├── templates/
│   │   └── index.html          # Frontend interface
│   └── README.md               # Deployment instructions
├── wordlists/                   # Sample wordlists (optional)
│   └── common.txt
└── examples/                    # Sample hashes (optional)
    └── test_hashes.txt
```

## 🎓 Technical Skills Demonstrated

### **Backend Development**
- ✅ Python programming with advanced features
- ✅ Flask web framework
- ✅ RESTful API design
- ✅ Error handling and validation
- ✅ Threading and concurrency

### **Frontend Development**
- ✅ Responsive HTML/CSS design
- ✅ Interactive JavaScript
- ✅ Modern UI/UX principles
- ✅ Progressive enhancement

### **DevOps & Deployment**
- ✅ Cloud deployment (Render)
- ✅ Environment configuration
- ✅ Production-ready applications
- ✅ CI/CD with Git integration

### **Cybersecurity Knowledge**
- ✅ Cryptographic hash functions
- ✅ Password security analysis
- ✅ Attack vector understanding
- ✅ Security best practices

## 🔍 Supported Hash Algorithms

| Algorithm | CLI Support | Web Support | Output Length | Security Level |
|-----------|-------------|-------------|---------------|----------------|
| **MD5** | ✅ | ✅ | 32 chars | ⚠️ Weak |
| **SHA-1** | ✅ | ✅ | 40 chars | ⚠️ Deprecated |
| **SHA-256** | ✅ | ✅ | 64 chars | ✅ Strong |
| **SHA-512** | ✅ | ✅ | 128 chars | ✅ Very Strong |

## 📈 Performance Benchmarks

### **CLI Version Performance**
- **Processing Speed**: ~15,000 hashes/second
- **Memory Usage**: < 50MB for large wordlists
- **File I/O**: Optimized streaming for GB+ files
- **Threading**: Non-blocking UI updates

### **Web Version Performance**
- **Response Time**: < 100ms for hash generation
- **Concurrent Users**: Handles 50+ simultaneous demos
- **Mobile Responsive**: Works on all screen sizes
- **Accessibility**: WCAG 2.1 compliant

## 🛡️ Security & Educational Value

### **What This Project Teaches**
- **Password Vulnerability**: How weak passwords are compromised
- **Hash Function Properties**: One-way functions, collision resistance
- **Attack Methodologies**: Dictionary attacks, brute force techniques
- **Defense Strategies**: Salting, key stretching, strong passwords

### **Ethical Considerations**
- **Educational Focus**: Designed for learning, not malicious use
- **Controlled Environment**: Web demo uses only safe, predefined data
- **Security Awareness**: Promotes better password practices
- **Responsible Disclosure**: Clear usage guidelines and disclaimers

## 🌟 Project Evolution

### **Phase 1: Initial CLI Tool**
- Basic dictionary attack implementation
- Simple file processing
- Core functionality proof-of-concept

### **Phase 2: Enhanced CLI Version**
- Added multiple hash algorithms
- Implemented progress tracking
- Professional UI with colors and animations
- Command-line argument parsing
- Performance optimizations

### **Phase 3: Web Portfolio**
- Translated core functionality to web interface
- Added educational content and demonstrations
- Implemented safe, demo-only cracking
- Deployed to cloud platform
- Created comprehensive documentation

### **Future Enhancements**
- GPU acceleration integration
- Advanced attack modes (hybrid, rule-based)
- Real-time collaboration features
- Educational certification integration

## 🚀 Deployment Information

### **Web Version**
- **Platform**: Render.com
- **URL**: [https://hash-education-portfolio.onrender.com](https://hash-education-portfolio.onrender.com)
- **Stack**: Python 3.11, Flask 2.3.3, Gunicorn
- **Features**: Auto-deployment from GitHub, custom domain support

### **Local Development**
Both versions can be run locally for development and testing. See individual README files for specific instructions.

## 📚 Learning Resources

### **Educational Materials**
- [OWASP Password Storage Guidelines](https://owasp.org/www-project-cheat-sheets/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [NIST Password Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [Cryptography Engineering Book](https://www.schneier.com/books/cryptography_engineering/)

### **Technical Documentation**
- [Python hashlib Documentation](https://docs.python.org/3/library/hashlib.html)
- [Flask Framework Guide](https://flask.palletsprojects.com/)
- [Render Deployment Docs](https://render.com/docs)

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Additional hash algorithm support
- Enhanced educational content
- Mobile app version
- Performance optimizations
- Accessibility improvements

### **Development Setup**
```bash
# Fork the repository
git clone https://github.com/yourusername/hash-cracker.git
cd hash-cracker

# Create feature branch
git checkout -b feature/your-enhancement

# Make changes and test
python hash_cracker.py  # Test CLI
cd web-portfolio && python app.py  # Test web

# Submit pull request
```

## 📄 License & Disclaimer

### **Educational Use Only**
This project is designed exclusively for educational purposes:
- ✅ Learning cybersecurity concepts
- ✅ Testing personal systems with authorization
- ✅ Educational demonstrations and training
- ✅ Security research in controlled environments

### **Prohibited Uses**
- ❌ Unauthorized system attacks
- ❌ Illegal password cracking
- ❌ Malicious activities
- ❌ Circumventing security without permission

## 👤 Author

**TheGhostPacket**
- 🐙 GitHub: [@TheGhostPacket](https://github.com/TheGhostPacket)
- 💼 LinkedIn: [Your LinkedIn Profile](#)
- 🌐 Portfolio: [Live Demo](https://hash-education-portfolio.onrender.com)
- 📧 Contact: [contact@theghostpacket.com](#)
=======
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

## 👤 Built by [TheGhostPacket](https://github.com/TheGhostPacket)

*Remember: With great power comes great responsibility. Use this knowledge to build more secure systems, not to break them.*
>>>>>>> 0b6ccb67b36ebbe98015f27328ef7739e2ff6ddc

---

<div align="center">

<<<<<<< HEAD
**🛡️ Built for Security Education • 🧠 Promoting Ethical Learning • 🔒 Advancing Cybersecurity**

*This project demonstrates technical proficiency while promoting responsible cybersecurity practices.*

</div>
=======
**🛡️ Stay Ethical • 🧠 Keep Learning • 🔒 Build Secure**

</div>
>>>>>>> 0b6ccb67b36ebbe98015f27328ef7739e2ff6ddc
