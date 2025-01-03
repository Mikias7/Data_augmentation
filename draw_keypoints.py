import cv2


def draw_keypoints(image, all_keypoints, img_width, img_height):
    class_idx = all_keypoints[0]
    x = all_keypoints[1]
    y = all_keypoints[2]
    width = all_keypoints[3]
    height = all_keypoints[4]

    keypoints = [[all_keypoints[5], all_keypoints[6]], 
             [all_keypoints[7], all_keypoints[8]],
             [all_keypoints[9], all_keypoints[10]], 
             [all_keypoints[11], all_keypoints[12]],
             [all_keypoints[13], all_keypoints[14]], 
             [all_keypoints[15], all_keypoints[16]]]

    if image is None:
        print("Error: Image not found. Check the path.")
        exit()

    # Get image dimensions
    img_height, img_width = image.shape[:2]

    # Draw bounding box
    top_left = (int((x - width / 2) * img_width), int((y - height / 2) * img_height))
    bottom_right = (int((x + width / 2) * img_width), int((y + height / 2) * img_height))
    cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 2)

    # Draw keypoints
    for i, (px, py) in enumerate(keypoints, 1):
        center = (int(px * img_width), int(py * img_height))
        cv2.circle(image, center, 5, (0, 255, 0), -1)  # Green circles
        cv2.putText(image, f"P{i}", center, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    return image
    # Display the image
    #cv2.imshow("Keypoints", image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
