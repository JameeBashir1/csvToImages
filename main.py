import csv
import os
from PIL import Image

# Read values from CSV file
values = []
with open('HL29.csv', 'r') as f:
  reader = csv.reader(f)
  for row in reader:
    values.append(float(row[0]))

# Determine dimensions of image
width = 20
height = 20

# Create the images folder if it doesn't exist
if not os.path.exists('images'):
  os.makedirs('images')

# Create image and assign values to pixels
for i in range(0, len(values), 200):
  # Create image and assign values to pixels
  image = Image.new('RGB', (width, height))
  pixels = image.load()

  # Find minimum and maximum values
  min_value = min(values[i:i+400])
  max_value = max(values[i:i+400])

  for x in range(width):
    for y in range(height):
      # Map values to pixel intensities and assign to RGB channels
      value = values[x + y * width + i]
      intensity = int((value - min_value) / (max_value - min_value) * 255)
      pixels[x, y] = (intensity, intensity, intensity)

  # Save image
  image_number = i // 200 + 1
  image.save(os.path.join('images', 'image_{}.jpg'.format(image_number)))

