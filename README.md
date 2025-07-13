# 🛡️ Secure Online Banking System with AI-Based Fraud Detection

A modern web-based online banking system built with **Python, Flask, and Machine Learning** to ensure secure transactions and detect fraud in real-time.

---

## 📌 Key Features

-  User registration and login with hashed passwords
-  Fraud detection using a trained ML model (Random Forest/XGBoost)
-  Money transfers with real-time fraud risk scoring
-  Transaction dashboards with interactive charts
-  Downloadable transaction reports in PDF format
-  Admin panel to view users and monitor fraud alerts
-  Optional email/SMS notifications via Flask-Mail/Twilio

---

##  Project Structure

```bash
secure-banking-ai/
│
├── app/
│   ├── __init__.py               # Flask app initialization
│   ├── routes.py                 # All route definitions (views)
│   ├── templates/                # HTML templates (Jinja2)
│   │   ├── base.html
│   │   └── dashboard.html
│   ├── static/                   # CSS, JS, image files
│   │   ├── css/
│   │   ├── js/
│   ├── models/                   # Database models (User, Transactions)
│   │   └── models.py
│   ├── ml/
│   │   └── fraud_detector.pkl    # Pre-trained fraud detection model
│   └── utils/
│       └── pdf_generator.py      # PDF generation logic
│
├── config.py                     # App configuration (DB URI, secret key)
├── run.py                        # Main entry point to start the Flask app
├── requirements.txt              # Python dependencies
├── README.md                     # Project overview (this file)
└── .gitignore                    # Ignore venv, __pycache__, etc.
