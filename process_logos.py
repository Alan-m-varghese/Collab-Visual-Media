from PIL import Image
import os

os.makedirs('assets/logos', exist_ok=True)
input_dir = 'logos'
output_dir = 'assets/logos'

for fname in os.listdir(input_dir):
    try:
        img_path = os.path.join(input_dir, fname)
        img = Image.open(img_path).convert("RGBA")
        
        corners = [
            img.getpixel((0, 0)),
            img.getpixel((img.width - 1, 0)),
            img.getpixel((0, img.height - 1)),
            img.getpixel((img.width - 1, img.height - 1))
        ]
        
        bg_is_white = sum(1 for c in corners if c[0]>240 and c[1]>240 and c[2]>240 and c[3]>240) >= 3
        
        data = img.getdata()
        new_data = []
        for item in data:
            r, g, b, a = item
            if bg_is_white:
                l = (0.299 * r + 0.587 * g + 0.114 * b)
                new_a = int((255 - l) * (a / 255.0))
                new_data.append((255, 255, 255, new_a))
            else:
                # If it's a dark logo with transparent background, we might have black pixels with alpha.
                # If we just change to white, the aliased edge (which might be dark) will be white, which is good.
                new_data.append((255, 255, 255, a))
                
        img.putdata(new_data)
        
        max_height = 88 
        ratio = max_height / float(img.height)
        new_width = int(float(img.width) * float(ratio))
        # Use simple resize if you don't have LANCZOS, but PIL usually does
        img = img.resize((new_width, max_height), Image.Resampling.LANCZOS)
        
        out_name = os.path.splitext(fname)[0] + ".png"
        img.save(os.path.join(output_dir, out_name), "PNG")
        print(f"Processed {fname}")
    except Exception as e:
        print(f"Error processing {fname}: {e}")
