import colorsys
import re

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color):
    return '#{:02x}{:02x}{:02x}'.format(*rgb_color)

def hsl_to_rgb(hsl_color):
    hue, saturation, lightness = hsl_color
    r, g, b = colorsys.hls_to_rgb(hue / 360.0, lightness, saturation)
    return round(r * 255), round(g * 255), round(b * 255)

def rgb_to_hsl(rgb_color):
    r, g, b = rgb_color
    h, l, s = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
    return round(h * 360), s, l

def increase_saturation(hsl_color, increase_amount):
    hue, saturation, lightness = hsl_color
    new_saturation = min(1, saturation + increase_amount)
    return (hue, new_saturation, lightness)
def increase_contrast(hsl_color, increase_amount):
    hue, saturation, lightness = hsl_color
    new_lightness = max(0, min(1, lightness + increase_amount))
    return (hue, saturation, new_lightness)
def modify_color_hex(hex_color, increase_amount):
    rgb_color = hex_to_rgb(hex_color)
    hsl_color = rgb_to_hsl(rgb_color)
    modified_hsl_color = increase_saturation(hsl_color, increase_amount)
    #modified_hsl_color = increase_contrast(hsl_color, increase_amount)
    modified_rgb_color = hsl_to_rgb(modified_hsl_color)
    modified_hex_color = rgb_to_hex(modified_rgb_color)
    return modified_hex_color

# Example usage:
#original_hex_color = "#56b6c2"
increase_amount = 0.1
#modified_hex_color = modify_color_hex(original_hex_color, increase_amount)

with open("test.json", "rb+") as f:
    while True:
        char = f.read(1).decode("utf-8")

        if char == "#":
            orig_color = f.read(6).decode("utf-8")
            try:
                new_color = modify_color_hex(orig_color, increase_amount).lstrip("#")
                f.seek(f.tell()-6)
                f.write(new_color.encode("utf-8"))
                print(orig_color,new_color)
            except:
                pass