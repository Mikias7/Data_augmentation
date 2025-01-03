
def get_keypoints(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        
        # Split each line by spaces
        word_list = [line.split() for line in lines]

        # Change the string values to float 
        keypoint_list = [float(keypoint) for keypoint in word_list[0]]
        return keypoint_list

