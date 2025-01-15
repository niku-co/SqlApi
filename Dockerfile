# استفاده از تصویر پایه پایتون
FROM python:3.10-slim

# نصب وابستگی‌های سیستم عامل و ابزارهای مورد نیاز
RUN apt-get update && apt-get install -y \
    libpq-dev \
    unixodbc-dev \
    curl \
    wget \
    apt-transport-https \
    && apt-get clean

# نصب Microsoft ODBC Driver 17
RUN wget https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/m/msodbcsql17/msodbcsql17_17.10.1.1-1_amd64.deb && \
    dpkg -i msodbcsql17_17.10.1.1-1_amd64.deb && \
    rm msodbcsql17_17.10.1.1-1_amd64.deb && \
    ln -s /opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.10.so.1.1 /opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.so && \
    echo "export LD_LIBRARY_PATH=/opt/microsoft/msodbcsql17/lib64:\$LD_LIBRARY_PATH" >> /etc/environment

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن فایل‌های پروژه به داخل تصویر
COPY . .

# نصب وابستگی‌های پایتون
RUN pip install --no-cache-dir -r requirements.txt

# اجرای برنامه
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
