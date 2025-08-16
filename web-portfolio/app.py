from flask import Flask, render_template, request, jsonify
import hashlib
import os
import time
import re
import math

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

def analyze_password_strength(password):
    """Comprehensive password strength analysis"""
    
    score = 0
    feedback = []
    
    # Length scoring
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
        feedback.append("Consider using 12+ characters for better security")
    else:
        score += 5
        feedback.append("Password too short - use at least 8 characters")
    
    # Character variety
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    char_types = sum([has_lower, has_upper, has_digit, has_special])
    score += char_types * 15
    
    if not has_lower:
        feedback.append("Add lowercase letters")
    if not has_upper:
        feedback.append("Add uppercase letters")
    if not has_digit:
        feedback.append("Add numbers")
    if not has_special:
        feedback.append("Add special characters (!@#$%^&*)")
    
    # Common patterns (negative scoring)
    common_patterns = [
        r'123', r'abc', r'password', r'admin', r'qwerty',
        r'111', r'000', r'aaa'
    ]
    
    for pattern in common_patterns:
        if re.search(pattern, password.lower()):
            score -= 10
            feedback.append(f"Avoid common patterns like '{pattern}'")
    
    # Sequential characters
    if re.search(r'(012|123|234|345|456|567|678|789|890)', password):
        score -= 10
        feedback.append("Avoid sequential numbers")
    
    if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password.lower()):
        score -= 10
        feedback.append("Avoid sequential letters")
    
    # Repeated characters
    if re.search(r'(.)\1{2,}', password):
        score -= 10
        feedback.append("Avoid repeating characters")
    
    # Calculate entropy
    charset_size = 0
    if has_lower: charset_size += 26
    if has_upper: charset_size += 26
    if has_digit: charset_size += 10
    if has_special: charset_size += 32
    
    entropy = len(password) * math.log2(charset_size) if charset_size > 0 else 0
    
    # Time to crack estimation (simplified)
    attempts_per_second = 1000000000  # 1 billion per second (modern GPU)
    combinations = charset_size ** len(password) if charset_size > 0 else 1
    seconds_to_crack = combinations / (2 * attempts_per_second)  # Average case
    
    # Convert to human readable time
    if seconds_to_crack < 1:
        crack_time = "Instantly"
    elif seconds_to_crack < 60:
        crack_time = f"{seconds_to_crack:.1f} seconds"
    elif seconds_to_crack < 3600:
        crack_time = f"{seconds_to_crack/60:.1f} minutes"
    elif seconds_to_crack < 86400:
        crack_time = f"{seconds_to_crack/3600:.1f} hours"
    elif seconds_to_crack < 31536000:
        crack_time = f"{seconds_to_crack/86400:.1f} days"
    else:
        crack_time = f"{seconds_to_crack/31536000:.1f} years"
    
    # Determine strength level
    if score >= 80:
        strength = "Very Strong"
        color = "#27ae60"
    elif score >= 60:
        strength = "Strong" 
        color = "#2ecc71"
    elif score >= 40:
        strength = "Moderate"
        color = "#f39c12"
    elif score >= 20:
        strength = "Weak"
        color = "#e67e22"
    else:
        strength = "Very Weak"
        color = "#e74c3c"
    
    return {
        'score': min(100, max(0, score)),
        'strength': strength,
        'color': color,
        'entropy': round(entropy, 1),
        'crack_time': crack_time,
        'feedback': feedback[:3],  # Limit to top 3 suggestions
        'has_lower': has_lower,
        'has_upper': has_upper,
        'has_digit': has_digit,
        'has_special': has_special,
        'length': len(password)
    }

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

@app.route('/analyze_password', methods=['POST'])
def analyze_password():
    """Analyze password strength endpoint"""
    data = request.json
    password = data.get('password', '')
    
    if not password:
        return jsonify({'error': 'No password provided'})
    
    analysis = analyze_password_strength(password)
    return jsonify(analysis)

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

@app.route('/compare_algorithms', methods=['POST'])
def compare_algorithms():
    """Compare multiple hash algorithms"""
    data = request.json
    text = data.get('text', '')
    algorithms = data.get('algorithms', [])
    
    if not text:
        return jsonify({'error': 'No text provided'})
    
    if not algorithms:
        return jsonify({'error': 'No algorithms specified'})
    
    results = {}
    
    for algorithm in algorithms:
        try:
            start_time = time.time()
            
            if algorithm == 'sha256':
                hash_result = hashlib.sha256(text.encode()).hexdigest()
            elif algorithm == 'md5':
                hash_result = hashlib.md5(text.encode()).hexdigest()
            elif algorithm == 'sha1':
                hash_result = hashlib.sha1(text.encode()).hexdigest()
            elif algorithm == 'sha512':
                hash_result = hashlib.sha512(text.encode()).hexdigest()
            else:
                continue
            
            end_time = time.time()
            processing_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            results[algorithm] = {
                'hash': hash_result,
                'length': len(hash_result),
                'time_ms': round(processing_time, 2),
                'algorithm': algorithm.upper()
            }
            
        except Exception as e:
            results[algorithm] = {'error': str(e)}
    
    return jsonify(results)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
