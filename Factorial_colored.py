import sys
from PIL import Image
import math as m

sys.setrecursionlimit(1000005)
sys.set_int_max_str_digits(1000000)

def fibonacci(num):
    return sum(fib(num))

def fib(num):
    if num <= 1:
        return [0, 1]
    
    output = fib(num - 1)
    return [output[1],(output[0] + output[1])]


def convert_to_base(num, base, base_mult):
    output = list()
    base = int(base / base_mult)
    while num >= 1:
        if base_mult == 1:
            output.append(num % base)
            num = m.floor(num // base)
        elif base_mult == 3:
            r = num % base
            num = m.floor(num // base)
            g = num % base
            num = m.floor(num // base)
            b = num % base
            num = m.floor(num // base)
            output.append((r, g, b))
    return output

def pixel_len(num, base):
    i =0
    while num >= 1:
        num = m.floor(num // base)
        i += 1
    return i

if __name__ == "__main__":
    base_mult = 1
    gray = 2 ** 8 # set base_mult to 1 and set the string in Image.new to 'L'
    rgb = base_mult *(2 ** 8) # set base_mult to 3 and set the string in Image.new to 'RGB'
    
    print('1')
    base = gray # change this to the scale you want to visualize the Fibonacci sequence in
    f = fibonacci(10000) # change the number in this to the Fibonacci number to solve for
    fi = pixel_len(f, base)
    width = m.floor(fi ** (1/2))
    height = m.ceil(fi / width)
    img = Image.new('L',(width,height)) # change this string to whatever base you want the image to be in
    pixels = convert_to_base(f, base, base_mult)

    print('2')
    w,h = 0,0
    for p in pixels:
        img.putpixel((w,h),p)
        w += 1
        if w >= width:
            w = 0
            h += 1

    print('3')
    img.show()