import requests
import os

# Đường dẫn API
URL = "http://127.0.0.1:8000/predict"

def test_ocr(image_path):
    if not os.path.exists(image_path):
        print(f"[ERROR] Không tìm thấy file tại: {image_path}")
        return

    print(f"--- Đang gửi file: {image_path} ---")
    try:
        with open(image_path, "rb") as f:
            files = {"file": (os.path.basename(image_path), f, "image/jpeg")}
            response = requests.post(URL, files=files)
            
        if response.status_code == 200:
            print("KẾT QUẢ:", response.json())
        else:
            print(f"LỖI {response.status_code}: {response.text}")
    except Exception as e:
        print(f"LỖI KẾT NỐI: {e}")

if __name__ == "__main__":
    # Thay đổi đường dẫn này cho khớp với file của bạn
    test_ocr("data/menu1.png")