import os
from pymongo import MongoClient
import sys

__author__ = 'Kevin'


class Segmentation:
    def __init__(self, iris_db):
        self.client = MongoClient()
        self.db = self.client.iris_db
        self.coll = self.db[iris_db]

        self.usit_path = self.db["sys_param"].find_one({"program": "USIT"}, {"_id": 0, "path": 1}).get("path")
        self.caht = self.usit_path+"caht"
        self.wahet = self.usit_path+"wahet"

    def execcaht(self):
        file = self.coll.find_one({}, {"_id": 0, "path": 1, "name": 1, "extension": 1, "segmentation.path_caht": 1,
                                     "compression.path_decompressed": 1, "compression.segmentation.path_caht": 1})

        # for original images
        orig_image = "\""+file.get("path")+"*"+"\""
        seg_image = "\""+file.get("segmentation").get("path_caht")+"?1"+".caht.bmp"+"\""
        binmask_image = "\""+file.get("segmentation").get("path_caht")+"?1"+".caht.bmp.binmask.bmp"+"\""
        cmd = self.caht+" -i "+orig_image+" -bm "+binmask_image+" -o "+seg_image
        print(cmd)
        sp = os.system(cmd)

        # for decompressed images
        orig_image = "\""+file.get("compression").get("path_decompressed")+"*"+"\""
        seg_image = "\""+file.get("compression").get("segmentation").get("path_caht")+"?1"+".caht.bmp"+"\""
        binmask_image = "\""+file.get("compression").get("segmentation").get("path_caht")+"?1"+".caht.bmp.binmask.bmp"+"\""
        cmd = self.caht+" -i "+orig_image+" -bm "+binmask_image+" -o "+seg_image
        print(cmd)
        sp = os.system(cmd)

    def execwahet(self):
        file = self.coll.find_one({}, {"_id": 0, "path": 1, "name": 1, "extension": 1, "segmentation.path_wahet": 1,
                                     "compression.path_decompressed": 1, "compression.segmentation.path_wahet": 1})

        # for original images
        orig_image = "\""+file.get("path")+"*"+"\""
        seg_image = "\""+file.get("segmentation").get("path_wahet")+"?1"+".wahet.bmp"+"\""
        binmask_image = "\""+file.get("segmentation").get("path_wahet")+"?1"+".wahet.bmp.binmask.bmp"+"\""
        cmd = self.wahet+" -i "+orig_image+" -bm "+binmask_image+" -o "+seg_image
        sp = os.system(cmd)

        # for decompressed images
        orig_image = "\""+file.get("compression").get("path_decompressed")+"*"+"\""
        seg_image = "\""+file.get("compression").get("segmentation").get("path_wahet")+"?1"+".wahet.bmp"+"\""
        binmask_image = "\""+file.get("compression").get("segmentation").get("path_wahet")+"?1"+".wahet.bmp.binmask.bmp"+"\""
        cmd = self.wahet+" -i "+orig_image+" -bm "+binmask_image+" -o "+seg_image
        sp = os.system(cmd)

    def createDirs(self):
        paths = self.coll.find({}, {"_id": 0, "segmentation.path_caht": 1, "segmentation.path_wahet": 1, "compression.segmentation.path_caht": 1,"compression.segmentation.path_wahet": 1})
        for path in paths:
            if not os.path.exists(path.get("compression").get("segmentation").get("path_caht")):
                os.makedirs(path.get("compression").get("segmentation").get("path_caht"))
            if not os.path.exists(path.get("compression").get("segmentation").get("path_wahet")):
                os.makedirs(path.get("compression").get("segmentation").get("path_wahet"))
            if not os.path.exists(path.get("segmentation").get("path_caht")):
                os.makedirs(path.get("segmentation").get("path_caht"))
            if not os.path.exists(path.get("segmentation").get("path_wahet")):
                os.makedirs(path.get("segmentation").get("path_wahet"))


def main():
    s = Segmentation(sys.argv[1])
    s.createDirs()
    s.execcaht()
    s.execwahet()


if __name__ == "__main__":
    main()