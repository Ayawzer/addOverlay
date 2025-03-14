from PIL import Image, UnidentifiedImageError
import os
from pathlib import Path

def add_overlay(image_path, output_path, color=(52, 55, 75, 191)):
    try:
        with Image.open(image_path) as image:
            overlay = Image.new('RGBA', image.size, color)
            image_with_overlay = Image.alpha_composite(image.convert('RGBA'), overlay)
            image_with_overlay_rgb = image_with_overlay.convert('RGB')
            image_with_overlay_rgb.save(output_path)
            print(f"✅ Overlay added to: {output_path}")
    except UnidentifiedImageError:
        print(f"❌ Unable to open image: {image_path}")
    except Exception as e:
        print(f"❌ Error processing {image_path}: {e}")

def process_images_in_directory(directory='.'):
    # Folder do zapisu wyników
    output_dir = Path(directory) / 'with_overlay'
    output_dir.mkdir(exist_ok=True)  # Tworzy folder jeśli nie istnieje

    input_files = list(Path(directory).glob('*.jpg'))
    
    if not input_files:
        print("⚠️ No .jpg files found in the directory.")
        return

    for input_file in input_files:
        output_file = output_dir / f"{input_file.stem}_with_overlay.jpg"
        add_overlay(input_file, output_file)

    print(f"✅ All overlays added successfully. Files saved in '{output_dir}'.")

if __name__ == "__main__":
    process_images_in_directory()
