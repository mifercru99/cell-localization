import subprocess

def get_codecs():
    cmd = "ffmpeg -codecs"
    x = subprocess.check_output(cmd, shell=True)
    x = x.split(b'\n')
    for e in x:
        print (e)

get_codecs()
