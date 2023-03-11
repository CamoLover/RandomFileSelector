import glob,random,os

format = ["*.mp4","*.jpg","*.png","*.jpeg","*.webm","*.avi"]

files = glob.glob(format[0])
for i in range(len(format)):
    files.extend(glob.glob(format[i]))

file = random.choice(files)

print ("Opening file %s..." % file)
os.system("rundll32 url.dll,FileProtocolHandler \"" + file + "\"")