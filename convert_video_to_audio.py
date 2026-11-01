# Convert the videos to mp3
import os
import subprocess
files = os.listdir("videos")

for file in files:
  # print(file)
  tutorial_num = file.split("_")[1].split(".")[0]
  file_name = file.split("_")[0]
  file_name = file_name.replace("-","_").lower()
  # print(tutorial_num,file_name)
  subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_num}_{file_name}.mp3"])