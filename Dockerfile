FROM python:3.9-slim

# Ishchi katalog
WORKDIR /app

# System dependencies o‘rnatish
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpq-dev \
    libffi-dev \
    libssl-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt ni nusxalash
COPY requirements.txt /app/

# pip yangilash va kutubxonalarni o‘rnatish
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Kodni konteynerga nusxalash
COPY . /app/

# Port
EXPOSE 8888

# Django serverni ishga tushirish
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8888"]