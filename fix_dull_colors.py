from PIL import Image
import colorsys
import os

os.makedirs('assets/logos_color_bright', exist_ok=True)
input_dir = 'assets/logos_color'
output_dir = 'assets/logos_color_bright'

for fname in os.listdir(input_dir):
    try:
        img_path = os.path.join(input_dir, fname)
        img = Image.open(img_path).convert('RGBA')
        
        data = img.getdata()
        new_data = []
        for item in data:
            r, g, b, a = item
            if a > 0:
                h, s, v = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
                
                # 1. Boost Value (Brightness) for dark pixels
                if v < 0.85:
                    v = 0.95 - (v * 0.11) # Map V to the 0.85-0.95 range smoothly
                    r_f, g_f, b_f = colorsys.hsv_to_rgb(h, s, v)
                    r, g, b = int(r_f*255), int(g_f*255), int(b_f*255)
                
                # 2. Guarantee Luminance (so dark blues/reds don't disappear)
                Y = 0.299 * r + 0.587 * g + 0.114 * b
                if Y < 140:
                    blend = (140 - Y) / 140.0
                    r = int(r + (255 - r) * blend)
                    g = int(g + (255 - g) * blend)
                    b = int(b + (255 - b) * blend)
                
                new_data.append((r, g, b, a))
            else:
                new_data.append((r, g, b, a))
                
        img.putdata(new_data)
        out_name = os.path.splitext(fname)[0] + '.png'
        img.save(os.path.join(output_dir, out_name), 'PNG')
        print(f'Processed {fname}')
    except Exception as e:
        print(f'Error processing {fname}: {e}')
