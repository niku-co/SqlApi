# استفاده از یک تصویر پایه Python
FROM python:3.9-slim

# تنظیم دایرکتوری کاری
WORKDIR /app

# نصب وابستگی‌ها
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن کد برنامه به داخل کانتینر
COPY . .

# پورت Flask (پورت 5000 در اینجا)
EXPOSE 5000

# اجرای اپلیکیشن Flask
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
