import os
import sys


def append_zero_to_pngs(directory):
    """Append '_0' to the filenames of all .png files in the given directory."""
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        sys.exit(1)

    # Get all .png files in the directory
    png_files = [f for f in os.listdir(directory) if f.lower().endswith(".png")]

    if not png_files:
        print("No .png files found in the directory.")
        sys.exit(1)

    for file in png_files:
        old_path = os.path.join(directory, file)
        filename, ext = os.path.splitext(file)
        new_filename = f"{filename}_0{ext}"
        new_path = os.path.join(directory, new_filename)

        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {file} -> {new_filename}")
        except Exception as e:
            print(f"Error renaming {file}: {e}")

    print("All .png files renamed successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    append_zero_to_pngs(directory)
