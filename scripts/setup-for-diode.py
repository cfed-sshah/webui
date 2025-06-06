#!/usr/bin/env python3

import os
from zipfile import ZipFile, ZIP_DEFLATED


def main(argv):
    
    with ZipFile('archive.zip', 'w', ZIP_DEFLATED) as myzip:
        for root, dirs, files in os.walk(argv[1]):           
            if root.startswith(tuple(['./node_modules', './.nuxt', './.output', './.git'])):
                continue
            for file in files:
                file_path = os.path.join(root, file)
                _, extension = os.path.splitext(file_path)
                
                if extension == '.vue':
                    myzip.write(file_path, file_path + ".txt")
                else:
                    myzip.write(file_path)   

if __name__ == '__main__':
    import sys
    main(sys.argv)