from deepfake_image_detection import predict

# Set the path of the image to analyze
image_path = "/storage/emulated/0/Pictures/test_image.jpg"  # Adjust path for Pydroid

try:
    result = predict(image_path)
    print("Detection Result:", result)
except Exception as e:
    print("Error:", e)