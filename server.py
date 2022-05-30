import subprocess
class stream_source:
    def __init__(self,url,quality="best",port=16384):
        self.subp=subprocess.Popen(f"streamlink {url} {quality} --player-external-http --player-external-http-port {port}",shell=True)
        self.port=port
    def __del__(self):
        self.subp.kill()
    def geturl(self):
        return f"http://127.0.0.1:{self.port}"
if __name__=="__main__":
    testurl="https://live.bilibili.com/81004"
    rc=stream_source(url=testurl)
    print(f"Test Server Start, url {testurl}, address {rc.geturl()}")
    while True:
        pass
