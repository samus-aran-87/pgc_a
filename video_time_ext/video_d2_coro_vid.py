#!/usr/bin/python3

# chmod +x {name}.py - права на выполнения

import os
import subprocess
from datetime import timedelta

def init(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return wrapper

def find_files(next_coroutine):
    for root, subfolders, files in os.walk(os.getcwd()):
        for file in files:
            next_coroutine.send(os.path.join(root, file))
    next_coroutine.close()

@init
def filter_videos(next_coroutine):
    video_ext = ['mp4', 'avi']

    try:
        while True:
            filename = yield
            ext = filename.split('.')[-1]
            if ext in video_ext:
                next_coroutine.send(filename)
    except GeneratorExit:
        next_coroutine.close()

@init
def get_video_duration(next_coroutine):
    try:
        while True:
            filename = yield
            filename = filename.replace(" ", "\ ")
            cmd = 'ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0"'.format(filename)
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT, universal_newlines=True) #shell=True !!! shell=False
            stdout, stderr = p.communicate()
            next_coroutine.send({'filename':filename, 'duration':int(float(stdout))})
    except GeneratorExit:
        next_coroutine.close()

@init
def duration_printer(next_coroutine):
    try:
        while True:
            video_data = yield
            filename = video_data['filename'].split('/')[-1] # не для windows
            # os.path.basename(path)
            # pathlib
            duration = video_data['duration']
            print(filename, str(timedelta(seconds=duration)))
            next_coroutine.send(duration)
    except GeneratorExit:
        next_coroutine.close()

@init
def get_total_duration():
    total = 0
    try:
        duration = yield
        total += duration
    except GeneratorExit:
        print("Total duration", str(timedelta(seconds=total))

def pipline():
    total_duration = get_total_duration()
    printer = duration_printer(total_duration)
    video_duration = get_video_duration(printer)
    videos = filter_videos(video_duration)
    find_files(videos)


if __name__ == "__main__":
    pipline()