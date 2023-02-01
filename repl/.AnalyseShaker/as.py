import shutil
import threading
import uuid

from selenium import webdriver
import os
import time
import sys


def autoRun():
  global i
  pwd = ""
  try:
    while True:
      pwd = os.path.join(os.path.join(os.getcwd(), "temp"), str(uuid.uuid4()))
      os.mkdir(pwd)
      print(f"--user-data-dir={str(pwd)}")
      op = options
      op.add_argument(f"--user-data-dir={str(pwd)}")
      driver = webdriver.Chrome(options=op)
      with open(f"{os.getcwd()}/temp/as/stealth.min.js") as f:
        js = f.read()
      driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                             {"source": js})
      driver.get(url)
      time.sleep(delay)
      driver.quit()
      shutil.rmtree(pwd)
      print(f"成功执行了{str(i)}次")
      i += 1
  except Exception as e:
    print(e)
    while True:
      try:
        shutil.rmtree(pwd)
        break
      except:
        time.sleep(0.5)
        continue
    print(f"发生错误：{pwd}")
    time.sleep(0.5)
    autoRun()


# 读取配置
url = sys.argv[1]
threads = int(sys.argv[2])
delay = int(sys.argv[3])
sourceDir = sys.argv[4]
os.chdir(sourceDir)
print(f"设置运行目录：{sourceDir}")

print("配置读取完毕，开始运行")

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-infobars')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('lang=zh_CN.utf-8')
options.add_argument(
  'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
)
i = 1
threadPool = []

for x in range(0, threads):
  t = threading.Thread(target=autoRun)
  threadPool.append(t)
  t.start()

for t in threadPool:
  t.join()

print("运行结束")
