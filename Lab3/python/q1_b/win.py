import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-p1" , "--path1" , help="path 1")
parser.add_argument("-p2" , "--path2" , help="path 2")
args=parser.parse_args()

urls = []
file = open(args.path1,"r")
while True:
    line = file.readline()
    if not line:
        break
    url = line.split("/")[2].strip()
    print(url)
    fullurl = line.strip()
    urls = urls + [fullurl]
file.close()

cnt = 0
file = open(args.path2, "r")
while True:
    line = file.readline()
    if not line:
        break
    url = line.split("||")[-1].strip()
    uid = line.split("||")[0].strip()
    if(url==""):
        url = line.split("||")[-2].strip()
    # print(uid,url)
    if url in [x[8:] for x in urls]:
        print(f"user_name - {uid} : Winner - Lucky draw!!! - https://{url}")
        cnt += 1
    elif url in [x[12:] for x in urls]:
        print(f"user_name - {uid} : Winner - Lucky draw!!! - https://www.{url}")
        cnt += 1
    elif url in urls:
        print(f"user_name - {uid} : Winner - Lucky draw!!! - {url}")
        cnt += 1
print(cnt)
file.close()
