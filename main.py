from fastapi import FastAPI, UploadFile, File, HTTPException
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import io

app = FastAPI(title="FoOdyssey OCR API")

# Load mô hình và processor từ Hugging Face (microsoft/trocr-small-printed)
# Trong lần chạy đầu tiên, script sẽ tự động tải model về cache
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-small-printed")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-small-printed")

@app.get("/")
async def root():
    """FoOdyssey - Smart Travel & Gastronomy"""
    return {
        "project": "FoOdyssey - Smart Travel & Gastronomy",
        "function": "OCR Menu Recognition using TrOCR",
        "description": "API này hỗ trợ trích xuất văn bản in từ hình ảnh menu món ăn."
    }

@app.get("/health")
async def health():
    """Kiểm tra trạng thái hoạt động của hệ thống [cite: 39]"""
    return {"status": "healthy", "model": "microsoft/trocr-small-printed"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """Nhận hình ảnh và trả về văn bản nhận diện được dưới dạng JSON [cite: 40, 43]"""
    # Kiểm tra định dạng file đầu vào [cite: 44, 45]
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File tải lên phải là hình ảnh!")
    
    try:
        # Đọc dữ liệu ảnh
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        
        # Tiền xử lý và dự đoán bằng mô hình TrOCR
        pixel_values = processor(images=image, return_tensors="pt").pixel_values
        generated_ids = model.generate(pixel_values)
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        
        return {
            "filename": file.filename,
            "prediction": generated_text,
            "status": "success"
        }
    except Exception as e:
        # Xử lý lỗi trong quá trình suy luận [cite: 45]
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)