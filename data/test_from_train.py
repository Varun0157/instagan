import os
import random
import shutil
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_name>")
        sys.exit(1)

    base_dir = sys.argv[1]
    base_seg_dir = f"{base_dir}_seg"

    # Check if the directories exist
    if not os.path.exists(base_dir) or not os.path.exists(base_seg_dir):
        print(f"Error: Directories '{base_dir}' and/or '{base_seg_dir}' do not exist.")
        sys.exit(1)

    # Get the list of image files (assumes files are named 1.png, 2.png, etc.)
    images = [f for f in os.listdir(base_dir) if f.endswith(".png") and f.isdigit()]
    images.sort(key=lambda x: int(os.path.splitext(x)[0]))  # Sort numerically

    if len(images) < 50:
        print("Error: Not enough images to select 50 random files.")
        sys.exit(1)

    # Select 50 random images
    selected_images = random.sample(images, 50)

    # Create new directories if they do not exist
    new_dir = os.path.join(base_dir, "new")
    new_seg_dir = os.path.join(base_seg_dir, "new_seg")
    os.makedirs(new_dir, exist_ok=True)
    os.makedirs(new_seg_dir, exist_ok=True)

    # Move the selected images to the new directories
    for img in selected_images:
        base_img_path = os.path.join(base_dir, img)
        seg_img_path = os.path.join(base_seg_dir, img)

        new_img_path = os.path.join(new_dir, img)
        new_seg_img_path = os.path.join(new_seg_dir, img)

        if os.path.exists(base_img_path) and os.path.exists(seg_img_path):
            shutil.move(base_img_path, new_img_path)
            shutil.move(seg_img_path, new_seg_img_path)
        else:
            print(
                f"Warning: Corresponding image '{img}' not found in both directories. Skipping."
            )

    print("Random images moved successfully.")


if __name__ == "__main__":
    main()
