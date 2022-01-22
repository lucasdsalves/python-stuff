from captcha.image import ImageCaptcha
import string
import random

# Create an image instance of the given size
image = ImageCaptcha(width = 280, height = 90)
 
# Image captcha text with random text
captcha_text = ''.join(random.choice(string.ascii_letters) for i in range(10)) 
 
# Generate the image of the given text
data = image.generate(captcha_text) 
 
# Write the image on the given file and save it
image.write(captcha_text, 'CAPTCHA.png')