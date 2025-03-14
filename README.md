# 🖼️ Image Overlay Tool

This Python script adds a semi-transparent overlay to all `.jpg` images in the folder where the script is executed. The modified images are saved in a separate folder called **`with_overlay`**.

## 🚀 How to Use
1. Install the required library:
   ```
   pip install pillow
   ```
## 2.Place the script in the folder with your .jpg images.

## 3.Run the script:
   ```
   python script_name.py
   ```
## 4.The modified images will be saved in a newly created with_overlay folder.

## 5.🎯 Features
✅ Automatically processes all .jpg files in the current folder.<br>
✅ Creates a with_overlay folder if it doesn't exist.
✅ Handles corrupted or unsupported files gracefully.
✅ Provides clear feedback for each processed file.

## 6.⚙️ Customization
To change the overlay color, modify this line in the script:
```
def add_overlay(image_path, output_path, color=(52, 55, 75, 191)):  # RGBA format
```
The color format is (R, G, B, Alpha), where Alpha controls transparency (191 = ~75% opacity).

## 7. 🖼️ Example Output
✅ Overlay added to: with_overlay/image1_with_overlay.jpg
✅ Overlay added to: with_overlay/image2_with_overlay.jpg
✅ All overlays added successfully. Files saved in 'with_overlay'.
