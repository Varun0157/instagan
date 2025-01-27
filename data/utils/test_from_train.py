import os
import random
import shutil
import sys


def create_test(train_dir: str, test_dir: str, sample_num: int = 50):
    print(train_dir, test_dir, sample_num)

    train_seg_dir = train_dir + "_seg"

    if not os.path.exists(train_dir) or not os.path.exists(train_seg_dir):
        print(
            f"error: directories '{train_dir}' and/or '{train_seg_dir}' do not exist."
        )
        sys.exit(1)

    images = [f for f in os.listdir(train_dir) if f.lower().endswith(".png")]
    # images.sort()

    if len(images) < sample_num:
        print(f"error: (len(images) = {len(images)}) < {sample_num}")
        sys.exit(1)

    selected_images = random.sample(images, sample_num)

    os.makedirs(test_dir, exist_ok=True)
    test_seg_dir = test_dir + "_seg"
    os.makedirs(test_seg_dir, exist_ok=True)

    print(test_dir, test_seg_dir)
    print(len(selected_images))

    for img in selected_images:
        train_img_path = os.path.join(train_dir, img)
        filename, ext = os.path.splitext(img)
        seg_img_path = f"{filename}_0{ext}"
        train_seg_path = os.path.join(train_seg_dir, seg_img_path)

        test_img_path = os.path.join(test_dir, img)
        test_seg_path = os.path.join(test_seg_dir, seg_img_path)

        if os.path.exists(train_img_path) and os.path.exists(seg_img_path):
            shutil.move(train_img_path, test_img_path)
            print(f"{train_img_path} -> {test_img_path}")

            shutil.move(train_seg_path, test_seg_path)
            print(f"{train_seg_path} -> {test_seg_path}")
        else:
            print(
                f"warning: corresponding image {img} not found in both directories. skipping."
            )


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_name>")
        sys.exit(1)

    dataset = sys.argv[1]
    for dir in ["trainA", "trainB"]:
        train_dir = os.path.join(dataset, dir)
        test_dir = os.path.join(dataset, dir.replace("train", "test"))
        create_test(train_dir, test_dir)
