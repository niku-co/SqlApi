from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_url():
    # تغییر URL به https://sql2.niku.co
    url = "https://sql2.niku.co"  # URL جدید
    response = requests.get(url)
    
    if response.status_code == 200:
        # به جای ارسال response.text، پارامتر دلخواه خود را برمی‌گردانیم
        return "c901884d-10d0-4b98-b5d0-e0d930fd85ad.hsvc.ir,30802"  # خروجی دلخواه شما
    else:
        return "Error: Could not fetch data", 500

if __name__ == '__main__':
    app.run(debug=True)
