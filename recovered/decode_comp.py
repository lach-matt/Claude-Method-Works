import base64, hashlib, json
p = "/mnt/user-data/tool_results/Google_Drive_download_file_content_toolu_01FuTTCUSiCKhjVxBx5NvByC.json"
obj = json.load(open(p))
if isinstance(obj, list):
    content = json.loads(obj[0]['text'])['content']
else:
    content = obj['content']
data = base64.b64decode(content, validate=True)
open("BUILD60_compendia.md","wb").write(data)
print("md5:", hashlib.md5(data).hexdigest())
print("bytes:", len(data))
print("lines:", data.count(b"\n"))