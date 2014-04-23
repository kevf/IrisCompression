import os
import subprocess
import sys

__author__ = 'kevin'
from pymongo import MongoClient


class Compression:
    def __init__(self, iris_db):
        self.client = MongoClient()
        self.db = self.client.iris_db
        self.coll = self.db[iris_db]

        self.cjpeg = self.db["sys_param"].find_one({"program": "cjpeg"}, {"_id": 0, "path": 1}).get("path")+"cjpeg"
        self.djpeg = self.db["sys_param"].find_one({"program": "djpeg"}, {"_id": 0, "path": 1}).get("path")+"djpeg"
        self.opj_compress = self.db["sys_param"].find_one({"program": "opj_compress"}, {"_id": 0, "path": 1}).get("path")+"opj_compress"
        self.opj_decompress = self.db["sys_param"].find_one({"program": "opj_decompress"}, {"_id": 0, "path": 1}).get("path")+"opj_decompress"
        self.JxrEncApp = self.db["sys_param"].find_one({"program": "JxrEncApp"}, {"_id": 0, "path": 1}).get("path")+"JxrEncApp"
        self.JxrDecApp = self.db["sys_param"].find_one({"program": "JxrDecApp"}, {"_id": 0, "path": 1}).get("path")+"JxrDecApp"

    def getFiles(self, format):
        files = self.coll.find({"compression.formats": format},
                               {"_id": 0, "path": 1, "name": 1, "extension": 1,
                                "compression.path_decompressed": 1,"compression.path_compressed": 1,
                                "compression.formats.$": 1})
        return files

    def getFileNamesForCompression(self, file, ratio):
        source_file = file.get("path")+\
                      file.get("name")+\
                      file.get("extension")
        target_file = file.get("compression").get("path_compressed")+ \
                      file.get("name")+ \
                      "."+ratio+\
                      file.get("extension")+ \
                      file.get("compression").get("formats")[0]
        return source_file, target_file

    def getFileNamesForDecompression(self, file, ratio):
        source_file = file.get("compression").get("path_compressed")+ \
                      file.get("name")+ \
                      "."+ratio+\
                      file.get("extension")+ \
                      file.get("compression").get("formats")[0]
        target_file = file.get("compression").get("path_decompressed")+ \
                      file.get("name")+\
                      "."+ratio+\
                      file.get("extension")+ \
                      file.get("compression").get("formats")[0]+\
                      file.get("extension")

        return source_file, target_file

    ##################################################################################################
    def jpg_compress(self, ratio):
        if ratio == "20": rate = "27"
        elif ratio == "35": rate = "12"
        elif ratio == "50": rate = "8"
        elif ratio == "75": rate = "4"
        elif ratio == "100": rate = "3"
        else: rate = "100"

        files = self.getFiles(".jpg")
        for file in files:
            source_file, target_file = self.getFileNamesForCompression(file, ratio)
            cmd = self.cjpeg+" -q "+rate+" -optimize -outfile "+target_file+" "+source_file
            print(cmd)
            os.system(cmd)
            # wrapper for controlling filesize
            orig_rate = rate
            for i in range(5):
                if (os.path.getsize(target_file) - 100) > (os.path.getsize(source_file) / int(ratio)):
                    print("too big...")
                    rate = str(int(rate) - 1)
                    cmd = self.cjpeg+" -q "+rate+" -optimize -outfile "+target_file+" "+source_file
                    print(cmd)
                    os.system(cmd)
                elif (os.path.getsize(target_file) + 100) < (os.path.getsize(source_file) / int(ratio)):
                    print("too small...")
                    rate = str(int(rate) + 1)
                    cmd = self.cjpeg+" -q "+rate+" -optimize -outfile "+target_file+" "+source_file
                    print(cmd)
                    os.system(cmd)
            rate = orig_rate

    def jpg_decompress(self, ratio):
        files = self.getFiles(".jpg")
        for file in files:
            source_file, target_file = self.getFileNamesForDecompression(file, ratio)
            cmd = self.djpeg+" -outfile "+target_file+" -bmp "+source_file
            print(cmd)
            os.system(cmd)

    def jp2_compress(self, ratio):

        files = self.getFiles(".jp2")
        for file in files:
            source_file, target_file = self.getFileNamesForCompression(file, ratio)
            cmd = self.opj_compress+" -r "+ratio+" -i "+source_file+" -o "+target_file
            print(cmd)
            os.system(cmd)

    def jp2_decompress(self, ratio):
        files = self.getFiles(".jp2")
        for file in files:
            source_file, target_file = self.getFileNamesForDecompression(file, ratio)
            cmd = self.opj_decompress+" -i "+source_file+" -o "+target_file
            print(cmd)
            os.system(cmd)

    def jxr_compress(self, ratio):
        if ratio == "20": rate = "56"
        elif ratio == "35": rate = "67"
        elif ratio == "50": rate = "73"
        elif ratio == "75": rate = "82"
        elif ratio == "100": rate = "86"
        else: rate = "1"

        files = self.getFiles(".jxr")
        for file in files:
            source_file, target_file = self.getFileNamesForCompression(file, ratio)
            cmd = self.JxrEncApp+" -l 2 -q "+rate+" -i "+source_file+" -o "+target_file
            print(cmd)
            os.system(cmd)
            # wrapper for controlling filesize
            orig_rate = rate
            for i in range(5):
                if (os.path.getsize(target_file) - 100) > (os.path.getsize(source_file) / int(ratio)):
                    print("too big...")
                    rate = str(int(rate) + 1)
                    cmd = self.JxrEncApp+" -l 2 -q "+rate+" -i "+source_file+" -o "+target_file
                    print(cmd)
                    os.system(cmd)
                elif (os.path.getsize(target_file) + 100) < (os.path.getsize(source_file) / int(ratio)):
                    print("too small...")
                    rate = str(int(rate) - 1)
                    cmd = self.JxrEncApp+" -l 2 -q "+rate+" -i "+source_file+" -o "+target_file
                    print(cmd)
                    os.system(cmd)
            rate = orig_rate

    def jxr_decompress(self, ratio):
        files = self.getFiles(".jxr")
        for file in files:
            source_file, target_file = self.getFileNamesForDecompression(file, ratio)
            cmd = self.JxrDecApp+" -i "+source_file+" -o "+target_file
            print(cmd)
            os.system(cmd)

    def createDirs(self):
        paths = self.coll.find({}, {"_id": 0, "compression.path_decompressed": 1,"compression.path_compressed": 1})
        for path in paths:
            if not os.path.exists(path.get("compression").get("path_compressed")):
                os.makedirs(path.get("compression").get("path_compressed"))
            if not os.path.exists(path.get("compression").get("path_decompressed")):
                os.makedirs(path.get("compression").get("path_decompressed"))


def main():
    c = Compression(sys.argv[1])

    c.createDirs()

    c.jpg_compress("20")
    c.jpg_compress("35")
    c.jpg_compress("50")
    c.jpg_compress("75")
    c.jpg_compress("100")
    c.jpg_decompress("20")
    c.jpg_decompress("35")
    c.jpg_decompress("50")
    c.jpg_decompress("75")
    c.jpg_decompress("100")

    c.jp2_compress("20")
    c.jp2_compress("35")
    c.jp2_compress("50")
    c.jp2_compress("75")
    c.jp2_compress("100")
    c.jp2_decompress("20")
    c.jp2_decompress("35")
    c.jp2_decompress("50")
    c.jp2_decompress("75")
    c.jp2_decompress("100")

    c.jxr_compress("20")
    c.jxr_compress("35")
    c.jxr_compress("50")
    c.jxr_compress("75")
    c.jxr_compress("100")
    c.jxr_decompress("20")
    c.jxr_decompress("35")
    c.jxr_decompress("50")
    c.jxr_decompress("75")
    c.jxr_decompress("100")

if __name__ == "__main__":
    main()