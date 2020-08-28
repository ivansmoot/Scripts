import glob
import sh
import os

zips = sorted(glob.glob('./*.zip'))

for zip in zips:
    name = zip[2:-4]
    sh.unzip(zip)
    print(f"名字是{name}")
    # sh.zip(f"{name}zip.zip", "./*.videofx", "./*.lic")
    videofx_full_name = ""
    lic_full_name = ""
    pic_full_name = ""
    for root, dirs, files in os.walk("./"):
        for file in files:
            if os.path.splitext(file)[-1] == '.videofx':
                videofx_full_name = os.path.split(file)[1]
            if os.path.splitext(file)[-1] == '.lic':
                lic_full_name = os.path.split(file)[1]
            if os.path.splitext(file)[-1] == '.png':
                pic_full_name = os.path.split(file)[1]
            elif os.path.splitext(file)[-1] == '.jpg':
                pic_full_name = os.path.split(file)[1]
    print(videofx_full_name)
    print(lic_full_name)
    print(pic_full_name)
    sh.zip(f"{name}zip.zip", videofx_full_name, lic_full_name)
    sh.rm("-rf", lic_full_name)
    sh.rm("-rf", videofx_full_name)
    sh.rm("-rf", zip)
    sh.zip(f"{zip}", pic_full_name, f"{name}zip.zip")
    sh.rm("-rf", pic_full_name)
    sh.rm("-rf", f"{name}zip.zip")
