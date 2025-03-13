# Sử dụng image Python 3.10 (bạn có thể thay đổi phiên bản nếu cần)
FROM python:3.10-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy file requirements.txt vào container
COPY requirements.txt .

# Cài đặt các phụ thuộc từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn vào container
COPY . .

# Mở cổng 5000 để Flask có thể lắng nghe
EXPOSE 5000

# Chạy ứng dụng
CMD ["python", "app.py"]