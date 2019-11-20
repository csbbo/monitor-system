#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib
import os
import settings


def getFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.sha256()
    with open(filename, 'rb') as f:
        ifile = f.read()
        myhash.update(ifile)
    if myhash.hexdigest() == None:
        return 'None'
    return myhash.hexdigest()
def getFileHash():
    # The value of sha_256 is None if the path does not exist
    checkfiles = settings.SHA256_FILE
    file_list = []
    for filepath in checkfiles:
        file_list.append(dict(filepath=filepath,sha256=getFileMd5(filepath)))
    return file_list
        

if __name__ == '__main__':
    print(getFileHash())