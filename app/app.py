from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_url():
    url = "https://sql2.niku.co"  # URL مقصد
    app.logger.info("Request initiated to target URL.")
    try:
        # ارسال درخواست به URL مقصد
        response = requests.get(url)
        app.logger.info(f"Response received with status code: {response.status_code}")
        
        if response.status_code == 200:
            app.logger.info("Request successful. Returning predefined string.")
            return "c901884d-10d0-4b98-b5d0-e0d930fd85ad.hsvc.ir,30802"
        else:
            app.logger.error(f"Request failed with status code: {response.status_code}")
            return "Error: Could not fetch data", response.status_code
    except requests.exceptions.RequestException as e:
        app.logger.exception("An exception occurred during the request.")
        return "Error: An unexpected error occurred", 500

if __name__ == '__main__':
    app.logger.info("Starting Flask application...")
    app.run(debug=True, host='0.0.0.0', port=5000)
