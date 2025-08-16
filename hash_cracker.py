#!/usr/bin/env python3
"""
🔓 Enhanced Hash Cracker
Educational tool for understanding password security and hash functions
"""

import hashlib
import time
import sys
import os
from pathlib import Path
import argparse
import threading

class Colors:
    """ANSI color codes for terminal output"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class HashCracker:
    def __init__(self):
        self.attempts = 0
        self.start_time = None
        self.found = False
        self.stop_progress = False

    def print_banner(self):
        """Display an attractive banner"""
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                    🔓 HASH CRACKER v2.0                     ║
║                  Educational Security Tool                   ║
╚══════════════════════════════════════════════════════════════╝
{Colors.END}
{Colors.YELLOW}⚡ Supported algorithms: SHA256, MD5, SHA1, SHA512{Colors.END}
{Colors.MAGENTA}🎓 For educational and authorized testing only!{Colors.END}
"""
        print(banner)

    def get_hash_function(self, algorithm):
        """Return the appropriate hash function"""
        algorithms = {
            'sha256': hashlib.sha256,
            'md5': hashlib.md5,
            'sha1': hashlib.sha1,
            'sha512': hashlib.sha512
        }
        return algorithms.get(algorithm.lower())

    def validate_hash(self, target_hash, algorithm):
        """Validate hash format"""
        expected_lengths = {
            'md5': 32,
            'sha1': 40,
            'sha256': 64,
            'sha512': 128
        }
        
        if len(target_hash) != expected_lengths.get(algorithm.lower(), 0):
            return False
        
        try:
            int(target_hash, 16)  # Check if it's valid hex
            return True
        except ValueError:
            return False

    def progress_indicator(self):
        """Show a spinning progress indicator"""
        spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧']
        i = 0
        while not self.stop_progress and not self.found:
            if self.attempts > 0:
                elapsed = time.time() - self.start_time
                rate = self.attempts / elapsed if elapsed > 0 else 0
                print(f"\r{Colors.BLUE}{spinner[i % len(spinner)]}{Colors.END} "
                      f"Attempts: {Colors.YELLOW}{self.attempts:,}{Colors.END} | "
                      f"Rate: {Colors.CYAN}{rate:.0f}/sec{Colors.END} | "
                      f"Time: {Colors.MAGENTA}{elapsed:.1f}s{Colors.END}", end='', flush=True)
            time.sleep(0.1)
            i += 1

    def crack_hash(self, target_hash, wordlist_path, algorithm='sha256', show_attempts=True):
        """Enhanced hash cracking with progress tracking"""
        
        # Validate inputs
        if not self.validate_hash(target_hash, algorithm):
            print(f"{Colors.RED}❌ Invalid {algorithm.upper()} hash format!{Colors.END}")
            return False

        if not Path(wordlist_path).exists():
            print(f"{Colors.RED}❌ Wordlist file not found: {wordlist_path}{Colors.END}")
            return False

        hash_func = self.get_hash_function(algorithm)
        if not hash_func:
            print(f"{Colors.RED}❌ Unsupported algorithm: {algorithm}{Colors.END}")
            return False

        # Get file size for progress estimation
        file_size = Path(wordlist_path).stat().st_size
        print(f"\n{Colors.BLUE}🔍 Starting {algorithm.upper()} crack attack...{Colors.END}")
        print(f"{Colors.CYAN}📁 Wordlist: {wordlist_path} ({file_size/1024/1024:.1f} MB){Colors.END}")
        print(f"{Colors.YELLOW}🎯 Target: {target_hash}{Colors.END}\n")

        self.start_time = time.time()
        self.attempts = 0
        self.found = False
        self.stop_progress = False

        # Start progress indicator in separate thread
        if show_attempts:
            progress_thread = threading.Thread(target=self.progress_indicator, daemon=True)
            progress_thread.start()

        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
                for line_num, word in enumerate(file, 1):
                    word = word.strip()
                    if not word:  # Skip empty lines
                        continue
                    
                    self.attempts += 1
                    hashed_word = hash_func(word.encode()).hexdigest()
                    
                    if hashed_word == target_hash.lower():
                        self.found = True
                        self.stop_progress = True
                        elapsed = time.time() - self.start_time
                        
                        print(f"\n\n{Colors.GREEN}{Colors.BOLD}🎉 SUCCESS! Password found!{Colors.END}")
                        print(f"{Colors.GREEN}📝 Password: {Colors.BOLD}{word}{Colors.END}")
                        print(f"{Colors.CYAN}⏱️  Time taken: {elapsed:.2f} seconds{Colors.END}")
                        print(f"{Colors.YELLOW}🔢 Attempts: {self.attempts:,}{Colors.END}")
                        print(f"{Colors.MAGENTA}📊 Rate: {self.attempts/elapsed:.0f} attempts/sec{Colors.END}")
                        return True

        except KeyboardInterrupt:
            self.stop_progress = True
            print(f"\n\n{Colors.YELLOW}⚠️  Attack interrupted by user{Colors.END}")
            return False
        except Exception as e:
            self.stop_progress = True
            print(f"\n\n{Colors.RED}❌ Error reading wordlist: {e}{Colors.END}")
            return False

        # If we get here, password wasn't found
        self.stop_progress = True
        elapsed = time.time() - self.start_time
        print(f"\n\n{Colors.RED}❌ Password not found in wordlist{Colors.END}")
        print(f"{Colors.CYAN}⏱️  Time taken: {elapsed:.2f} seconds{Colors.END}")
        print(f"{Colors.YELLOW}🔢 Total attempts: {self.attempts:,}{Colors.END}")
        return False

    def generate_sample_hashes(self):
        """Generate sample hashes for testing"""
        test_passwords = ["password", "123456", "admin", "hello", "test"]
        print(f"\n{Colors.BLUE}🧪 Sample hashes for testing:{Colors.END}")
        print("-" * 50)
        
        for password in test_passwords:
            sha256_hash = hashlib.sha256(password.encode()).hexdigest()
            md5_hash = hashlib.md5(password.encode()).hexdigest()
            print(f"{Colors.YELLOW}Password:{Colors.END} {Colors.BOLD}{password}{Colors.END}")
            print(f"  {Colors.CYAN}SHA256:{Colors.END} {sha256_hash}")
            print(f"  {Colors.MAGENTA}MD5:{Colors.END}    {md5_hash}")
            print()

