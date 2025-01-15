import logging
from flask import Flask, request
import requests

# تنظیم لاگ
logging.basicConfig(
    filename='app.log',  # نام فایل لاگ
    level=logging.DEBUG,  # سطح لاگ (DEBUG برای ثبت همه موارد)
    format='%(asctime)s [%(levelname)s] %(message)s'  # قالب لاگ
)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_url():
    url = "https://sql2.niku.co"  # URL مقصد
    logging.info(f"Sending request to {url}")  # ثبت شروع درخواست
    
    try:
        response = requests.get(url)  # ارسال درخواست به URL مقصد
        logging.info(f"Received response with status code: {response.status_code}")  # ثبت وضعیت پاسخ
        
        if response.status_code == 200:
            logging.debug("Request successful. Returning predefined string.")  # ثبت لاگ برای موفقیت
            return "c901884d-10d0-4b98-b5d0-e0d930fd85ad.hsvc.ir,30802"
        else:
            logging.error(f"Error response from {url}: Status {response.status_code}")  # ثبت خطا
            return "Error: Could not fetch data", 500
    except Exception as e:
        logging.exception(f"Exception occurred while fetching data: {str(e)}")  # ثبت استثنا
        return "Error: An unexpected error occurred", 500

if __name__ == '__main__':
    logging.info("Starting Flask application...")  # ثبت شروع اپلیکیشن
    app.run(debug=True, host='0.0.0.0', port=5000)  # اجرای Flask روی پورت 5000
