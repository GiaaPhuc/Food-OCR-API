# [LAB 1] - API NHẬN DIỆN THỰC ĐƠN (OCR)

## 1. Thông tin sinh viên

- **Họ và tên:** Võ Gia Phúc
- **MSSV:** 24120413
- **Lớp:** 24CTT3 - Tư Duy Tính Toán
- **Trường:** Đại học Khoa học Tự nhiên - ĐHQG HCM

## 2. Mô hình Hugging Face

- **Tên mô hình:** TrOCR (Transformer-based Optical Character Recognition)
- **Liên kết:** [Hugging Face TrOCR](https://huggingface.co/microsoft/trocr-small-printed)
- **Mô tả:** Hệ thống cho phép người dùng tải lên hình ảnh một dòng văn bản từ thực đơn và tự động chuyển đổi thành dữ liệu văn bản số (String) thông qua kiến trúc Transformer.

## 3. Hướng dẫn cài đặt và chạy chương trình

1. Clone repository về máy.
2. Cài đặt các thư viện cần thiết:
   ```bash
   pip install -r requirements.txt
   ```
3. Khởi động Server:
   Mở Terminal tại thư mục gốc của dự án và chạy lệnh:
   ```bash
   python main.py
   ```
   Hoặc sử dụng uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

   Server sẽ mặc định chạy tại địa chỉ: http://127.0.0.1:8000.

4. Truy cập Giao diện Tài liệu (Swagger UI):
   Mở trình duyệt và truy cập đường dẫn http://127.0.0.1:8000/docs để kiểm tra các endpoint trực quan.

5. Hướng dẫn gọi API và Ví dụ Request/Response
   Endpoint 1: GET /
      Chức năng: Trả về thông tin giới thiệu ngắn gọn về hệ thống.
   Endpoint 2: GET /health
      Chức năng: Kiểm tra trạng thái hoạt động của hệ thống.
   Endpoint 3: POST /predict
      Chức năng: Nhận hình ảnh từ người dùng, gọi mô hình Hugging Face và trả kết quả nhận diện.
      Dữ liệu đầu vào: File hình ảnh (định dạng .jpg, .png,...).

6. Liên kết Video Demo 
   Video minh họa quá trình chạy chương trình, cấu trúc source code và thử nghiệm thực tế:
      Xem trên YouTube: [YouTube](https://youtu.be/L7bnfCdnFuo)
      Link dự phòng (Google Drive): [Google Drive](https://drive.google.com/file/d/1glEq0xH0sOV1dpV03IjsrgQqAyUnsQ1B/view?usp=sharing)
