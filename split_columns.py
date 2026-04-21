# split_columns.py
# Updated for Windows / current folder usage
# Place this file inside:
# C:\Users\ABDUL\Downloads\rrb-project

from PIL import Image
import os

# =====================================
# SETTINGS
# =====================================

# Current folder
project_folder = "."

# Divider shift (adjust if text cuts)
divider_offset = 10

# Supported image types
valid_ext = (".png", ".jpg", ".jpeg")

# =====================================
# PROCESS ALL CHAPTERS
# =====================================

chapters = sorted(os.listdir(project_folder))

for chapter in chapters:

    chapter_path = os.path.join(project_folder, chapter)

    # only folders like part01, part02
    if os.path.isdir(chapter_path) and chapter.lower().startswith("part"):

        input_folder = os.path.join(chapter_path, "images")
        output_folder = os.path.join(chapter_path, "columns")

        # skip if no images folder
        if not os.path.exists(input_folder):
            continue

        os.makedirs(output_folder, exist_ok=True)

        print(f"\n📘 Processing {chapter}")

        files = sorted(os.listdir(input_folder))

        for file in files:

            if file.lower().endswith(valid_ext):

                file_path = os.path.join(input_folder, file)

                try:
                    img = Image.open(file_path)

                    width, height = img.size

                    # split center
                    mid = width // 2 + divider_offset

                    # crop columns
                    left = img.crop((0, 0, mid, height))
                    right = img.crop((mid, 0, width, height))

                    base = os.path.splitext(file)[0]

                    left_path = os.path.join(
                        output_folder,
                        f"{base}_left.png"
                    )

                    right_path = os.path.join(
                        output_folder,
                        f"{base}_right.png"
                    )

                    left.save(left_path)
                    right.save(right_path)

                    print(f"   ✅ {file}")

                except Exception as e:
                    print(f"   ❌ Error in {file}: {e}")

print("\n🎉 All chapter images split successfully!")