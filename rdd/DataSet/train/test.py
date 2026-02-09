import os
from ultralytics import YOLO
from PIL import Image

# 1. Авто-настройка путей: скрипт сам поймет, где он находится
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

# 2. Укажите названия ваших файлов
MODEL_PATH = 'yolov8n (2).pt'
IMAGE_PATH = 'img_0156.jpg' # Убедитесь, что название совпадает до буквы

def run_detection():
    # Проверка: есть ли файлы на месте?
    if not os.path.exists(MODEL_PATH):
        print(f"Ошибка: Файл модели '{MODEL_PATH}' не найден в {BASE_DIR}")
        return
    if not os.path.exists(IMAGE_PATH):
        print(f"Ошибка: Файл картинки '{IMAGE_PATH}' не найден в {BASE_DIR}")
        return

    print("Загрузка модели и обработка...")
    
    # 3. Загружаем модель
    model = YOLO(MODEL_PATH)

    # 4. Делаем предсказание
    # save=True сохранит фото в папку runs/detect/predict
    results = model.predict(source=IMAGE_PATH, save=True, imgsz=640, conf=0.25)

    # 5. Показываем результат сразу на экране
    for r in results:
        # Это откроет стандартное приложение для просмотра фото с результатом
        im_array = r.plot()  # Рисует рамки на изображении
        im = Image.fromarray(im_array[..., ::-1])  # Конвертирует цвета для корректного отображения
        im.show()
        
        # Печатаем в консоль, где именно сохранился файл
        print(f"Готово! Результат сохранен в папку: {r.save_dir}")

if __name__ == "__main__":
    run_detection()