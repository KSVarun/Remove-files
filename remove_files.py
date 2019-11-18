import re
import os

dir_path = "/Users/idks/Downloads/[FreeTutorials.Us] Udemy - Full Stack Project Spring Boot 2.0, ReactJS, Redux"
path = os.listdir(dir_path)
for x in path:
    if(x == '.DS_Store'):
        path.remove(x)

for file in path:
    """file_path = os.path.join(dir_path, file)
    with open(file_path, 'r') as file:
        print(file.read())"""

    inside_dir_path = dir_path+"/"+file+"/"
    path2 = os.listdir(inside_dir_path)
    mpfiles = '.*\(.vtt|.srt)'
    #mpfiles_srt = '.*\.srt'

    for file_inside in path2:
        pattern = re.compile(mpfiles)
        matches = pattern.finditer(file_inside)
        # pattern_srt = re.compile(mpfiles_srt)
        # matches_srt = pattern_srt.finditer(file_inside)

        for match in matches:
            str_match = str(match.group(0))
            # print(inside_dir_path+str_match)
            os.remove(inside_dir_path+str_match)

        # for match in matches_srt:
        #     str_match_srt = str(match.group(0))
        #     os.remove(inside_dir_path+str_match_srt)
