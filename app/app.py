import logging
from flask import Flask, Response
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
            logging.debug(f"Response content: {response.text[:100]}...")  # ثبت بخشی از محتوای پاسخ
            return Response(response.content, status=response.status_code, content_type=response.headers['Content-Type'])
        else:
            logging.error(f"Error response from {url}: Status {response.status_code}")
            return Response(f"Error: Unable to fetch data from {url}", status=response.status_code)
    except Exception as e:
        logging.exception(f"Exception occurred while fetching data from {url}: {str(e)}")  # ثبت استثنا
        return Response(f"Error: {str(e)}", status=500)

if __name__ == '__main__':
    logging.info("Starting Flask application...")  # ثبت شروع اپلیکیشن
    app.run(debug=True, host='0.0.0.0', port=5000)  # اجرای Flask روی پورت 5000
