from PIL import Image, ImageOps, ImageEnhance
import sys
inp, out = sys.argv[1], sys.argv[2]
im = Image.open(inp).convert('RGB')
im = ImageOps.fit(im, (100, 53), method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
g = ImageOps.grayscale(im)
g = ImageEnhance.Contrast(g).enhance(1.35)
g = ImageEnhance.Brightness(g).enhance(1.05)
g.save(out)
print(out)
