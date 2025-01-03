import cv2 
from image_augmentation import *
from annotation_augmentation import *
from draw_keypoints import draw_keypoints
from get_annotation_keypoints import get_keypoints
from img_dimensions import get_img_dimensions
from get_annotation_keypoints import get_keypoints
from file_processing import *



def shift_right_up_darken():
    
    # Shift Image and annotation right then up and darken image
    shift_right_image = move_right(image)
    shift_right_ann = move_ann_right(keypoints, img_width, img_height, dx)

    shift_up_image = move_up(shift_right_image)
    shift_up_ann = move_ann_up(shift_right_ann, img_width, img_height, dx)

    darkened_img = darken_image(shift_up_image)

    # Blurr image
    blurred_img = gaussian_blur(darkened_img)


    #draw_keypoints(blurred_img, shift_up_ann, img_width, img_width)

    return blurred_img, shift_up_ann


def shift_left_down_brightness():
    # Shift Image and annotation left then down and add brightness to image
    shift_left_image = move_right(image)
    shift_left_ann = move_ann_right(keypoints, img_width, img_height, dx)

    shift_down_image = move_up(shift_left_image)
    shift_down_ann = move_ann_up(shift_left_ann, img_width, img_height, dx)

    add_brightness = adjust_brightness(shift_down_image)

    # Add salt and pepper filter
    noisy_image = salt_and_pepper(add_brightness)

    #modified_img = draw_keypoints(noisy_image, shift_down_ann, img_width, img_width)
    
    # invert image color
    invert_img = invert_color(noisy_image)

    return invert_img, shift_down_ann



all_image_file_path = loop_images()
all_txt_file_path = loop_annotations()


for image_path, annotation_path in zip(all_image_file_path, all_txt_file_path):
    # Load image
    #image_path = ""
    #image = cv2.imread(image_path)
    #print(image_path)
    #print(annotation_path)

    # Load image
    image = cv2.imread(f"image ppath/{image_path}")

    # Load text file
    text_file_path = f"text file path/{annotation_path}"

    raw_keypoints = get_keypoints(text_file_path) # Get keypoints from txt file
    img_width, img_height = get_img_dimensions(f'image path/{image_path}') # Get full image dimensions
    dx = 100

    # Convert annotation key list to int list
    keypoints = get_keypoints(text_file_path)

    final_image, final_annotation = shift_left_down_brightness()
    
    save_img(final_image, image_path)
    save_annotation(text_file_path, annotation_path)

