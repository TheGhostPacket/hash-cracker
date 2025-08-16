# 🌐 Hash Cracker Web Portfolio

Educational web interface for the Hash Cracker project - deployed on Render.

## 🚀 Live Demo

**[https://hash-education-portfolio.onrender.com](https://hash-education-portfolio.onrender.com)**

## 🏗️ Local Development

### Prerequisites
- Python 3.9+
- pip package manager

### Setup
```bash
# Navigate to web portfolio directory
cd web-portfolio

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit `http://localhost:5000` to see the application.

## 📁 File Structure

```
web-portfolio/
├── app.py                 # Flask application backend
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main web interface
└── README.md             # This file
```

## 🚀 Deployment to Render

### Step 1: Prepare Repository
Make sure your repository has this web-portfolio folder with all the required files.

### Step 2: Connect to Render
1. Go to [render.com](https://render.com) and sign up/log in
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Select the repository containing this web-portfolio folder

### Step 3: Configure Settings
```
Name: hash-education-portfolio
Environment: Python 3
Root Directory: web-portfolio
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Instance Type: Free
```

### Step 4: Deploy
Click "Create Web Service" and wait for deployment to complete.

## 🔧 Environment Variables

For production deployment, you may want to set:
```
FLASK_ENV=production
PORT=10000  # Auto-configured by Render
```

## 🎯 Features

- **Interactive Hash Generator** - Real-time hash creation with multiple algorithms
- **Demo Cracking Simulation** - Safe educational hash cracking demonstrations
- **Educational Content** - Comprehensive lessons on password security
- **Professional Design** - Clean, responsive interface perfect for portfolios
- **Safe Operation** - Limited to educational demos only

## 🛡️ Security Features

- **Demo-Only Hashes** - Only works with predefined educational examples
- **No File Uploads** - Prevents misuse with real password lists
- **Input Validation** - Proper sanitization of all user inputs
- **Educational Focus** - Clear disclaimers and educational content

## 🔍 API Endpoints

### `POST /generate_hash`
Generate hash for given text and algorithm.

**Request:**
```json
{
  "text": "password123",
  "algorithm": "sha256"
}
```

**Response:**
```json
{
  "text": "password123",
  "algorithm": "SHA256",
  "hash": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f",
  "length": 64
}
```

### `POST /demo_crack`
Attempt to crack a demo hash.

**Request:**
```json
{
  "hash": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
  "algorithm": "sha256"
}
```

**Response:**
```json
{
  "success": true,
  "password": "password",
  "attempts": 1,
  "time_taken": 0.023,
  "rate": 43,
  "algorithm": "SHA256"
}
```

## 🎓 Educational Value

This web interface demonstrates:
- Modern web development with Flask
- RESTful API design
- Responsive frontend development
- Cloud deployment practices
- Cybersecurity education through interactive tools

## ⚠️ Important Notes

- This is an educational demonstration only
- Only works with predefined demo hashes for safety
- Not intended for real password cracking
- Designed to teach security concepts responsibly

## 🔄 Updates and Maintenance

To update the deployed application:
1. Make changes to the code
2. Commit and push to GitHub
3. Render will automatically redeploy

## 📞 Support

For deployment issues or questions about the web interface, refer to:
- [Render Documentation](https://render.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- Main project README in the parent directory
