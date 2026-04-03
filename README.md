# [LAB 1] - API NHẬN DIỆN THỰC ĐƠN (OCR)

---

# 1. Thông tin sinh viên

* **Họ và tên:** Võ Gia Phúc
* **MSSV:** 24120413
* **Lớp:** 24CTT3 - Tư Duy Tính Toán
* **Trường:** Đại học Khoa học Tự nhiên - ĐHQG HCM

---

# 2. Mô hình Hugging Face

* **Tên mô hình:** TrOCR (small-sized model, fine-tuned on SROIE)

* **Liên kết:** [TrOCR](https://huggingface.co/microsoft/trocr-small-printed)

* **Mô tả:**
  Hệ thống cho phép người dùng tải lên hình ảnh một dòng văn bản từ thực đơn và tự động chuyển đổi thành dữ liệu văn bản số (**String**) thông qua kiến trúc **Transformer**.

---

# 3. Hướng dẫn cài đặt và chạy chương trình

## Bước 1: Clone repository

```bash
git clone <repository_link>
cd <project_folder>
```

## Bước 2: Cài đặt các thư viện cần thiết

```bash
pip install -r requirements.txt
```

## Bước 3: Khởi động Server

Mở Terminal tại thư mục gốc của dự án và chạy lệnh:

```bash
python main.py
```

Hoặc sử dụng uvicorn:

```bash
uvicorn main:app --reload
```

Server sẽ mặc định chạy tại địa chỉ:

```
http://127.0.0.1:8000
```

---

# 4. Giao diện Swagger UI

Truy cập giao diện tài liệu API tại:

```
http://127.0.0.1:8000/docs
```

Swagger UI cho phép:

* Kiểm tra các endpoint
* Upload hình ảnh trực tiếp
* Test API nhanh chóng

---

# 5. Hướng dẫn gọi API

## Endpoint 1: GET /

### Chức năng

Trả về thông tin giới thiệu ngắn gọn về hệ thống

### Ví dụ Response

```json
{
  "message": "Menu OCR API is running"
}
```

---

## Endpoint 2: GET /health

### Chức năng

Kiểm tra trạng thái hoạt động của hệ thống

### Ví dụ Response

```json
{
  "status": "OK"
}
```

---

## Endpoint 3: POST /predict

### Chức năng

Nhận hình ảnh từ người dùng, gọi mô hình Hugging Face và trả kết quả nhận diện

### Input

* File hình ảnh (.jpg, .png, .jpeg,...)

### Ví dụ Request

Upload file ảnh thông qua Swagger UI hoặc gửi request bằng Postman

### Ví dụ Response

```json
{
  "prediction": "Cơm gà xối mỡ - 35.000đ"
}
```

---

# 6. Video Demo

Video minh họa quá trình:

* Cấu trúc source code
* Cách chạy chương trình
* Demo thực tế

## [YouTube](https://youtu.be/L7bnfCdnFuo)

## [Google Drive](https://drive.google.com/file/d/1glEq0xH0sOV1dpV03IjsrgQqAyUnsQ1B/view?usp=sharing) (Link dự phòng)

---

# 7. Công nghệ sử dụng

* Python
* FastAPI
* Hugging Face Transformers
* TrOCR Model
* Uvicorn

---

# 8. Cấu trúc thư mục

```
.
├── main.py
├── test_api.py
├── requirements.txt
├── README.md
├── data
│   └── menu1.png
│   └── menu2.png
```

---

# 9. Quy trình hoạt động hệ thống

1. Người dùng upload ảnh thực đơn
2. API nhận ảnh từ request
3. Ảnh được xử lý bằng mô hình TrOCR
4. Mô hình trả về văn bản
5. API trả kết quả JSON cho người dùng

---

# 10. Ghi chú

* API được xây dựng phục vụ mục đích học tập
* Có thể mở rộng nhận diện nhiều dòng văn bản
* Có thể tích hợp giao diện frontend sau này
* Có thể deploy lên cloud (Render, Railway, HuggingFace Spaces)

---

# 11. Tác giả

**Võ Gia Phúc**
Sinh viên Đại học Khoa học Tự nhiên - ĐHQG HCM
Lớp 24CTT3 - Tư Duy Tính Toán

---

# 12. Lab Information

**Tên Lab:** LAB 1 - API Nhận Diện Thực Đơn OCR
**Môn học:** Tư Duy Tính Toán
**Giảng viên thực hành:** Lê Đức Khoan

---

⭐ **Hoàn thành LAB 1 - API OCR bằng Hugging Face TrOCR**
