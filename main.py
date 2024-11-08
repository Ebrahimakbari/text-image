import numpy as np
from PIL import Image

def text_to_matrix(text):
    # مرحله 1 و 2: تبدیل متن به مقادیر 0 تا 255 و تبدیل به ماتریس مربعی
    mapped_numbers = [ord(char) % 256 for char in text]
    size = int(np.ceil(len(mapped_numbers)**0.5))
    matrix = np.zeros((size, size), dtype=int)
    matrix.flat[:len(mapped_numbers)] = mapped_numbers
    return matrix

def normalize_rows(matrix):
    # نرمال‌سازی مقادیر هر سطر به طور جداگانه
    normalized_matrix = np.zeros_like(matrix, dtype=np.uint8)
    for i, row in enumerate(matrix):
        min_val, max_val = row.min(), row.max()
        if max_val > min_val:  # جلوگیری از تقسیم بر صفر
            normalized_matrix[i] = ((row - min_val) / (max_val - min_val) * 255).astype(np.uint8)
        else:
            normalized_matrix[i] = 0  # اگر همه مقادیر برابر باشند
    return normalized_matrix

def enlarge_matrix(matrix, block_size=10):
    # بزرگ‌نمایی ماتریس برای هر بلوک 6x6
    return np.kron(matrix, np.ones((block_size, block_size), dtype=np.uint8))

# مثال استفاده
input_text = "Adventure, a journey unfolds. Mountain, of rivers flow. Cascade, a soft breeze. Sunshine, in stars dance, a beautiful journey,and so on."



print(len(input_text))
# اجرای مراحل
matrix = text_to_matrix(input_text)
print(matrix)
normalized_matrix = normalize_rows(matrix)
print(normalized_matrix)
image_matrix = enlarge_matrix(normalized_matrix)

# ایجاد و ذخیره تصویر
final_image = Image.fromarray(image_matrix, mode='L')
final_image.save("normalized_peak_matrix_image.png")