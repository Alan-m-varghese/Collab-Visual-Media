from PIL import Image, ImageChops
import os

os.makedirs('assets/logos_cropped', exist_ok=True)
input_dir = 'logos'
output_dir = 'assets/logos_cropped'

def trim(im):
    if im.mode == 'RGBA':
        alpha = im.getchannel('A')
        bbox = alpha.getbbox()
        if bbox:
            return im.crop(bbox)
        return im
    else:
        # Solid background - assuming top-left pixel is bg
        bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
        diff = ImageChops.difference(im, bg)
        if diff.mode != 'L':
            diff = diff.convert('L')
        # Filter out noise
        diff = diff.point(lambda p: 255 if p > 10 else 0)
        bbox = diff.getbbox()
        if bbox:
            # add a tiny 2px padding so it doesn't touch edges completely
            l, t, r, b = bbox
            l = max(0, l-2)
            t = max(0, t-2)
            r = min(im.width, r+2)
            b = min(im.height, b+2)
            return im.crop((l, t, r, b))
        return im

for fname in os.listdir(input_dir):
    try:
        img_path = os.path.join(input_dir, fname)
        img = Image.open(img_path)
        
        if img.mode == 'P':
            if 'transparency' in img.info:
                img = img.convert('RGBA')
            else:
                img = img.convert('RGB')
        elif img.mode not in ('RGB', 'RGBA'):
            img = img.convert('RGBA')
                
        img_cropped = trim(img)
        
        out_name = fname
        if out_name.lower().endswith(('.jpg', '.jpeg')):
            img_cropped = img_cropped.convert('RGB')
            img_cropped.save(os.path.join(output_dir, out_name), quality=100)
        else:
            img_cropped.save(os.path.join(output_dir, out_name))
            
        print(f"Cropped {fname}")
    except Exception as e:
        print(f"Error {fname}: {e}")
