import os
import sys
from typing import Tuple
from PIL import Image


def clean_subdir(
    src_dir: str, target_dir: str, target_size: Tuple[int, int], seg: bool
):
    if not os.path.exists(src_dir):
        print(f"error: dir '{src_dir}' does not exist.")
        sys.exit(1)

    files = [f for f in os.listdir(src_dir) if f.lower().endswith(".png")]
    if not files:
        print("no image files found in the directory.")
        sys.exit(1)

    os.makedirs(target_dir, exist_ok=True)

    for in_file in files:
        input_path = os.path.join(src_dir, in_file)
        base_name, ext = os.path.splitext(in_file)

        #out_file = f"{int(base_name):04d}"
        out_file = base_name.zfill(4) 
        
        if seg:
            out_file += "_0"
        out_file += ext
        output_path = os.path.join(target_dir, out_file)

        try:
            with Image.open(input_path) as img:
                out = img.resize(target_size, Image.Resampling.LANCZOS)
                if seg:
                    out = out.convert("L")

                out.save(output_path)
                print(f"resized and saved: {in_file} -> {out_file}")
        except Exception as e:
            print(f"error processing {in_file}: {e}")


def clean_dataset(
    src_dir: str, target_dir: str, target_size: Tuple[int, int] = (320, 180)
):
    if not os.path.exists(src_dir):
        print("source directory does not exist")
        sys.exit(1)

    os.makedirs(target_dir, exist_ok=True)

    img_dirs = ["trainA", "trainB"]
    seg_dirs = ["trainA_seg", "trainB_seg"]

    for subdir in img_dirs + seg_dirs:
        clean_subdir(
            os.path.join(src_dir, subdir),
            os.path.join(target_dir, subdir),
            target_size,
            subdir in seg_dirs,
        )
        print("*" * 5 + f" done processing {subdir} " + "*" * 5)
        print()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: python prep-images.py <source_dir> <target_dir>")
        sys.exit(1)

    src_dir, target_dir = sys.argv[1], sys.argv[2]
    clean_dataset(src_dir, target_dir)