def main():
    parser = argparse.ArgumentParser(
        description="Educational hash cracking tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python hash_cracker.py
  python hash_cracker.py --hash 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 --wordlist rockyou.txt
  python hash_cracker.py --samples
        """
    )
    
    parser.add_argument('--hash', '-H', help='Target hash to crack')
    parser.add_argument('--wordlist', '-w', help='Path to wordlist file')
    parser.add_argument('--algorithm', '-a', default='sha256', 
                       choices=['sha256', 'md5', 'sha1', 'sha512'],
                       help='Hash algorithm (default: sha256)')
    parser.add_argument('--samples', action='store_true', 
                       help='Generate sample hashes for testing')
    parser.add_argument('--no-progress', action='store_true',
                       help='Disable progress indicator')

    args = parser.parse_args()
    
    cracker = HashCracker()
    cracker.print_banner()

    if args.samples:
        cracker.generate_sample_hashes()
        return

    # Get target hash
    if args.hash:
        target_hash = args.hash
    else:
        target_hash = input(f"{Colors.CYAN}🎯 Enter the {args.algorithm.upper()} hash to crack: {Colors.END}").strip()

    if not target_hash:
        print(f"{Colors.RED}❌ No hash provided!{Colors.END}")
        return

    # Get wordlist path
    if args.wordlist:
        wordlist_path = args.wordlist
    else:
        wordlist_path = input(f"{Colors.CYAN}📁 Enter path to wordlist file: {Colors.END}").strip()

    if not wordlist_path:
        print(f"{Colors.RED}❌ No wordlist provided!{Colors.END}")
        return

    # Start cracking
    success = cracker.crack_hash(
        target_hash, 
        wordlist_path, 
        args.algorithm,
        show_attempts=not args.no_progress
    )

    if success:
        print(f"\n{Colors.GREEN}✅ Hash successfully cracked!{Colors.END}")
    else:
        print(f"\n{Colors.YELLOW}💡 Consider trying a different wordlist or algorithm{Colors.END}")

    print(f"\n{Colors.MAGENTA}🛡️  Remember: Use strong, unique passwords!{Colors.END}")

if __name__ == "__main__":
    main()
