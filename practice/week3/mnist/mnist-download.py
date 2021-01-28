import urllib.request as req
import gzip, os, os.path

savepath = "./mnist" # current directoty path
baseurl = "http://yann.lecun.com/exdb/mnist"
files = [
    "train-images-idx3-ubyte.gz",
    "train-labels-idx1-ubyte.gz",
    "t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz"]

if not os.path.exists(savepath):
    os.mkdir(savepath) # make directory

# download
for f in files:
    # "aaaa" + "/" + "bbb" => aaaa/bbb
    url = baseurl + "/" + f
    # location
    loc = savepath + "/" + f
    print("download:", url) # donwloading
    if not os.path.exists(loc):
        req.urlretrieve(url, loc)

# unzip
for f in files:
    gz_file = savepath + "/" + f # path
    raw_file = savepath + "/" + f.replace(".gz", "") # path
    print("gzip:", f)
    
    # gz -> gzip; zip -> unzip
    # rb -> read back
    with gzip.open(gz_file, "rb") as fp:
        body = fp.read()
        # wb -> write back
        with open(raw_file, "wb") as w:
            w.write(body)
print("ok")