


# Move annotation keypoints to the right
def move_ann_right(keypoints, img_width, img_height,dx):
    n = dx/ (img_width + dx)
    m = img_width/ (img_width + dx)

    #n = 100/641
    #m = 541/641

    new_keypoints = keypoints.copy()

    new_keypoints[1] = new_keypoints[1] * m + n
    new_keypoints[3] = new_keypoints[3] * m
    new_keypoints[5] = new_keypoints[5] * m + n
    new_keypoints[7] = new_keypoints[7] * m + n
    new_keypoints[9] = new_keypoints[9] * m + n
    new_keypoints[11] = new_keypoints[11] * m + n
    new_keypoints[13] = new_keypoints[13] * m + n
    new_keypoints[15] = new_keypoints[15] * m + n


    return new_keypoints

# Move annotation keypoint to the left 
def move_ann_left(keypoints, img_width, img_height,dx):
    l = img_width / (img_width + dx)
   
    new_keypoints = keypoints.copy()

    new_keypoints[1] = new_keypoints[1] * l
    new_keypoints[3] = new_keypoints[3] * l
    new_keypoints[5] = new_keypoints[5] * l
    new_keypoints[7] = new_keypoints[7] * l
    new_keypoints[9] = new_keypoints[9] * l
    new_keypoints[11] = new_keypoints[11] * l
    new_keypoints[13] = new_keypoints[13] * l
    new_keypoints[15] = new_keypoints[15] * l

  
    return new_keypoints

# Move annotation keypoint down
def move_ann_down(keypoints, img_width, img_height,dy):
    n = dy/ (img_height + dy)
    m = img_height/ (img_height + dy)

    #n = 100/641
    #m = 541/641

    new_keypoints = keypoints.copy()

    new_keypoints[2] = new_keypoints[2] * m + n
    new_keypoints[4] = new_keypoints[4] * m
    new_keypoints[6] = new_keypoints[6] * m + n
    new_keypoints[8] = new_keypoints[8] * m + n
    new_keypoints[10] = new_keypoints[10] * m + n
    new_keypoints[12] = new_keypoints[12] * m + n
    new_keypoints[14] = new_keypoints[14] * m + n
    new_keypoints[16] = new_keypoints[16] * m + n

    return new_keypoints


# Move annotation keypoint up
def move_ann_up(keypoints, img_width, img_height,dy):
    l = img_width / (img_width + dy)
  
    new_keypoints = keypoints.copy()

    new_keypoints[2] = new_keypoints[2] * l
    new_keypoints[4] = new_keypoints[4] * l
    new_keypoints[6] = new_keypoints[6] * l
    new_keypoints[8] = new_keypoints[8] * l
    new_keypoints[10] = new_keypoints[10] * l
    new_keypoints[12] = new_keypoints[12] * l
    new_keypoints[14] = new_keypoints[14] * l
    new_keypoints[16] = new_keypoints[16] * l

    return new_keypoints