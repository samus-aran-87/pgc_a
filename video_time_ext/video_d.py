#!usr/bin/python3

import os
import subprocess
from datetime import timedelta


video_ext = ['mp4', 'avi']

def get_videos():
    videos = []
    for root, subfolders, files in os.walk(os.getcwd()):
        for file in files:
            if file.split(".")[-1] in video_ext:
                videos.append(os.path.join(root,file))
    return videos

def get_ffprobe_output(filename):
    filename = filename.replace(" ", "\ ")
    cmd = 'ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0"'.format(filename)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, 
    stderr=subprocess.STDOUT, universal_newlines=True) #shell=True !!! shell=False
    # output = p.stdout.read().decode().strip()
    # print(output)
    stdout, stderr = p.communicate()
    return int(float(stdout))

def sec_to_str(s):
    return str(timedelta(seconds=s))

def main():
    videos = get_videos()
    total_duration = 0

    for v in videos:
        duration = get_ffprobe_output(v)

        print(v.split('/')[-1], 'Duration:', sec_to_str(duration))
        total_duration += duration
    
    print()
    print("Total duration", sec_to_str(total_duration))

if __name__ == "__main__":
    main()