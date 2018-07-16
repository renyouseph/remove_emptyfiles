### Requirements ###
# apt-get update
# apt-get install python3
###

import os

path = '/root/python/files'
for CurDir,SubDir,SubFiles in os.walk('/root/python/files'):
    for files in SubFiles:
        abPath = os.path.join(CurDir,files)
        if os.path.getsize(abPath) == 0:
            os.unlink(abPath)
