import os
import shutil
from ultralytics import YOLO

def crt_DS(path, dest1, dest2):
    folder = os.listdir(path)

    to_copy_amnt=(round(len(folder)*0.3))
    to_leave_amnt=(round(len(folder)*0.7))


    print(to_leave_amnt)
    to_copy = sorted(folder)[:to_copy_amnt]
    folder = sorted(folder)[to_copy_amnt:]

    if to_copy_amnt % 2 > 0:
        to_appnd=to_copy.pop()
        print(to_appnd)
        folder.append(to_appnd)
        print(sorted(to_copy))
        print("???????????????????????????????????????????????????????????????????????????")
        print(sorted(folder))

    for file in to_copy:
        shutil.move(os.path.join(path, file), dest1)

    for file in folder:
        shutil.move(os.path.join(path, file), dest2)

    print(f"to_train: {len(to_copy)}\nto_validate: {len(folder)}")





if __name__ == "__main__":
    path = "DataSet/src"
    dest1 = "DataSet/train"
    dest2 = "datasets/DataSet/val/"

# Load a model
    model = YOLO("yolov8n.pt")  # pretrained YOLO8n model

    model.train(data="damage.yaml", epochs=50)  # обучите модель
    model.val()  # оцените производительность модели на наборе проверки
    model.predict(source=[dest2+"F_3980.jpeg", dest2+"F_9400.jpeg"])  # предсказать по изображению

# Run batched inference on a list of images
    #results = model([dest2+"F_3980.jpeg", dest2+"F_9400.jpeg"])  # return a list of Results objects

# Process results list
    #for result in results:
    #    boxes = result.boxes  # Boxes object for bounding box outputs
    #    masks = result.masks  # Masks object for segmentation masks outputs
    #    keypoints = result.keypoints  # Keypoints object for pose outputs
    #    probs = result.probs  # Probs object for classification outputs
    #    obb = result.obb  # Oriented boxes object for OBB outputs
    #    result.show()  # display to screen
    #    result.save(filename="ress/result.jpg")  # save to disk

