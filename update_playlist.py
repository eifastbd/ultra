import urllib.request

SOURCE = "https://raw.githubusercontent.com/sm-monirulislam/Toffee-Auto-Update/refs/heads/main/toffee_playlist.m3u"
OUTPUT = "zisan.m3u"

req = urllib.request.Request(
    SOURCE,
    headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(req, timeout=60) as response:
    data = response.read()

with open(OUTPUT, "wb") as f:
    f.write(data)

print("zisan.m3u updated successfully.")
