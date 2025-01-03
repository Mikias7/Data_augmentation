import cv2
import numpy as np

def move_right(image):
    
    # Define how much to move the image
    dx = 100  # Move 100 pixels to the right

    # Get the original image dimensions
    height, width = image.shape[:2]

    # Define new dimensions for the canvas
    new_width = width + dx
    new_height = height

    # Create a blank canvas
    new_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Place the original image onto the new canvas
    new_image[0:height, dx:dx + width] = image

    # Display the result
    cv2.imshow("Image Moved Right", new_image)

    return new_image
   

def move_down(image):
    
    # Define how much to move the image
    dy = 100  # Move 100 pixels down

    # Get the original image dimensions
    height, width = image.shape[:2]

    # Define new dimensions for the canvas
    new_width = width
    new_height = height + dy

    # Create a blank canvas
    new_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Place the original image onto the new canvas
    new_image[dy:dy + height, 0:width] = image

    # Display the result
    cv2.imshow("Image Moved Down", new_image)

    return new_image


def move_left(image):
    
    # Define how much to move the image
    dx = 100  # Move 100 pixels to the left

    # Get the original image dimensions
    height, width = image.shape[:2]

    # Define new dimensions for the canvas
    new_width = width + dx
    new_height = height

    # Create a blank canvas
    new_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Place the original image onto the new canvas
    new_image[0:height, 0:width] = image

    # Display the result
    cv2.imshow("Image Moved Left", new_image)

    return new_image
    

def move_up(image):
    
    # Define how much to move the image
    dy = 100  # Move 100 pixels up

    # Get the original image dimensions
    height, width = image.shape[:2]

    # Define new dimensions for the canvas
    new_width = width
    new_height = height + dy

    # Create a blank canvas
    new_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Place the original image onto the new canvas
    new_image[0:height, 0:width] = image

    # Display the result
    cv2.imshow("Image Moved Up", new_image)

    return new_image
  
# Adjust the brightness of the image
def adjust_brightness(image):
    
    # Convert the image to HSV (Hue, Saturation, Value) color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Brightness_value
    brightness_value = 100

    # Split the HSV channels
    h, s, v = cv2.split(hsv_image)

    # Increase or decrease the Value channel to adjust brightness
    v = cv2.add(v, brightness_value)

    # Merge the channels back
    bright_hsv = cv2.merge((h, s, v))

    # Convert back to BGR color space
    bright_image = cv2.cvtColor(bright_hsv, cv2.COLOR_HSV2BGR)

    # Display the brightened image
    cv2.imshow('Brightened Image', bright_image)

    return bright_image

# Darken the image
def darken_image(image):
   
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)
    brightness_decrease = 190  # Decrease brightness by this value
    v = cv2.subtract(v, brightness_decrease)
    dark_hsv = cv2.merge((h, s, v))
    dark_image = cv2.cvtColor(dark_hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow('Darkened Image', dark_image)

    return dark_image

# Add hue
def add_hue(image):
    
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)
    hue_increase = 500  # Increase hue by this value
    h = cv2.add(h, hue_increase)
    hue_hsv = cv2.merge((h, s, v))
    hue_image = cv2.cvtColor(hue_hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow('Hue Added Image', hue_image)

    return hue_image

# Add salt and pepper noise to the image
def salt_and_pepper(image):
    
    # Define noise probabilities
    salt_prob = 0.01  # Probability for salt noise
    pepper_prob = 0.01  # Probability for pepper noise

    # Create a copy of the image
    noisy_image = image.copy()

    # Add salt noise (white pixels)
    num_salt = int(salt_prob * image.size)
    salt_coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[salt_coords[0], salt_coords[1]] = 255

    # Add pepper noise (black pixels)
    num_pepper = int(pepper_prob * image.size)
    pepper_coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy_image[pepper_coords[0], pepper_coords[1]] = 0

    # Display the noisy image
    cv2.imshow("Salt and Pepper Noise", noisy_image)

    return noisy_image

def gaussian_blur(image):
    
    # Apply Gaussian Blur with a kernel size of (5, 5) (you can adjust the kernel size as needed)
    blurred_image = cv2.GaussianBlur(image, (9, 9), 0)

    # Display the blurred image
    cv2.imshow("Gaussian Blur", blurred_image)

    return blurred_image

def invert_color(image):
    # Invert the image
    inverted_image = 100 - image

    return inverted_image