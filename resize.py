import os
import sys
from PIL import Image


def resize_images(directory, target_size):
    """Resize all images in the given directory to the target size."""
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        sys.exit(1)

    # Get a list of files in the directory
    files = [
        f for f in os.listdir(directory) if f.lower().endswith(("png", "jpg", "jpeg"))
    ]

    if not files:
        print("No image files found in the directory.")
        sys.exit(1)

    # Create an output directory
    output_dir = os.path.join(directory, "resized")
    os.makedirs(output_dir, exist_ok=True)

    for file in files:
        input_path = os.path.join(directory, file)
        output_path = os.path.join(output_dir, file)

        try:
            with Image.open(input_path) as img:
                # Resize the image
                img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
                img_resized.save(output_path)
                print(f"Resized and saved: {file}")
        except Exception as e:
            print(f"Error processing {file}: {e}")

    print("All images resized successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    target_size = (320, 180)  # Fixed resolution

    resize_images(directory, target_size)
