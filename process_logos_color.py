from rembg import remove
from PIL import Image
import os

os.makedirs('assets/logos_color', exist_ok=True)
input_dir = 'logos'
output_dir = 'assets/logos_color'

for fname in os.listdir(input_dir):
    try:
        img_path = os.path.join(input_dir, fname)
        img = Image.open(img_path)
        
        # Remove background using rembg
        out_img = remove(img)
        
        # Convert to RGBA just in case
        out_img = out_img.convert("RGBA")
        
        # Crop to the exact bounding box of the non-transparent pixels
        bbox = out_img.getbbox()
        if bbox:
            out_img = out_img.crop(bbox)
        
        # Resize to max height 88px to maintain sharp quality 
        # (CSS will display them at 44px)
        max_height = 88 
        ratio = max_height / float(out_img.height)
        new_width = int(float(out_img.width) * float(ratio))
        out_img = out_img.resize((new_width, max_height), Image.Resampling.LANCZOS)
        
        out_name = os.path.splitext(fname)[0] + ".png"
        out_img.save(os.path.join(output_dir, out_name), "PNG")
        print(f"Processed {fname}")
        
    except Exception as e:
        print(f"Error processing {fname}: {e}")
