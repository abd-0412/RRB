import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

project_folder = "."
valid_ext = (".png", ".jpg", ".jpeg")

items = sorted(os.listdir(project_folder))

for chapter in items:

    chapter_path = os.path.join(project_folder, chapter)

    if os.path.isdir(chapter_path) and chapter.lower() == "part 4":

        input_folder = os.path.join(chapter_path, "columns")
        output_file = os.path.join(chapter_path, "raw_text.txt")

        if not os.path.exists(input_folder):
            continue

        files = sorted(os.listdir(input_folder))

        if not files:
            continue

        print(f"\n[Chapter] Processing {chapter}")

        all_text = ""

        for file in files:

            if file.lower().endswith(valid_ext):

                img_path = os.path.join(input_folder, file)

                img = Image.open(img_path)

                text = pytesseract.image_to_string(
                    img,
                    config='--psm 6'
                )

                all_text += f"\n\n===== {file} =====\n{text}"

                print(f"   + {file}")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(all_text)

        print(f"Saved: {output_file}")

print("\nAll chapters OCR completed!")