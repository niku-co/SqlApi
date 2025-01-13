# استفاده از تصویر پایه پایتون
FROM python:3.10-slim

# نصب وابستگی‌های سیستم عامل
RUN apt-get update && apt-get install -y \
    libpq-dev \
    unixodbc-dev \
    && apt-get clean

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن فایل‌های پروژه به داخل تصویر
COPY . .

# نصب وابستگی‌های پایتون
RUN pip install --no-cache-dir -r requirements.txt

# اجرای برنامه
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
