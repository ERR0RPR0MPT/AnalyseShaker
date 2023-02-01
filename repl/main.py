import os
import shutil
import time
import requests

remoteLink = "https://ashaker.fuckgyz.eu.org"


def get(url):
  try:
    requests.get(url, timeout=10)
  except:
    print(f"{url}保活失败")


print("移动文件...")
pwd = os.path.join(os.getcwd(), "temp")
os.system(f"rm -rf {pwd}")
os.system("ps -ef | grep nginx | grep -v grep | awk '{print $2}' | xargs kill")
os.system("ps -ef | grep as.py | grep -v grep | awk '{print $2}' | xargs kill")
os.system("ps -ef | grep asrun | grep -v grep | awk '{print $2}' | xargs kill")
os.system("rm -rf /home/runner/nginx")
os.mkdir(pwd)
shutil.copytree(f"{os.getcwd()}/.AnalyseShaker", f"{pwd}/as")
shutil.copytree(f"{os.getcwd()}/.nginx", "/home/runner/nginx")
os.system(f"chmod a+x -R {pwd}/as")
os.system("chmod a+x -R /home/runner/nginx/sbin")
os.system(f"{pwd}/as/asrun {remoteLink} {os.getcwd()} &")
print("开始运行...")
os.system("/home/runner/nginx/sbin/nginx -g 'daemon off;' &")
print("开始自保活...")
link = "https://" + os.getenv("REPL_SLUG") + "." + os.getenv(
  "REPL_OWNER") + ".repl.co"
while True:
  get(link)
  print("成功保活")
  time.sleep(10)
