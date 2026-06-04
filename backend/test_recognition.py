from deepface import DeepFace

result = DeepFace.find(
    img_path="dataset/srijan/78.jpg",
    db_path="dataset",
    model_name="Facenet512",
    enforce_detection=False
)

print(result[0].head(10))