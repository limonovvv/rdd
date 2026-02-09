import os
from autodistill_grounding_dino import GroundingDINO
from autodistill.detection import CaptionOntology

# 1. Настройка путей
# Используем r'' перед строкой, чтобы Windows-пути с косой чертой не выдавали ошибку
INPUT_DIR = r"C:\Users\limon\Downloads\rdd\DataSet\train\images"
OUTPUT_DIR = r"C:\Users\limon\Downloads\rdd\DataSet\labeled_signboards"

# 2. Описываем нейронке, что именно искать на фото
ontology = CaptionOntology({
    "shop signboard": "signboard",    # основные вывески
    "advertising banner": "signboard" # рекламные баннеры
})

# 3. Загружаем "умную" модель
print("Загрузка модели Grounding DINO... (может занять время при первом запуске)")
base_model = GroundingDINO(ontology=ontology)

# 4. Запуск процесса разметки
print(f"Начинаю разметку изображений в {INPUT_DIR}...")
base_model.label(
    input_folder=INPUT_DIR, 
    extension=".jpg", 
    output_folder=OUTPUT_DIR
)

print(f"Готово! Размеченный датасет (картинки + txt файлы) лежит тут: {OUTPUT_DIR}")