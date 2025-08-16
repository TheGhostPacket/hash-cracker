from flask import Flask, render_template, request, jsonify
import hashlib
import os
import time

app = Flask(__name__)

# Sample hashes for educational demonstration
DEMO_HASHES = {
    'sha256': {
        '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8': 'password',
        '2cf24dba4f21d4288094c85b66a5a6c59e9fe49a9ce0e473e8bba76ec1abb0fb': 'hello',
        'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f': 'test123',
        '8bb0cf6eb9b17d0f7d22b456f121257dc1254e1f01665370476383ea776df414': 'admin',
        '15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225': 'secret'
    },
    'md5': {
        '5d41402abc4b2a76b9719d911017c592': 'hello',
        '098f6bcd4621d373cade4e832627b4f6': 'test',
        '5f4dcc3b5aa765d61d8327deb882cf99': 'password',
        '21232f297a57a5a743894a0e4a801fc3': 'admin'
    }
}

# Demo wordlist for simulation
DEMO_WORDLIST = [
    'password', 'hello', 'test', 'admin', '123456', 'test123', 
    'secret', 'login', 'user', 'pass', 'demo', 'sample'
]

@app.route('/')
def home():
    """Main portfolio page"""
    return render_template('index.html')

@app.route('/generate_hash', methods=['POST'])
def generate_hash():
    """Generate hash for educational demonstration"""
    data = request.json
    text = data.get('text', '')
    algorithm = data.get('algorithm', 'sha256').lower()
    
    if not text:
        return jsonify({'error': 'No text provided'})
    
    try:
        if algorithm == 'sha256':
            hash_result = hashlib.sha256(text.encode()).hexdigest()
        elif algorithm == 'md5':
            hash_result = hashlib.md5(text.encode()).hexdigest()
        elif algorithm == 'sha1':
            hash_result = hashlib.sha1(text.encode()).hexdigest()
        elif algorithm == 'sha512':
            hash_result = hashlib.sha512(text.encode()).hexdigest()
        else:
            return jsonify({'error': 'Unsupported algorithm'})
        
        return jsonify({
            'text': text,
            'algorithm': algorithm.upper(),
            'hash': hash_result,
            'length': len(hash_result)
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/demo_crack', methods=['POST'])
def demo_crack():
    """Demonstrate hash cracking with limited demo data"""
    data = request.json
    target_hash = data.get('hash', '').lower()
    algorithm = data.get('algorithm', 'sha256').lower()
    
    if not target_hash:
        return jsonify({'error': 'No hash provided'})
    
    # Check if it's a demo hash
    if target_hash not in DEMO_HASHES.get(algorithm, {}):
        return jsonify({
            'success': False,
            'message': 'Hash not found in demo dataset',
            'note': 'This demo only works with predefined educational hashes',
            'available_demos': list(DEMO_HASHES.get(algorithm, {}).keys())
        })
    
    # Simulate the cracking process
    start_time = time.time()
    attempts = 0
    
    # Get the hash function
    hash_func = getattr(hashlib, algorithm, None)
    if not hash_func:
        return jsonify({'error': 'Unsupported algorithm'})
    
    # Simulate checking each word in wordlist
    for word in DEMO_WORDLIST:
        attempts += 1
        time.sleep(0.01)  # Small delay to simulate processing
        
        word_hash = hash_func(word.encode()).hexdigest()
        if word_hash == target_hash:
            elapsed = time.time() - start_time
            return jsonify({
                'success': True,
                'password': word,
                'attempts': attempts,
                'time_taken': round(elapsed, 3),
                'rate': round(attempts / elapsed) if elapsed > 0 else 0,
                'algorithm': algorithm.upper()
            })
    
    # If not found (shouldn't happen with demo data)
    elapsed = time.time() - start_time
    return jsonify({
        'success': False,
        'message': 'Password not found in demo wordlist',
        'attempts': attempts,
        'time_taken': round(elapsed, 3)
    })

@app.route('/get_demo_hashes')
def get_demo_hashes():
    """Return available demo hashes for testing"""
    return jsonify(DEMO_HASHES)

@app.route('/code')
def show_code():
    """Display the original code with syntax highlighting"""
    original_code = '''import hashlib

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
    crack_hash(target_hash, wordlist_file)'''
    
    return render_template('code.html', code=original_code)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)