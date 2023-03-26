import requests #for request handling 
import time
from tqdm import tqdm #animation loader
import math 


url = 'http://staff.ltam.lu/feljc/software/python/python_basics.pdf'
#stream = true does downloading of data in chunks
r = requests.get(url, stream = True)
chunk_size = 256

#headers is header that is  context of message part , we required content length in order to download

size =int( r.headers['Content-Length']) 

n = math.ceil(size/chunk_size)

with open("file.pdf","wb") as file:
    for chunk in tqdm(r.iter_content(chunk_size = chunk_size),total =n):
        time.sleep(0.5)
        file.write(chunk)




