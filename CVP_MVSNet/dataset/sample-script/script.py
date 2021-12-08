# sample script to get Cameras -> cam.txt, Rectified -> respective images for our data. Need images and poses in the directory. 

# get time_stamps with difference more than 1

from pathlib import Path
from scipy.spatial.transform import Rotation as R
# Path("path/to/current/file.foo").rename("path/to/new/destination/for/file.foo")

current_time = []
image_count = 1

with open('images.txt', 'r') as f:
    for each in f.readlines():
        
        current = each.split()[0].strip()
        get_image = False

        if not current_time:
            current_time.append(current)
            get_image = True

        elif float(current) - float(current_time[-1]) >= 1:
            current_time.append(current)
            get_image = True

# get images and save images for respective timestamp
        if get_image:
            image_file_path = each.split()[1].strip()
            Path(image_file_path).rename("scan1/rect_" + f"{image_count:03}" + "_3_r5000.png")
            image_count += 1

# mapper contains closet timestamp from poses.txt for each image timestamp
mapper = {}
camera_count = 0

for each in current_time:
    rotations = []
    translations = []

    with open('poses.txt', 'r') as f:
        for line in f.readlines():
            current = line.split()[0].strip()

            if each in mapper and (abs(float(current) - float(each)) < abs(float(mapper[each]) - float(each))):
                mapper[each] = current
                rotations = [float(each) for each in line.split()[1:5]]
                translations = [float(each) for each in line.strip().split()[5:]]
            elif each not in mapper:
                mapper[each] = current
                rotations = [float(each) for each in line.split()[1:5]]
                translations = [float(each) for each in line.strip().split()[5:]]
    # get camera parameters for mapper[each] and save as desired .txt files
    
    with open("Cameras/" + f"{camera_count:08}" + "_cam.txt", 'a+') as file:
        file.write('extrinsic' + '\n')
        r = R.from_quat([rotations])
        rotation = r.as_matrix()
        rotation = r.as_matrix()[0]
       
        file.write(str(rotation[0][0]) + " " + str(rotation[0][1]) + " " + str(rotation[0][2]) + " " + str(1000.0 * translations[0]) +"\n")
        file.write(str(rotation[1][0]) + " " + str(rotation[1][1]) + " " + str(rotation[1][2]) + " " + str(1000.0 * translations[1]) +"\n")
        file.write(str(rotation[2][0]) + " " + str(rotation[2][1]) + " " + str(rotation[2][2]) + " " + str(1000.0 * translations[2]) +"\n")
        file.write("0.0 0.0 0.0 1.0\n")
        file.write("\n")
        file.write("intrinsic\n")
        file.write("226.38018519795807 0.0 173.6470807871759\n")
        file.write("0.0 226.15002947047415 133.73271487507847\n")
        file.write("0.0 0.0 1.0\n")
        file.write("\n")
        file.write("1.0 0.05")
    camera_count += 1

