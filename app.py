from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'LUKE S. BALILI BSIT SYSTEM INTEGRATION SEMI-FINALS'