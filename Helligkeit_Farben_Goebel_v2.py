# Samuel Goebel
# Munich, 12.11.2025

# Coding Assignemnt VISPIRON SYSTEMS: "Farben Hexadecmimals Helligkeit"

#Goal:
# script selects the brightest color from a list of color values and output 
# the red, green and blue components individually. 

# Bonus: Name the brightest color ('https://www.csscolorsapi.com/')



# -----------------------------------------------------------------------------
# Context:


# (r,g,b) format --> '(0,0,0)'
# hex format --> '#RRGGBB'

# decimals         hexvalues
# 0 - 9             0 - 9
# 10                A
# 11                B
# 12                C
# 13                D
# 14                E
# 15                F



# RGB decimal number N ranges: 0 <= N <= 255
# Convert Hex into RGB

# Hex numbers are based around power of 16

# Hex #RRGGBB: [1-3] corresponds to red, [3-5] to green, [5-7] to blue

# rgb decimal function:
#  N = (First Hex digit * 16**1) + (Second Hex digit * 16**0)

# e.g. hex red = #FF0000
# N[1-3] = (15 * 16 ) + (15 * 1) = 240 + 15 = 255
# N[3-5] = ... = 0
# N[5-7] = ... = 0
# 'hex #FF0000' == 'rgb (255, 0, 0)'

# -----------------------------------------------------------------------------
# bonus context:
#  calculate (r,g,b) brighness:

# Formula: sqrt(0.241 R**2 + 0.691 G**2 + 0.068 B**2)

# -----------------------------------------------------------------------------


import math
import requests 

# To install 'requests' in your active environment (e.g., your Conda 'base'):
# >>> pip install requests


'''Converting hex to rgb Function'''
def hex_to_rgb(hex_code):
    if not isinstance(hex_code, str):
        return None
    if not hex_code.startswith("#"):
        return None
    if len(hex_code) != 7:  
        return None

    try:
        r = int(hex_code[1:3], 16) # int(value, base); hexadecimals use base 16
        g = int(hex_code[3:5], 16)
        b = int(hex_code[5:7], 16)
        return r, g, b
    except ValueError:
        return None


'''Brightness Function'''
def brightness(r, g, b):
    return math.sqrt(0.241 * r**2 + 0.691 * g**2 + 0.068 * b**2)


'''Fetch all 148 colors from the api; api wont accept hex code input'''
def get_color_name(hex_code):
    try:
        url = "https://www.csscolorsapi.com/api/colors"
        response = requests.get(url, timeout=5)
        data = response.json()

        colors = data.get("colors", [])
        hex_clean = hex_code.lstrip('#').lower()

        for color in colors:
            api_hex = color["hex"].lower()
            if api_hex == hex_clean:
                return color["name"]

        return "Unknown"

    except Exception as e:
        print(f"Error fetching color name: {e}")
        return "Unknown"


"""Find the brightest color from a list"""
def find_brightest_color(colors):

    brightest_color = None
    max_brightness = -1

    for hex_code in colors:
        rgb = hex_to_rgb(hex_code)
        if rgb is None:
            print(f"Skipping invalid color: {hex_code}")
            continue

        r, g, b = rgb
        bright = brightness(r, g, b)
        if bright > max_brightness:
            max_brightness = bright
            brightest_color = (hex_code, r, g, b)

    return brightest_color


# ---- Test the script ----
if __name__ == "__main__":
    # Test cases
    # colors = ['#FFFFFF']
    # colors = ['#000000']
    # colors = ['#FFFFFF', '#000000']
    # colors = ['42']
    # colors = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]
    colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFFFF']

    brightest = find_brightest_color(colors)

    if brightest is None:
        print("No valid colors found — please check your list.")
    else:
        hex_code, r, g, b = brightest
        name = get_color_name(hex_code)
        print(f"The brightest color is: {hex_code} (r={r}, g={g}, b={b}), called '{name}'")