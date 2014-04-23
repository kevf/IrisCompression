import sys

__author__ = 'kevin'
from pymongo import MongoClient
import os


class MaskCmp:
    def __init__(self, iris_db):
        self.client = MongoClient()
        self.db = self.client.iris_db
        self.coll = self.db[iris_db]

        self.usit_path = self.db["sys_param"].find_one({"program": "USIT"}, {"_id": 0, "path": 1}).get("path")
        self.maskcmp = self.usit_path+"maskcmp"

    def execmaskcmp_caht(self):
        file = self.coll.find_one({}, {"_id": 0,"path": 1, "segmentation.path_caht": 1, "segmentation.path_wahet": 1,
                                     "compression.segmentation.path_caht": 1, "compression.segmentation.path_wahet": 1})

        ref_seg_image = "\""+file.get("segmentation").get("path_caht")+"*.bmp.caht.bmp.binmask.bmp"+"\""
        cmp_seg_image_jpg_10 = "\""+file.get("compression").get("segmentation").get("path_caht")+"?1.50.bmp.jpg.bmp.caht.bmp.binmask.bmp"+"\""
        cmp_seg_image_jpg_15 = "\""+file.get("compression").get("segmentation").get("path_caht")+"?1.75.bmp.jpg.bmp.caht.bmp.binmask.bmp"+"\""
        cmp_seg_image_jpg_20 = "\""+file.get("compression").get("segmentation").get("path_caht")+"?1.100.bmp.jpg.bmp.caht.bmp.binmask.bmp"+"\""
        cmp_seg_image_jp2_10 = "\""+file.get("compression").get("segmentation").get("path_caht")+"?1.50.bmp.jp2.bmp.caht.bmp.binmask.bmp"+"\""
        cmp_seg_image_jp2_15 = "\""+file.get("compression").get("segmentation").get("path_caht")+"?1.75.bmp.jp2.bmp.caht.bmp.binmask.bmp"+"\""
        cmp_seg_image_jp2_20 = "\""+file.get("compression").get("segmentation").get("path_caht")+"?1.100.bmp.jp2.bmp.caht.bmp.binmask.bmp"+"\""
        cmp_seg_image_jxr_10 = "\""+file.get("compression").get("segmentation").get("path_caht")+"?1.50.bmp.jxr.bmp.caht.bmp.binmask.bmp"+"\""
        cmp_seg_image_jxr_15 = "\""+file.get("compression").get("segmentation").get("path_caht")+"?1.75.bmp.jxr.bmp.caht.bmp.binmask.bmp"+"\""
        cmp_seg_image_jxr_20 = "\""+file.get("compression").get("segmentation").get("path_caht")+"?1.100.bmp.jxr.bmp.caht.bmp.binmask.bmp"+"\""

        out_jpg_10 = "~/maskcmp_caht_out_jpg_50"
        out_jpg_15 = "~/maskcmp_caht_out_jpg_75"
        out_jpg_20 = "~/maskcmp_caht_out_jpg_100"
        out_jp2_10 = "~/maskcmp_caht_out_jp2_50"
        out_jp2_15 = "~/maskcmp_caht_out_jp2_75"
        out_jp2_20 = "~/maskcmp_caht_out_jp2_100"
        out_jxr_10 = "~/maskcmp_caht_out_jxr_50"
        out_jxr_15 = "~/maskcmp_caht_out_jxr_75"
        out_jxr_20 = "~/maskcmp_caht_out_jxr_100"

        cmd1 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jpg_10+" -o "+out_jpg_10
        cmd2 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jpg_15+" -o "+out_jpg_15
        cmd3 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jpg_20+" -o "+out_jpg_20
        cmd4 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jp2_10+" -o "+out_jp2_10
        cmd5 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jp2_15+" -o "+out_jp2_15
        cmd6 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jp2_20+" -o "+out_jp2_20
        cmd7 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jxr_10+" -o "+out_jxr_10
        cmd8 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jxr_15+" -o "+out_jxr_15
        cmd9 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jxr_20+" -o "+out_jxr_20

        print(cmd1)
        sp = os.system(cmd1)
        print(cmd2)
        sp = os.system(cmd2)
        print(cmd3)
        sp = os.system(cmd3)
        print(cmd4)
        sp = os.system(cmd4)
        print(cmd5)
        sp = os.system(cmd5)
        print(cmd6)
        sp = os.system(cmd6)
        print(cmd7)
        sp = os.system(cmd7)
        print(cmd8)
        sp = os.system(cmd8)
        print(cmd9)
        sp = os.system(cmd9)

    def execmaskcmp_wahet(self):
        file = self.coll.find_one({}, {"_id": 0,"path": 1, "segmentation.path_caht": 1, "segmentation.path_wahet": 1,
                                     "compression.segmentation.path_caht": 1, "compression.segmentation.path_wahet": 1})

        ref_seg_image = "\""+file.get("segmentation").get("path_wahet")+"*.bmp.wahet.bmp.binmask.bmp"+"\""
        cmp_seg_image_jpg_10 = "\""+file.get("compression").get("segmentation").get("path_wahet")+"?1.50.bmp.jpg.bmp.wahet.bmp.binmask.bmp"+"\""
        cmp_seg_image_jpg_15 = "\""+file.get("compression").get("segmentation").get("path_wahet")+"?1.75.bmp.jpg.bmp.wahet.bmp.binmask.bmp"+"\""
        cmp_seg_image_jpg_20 = "\""+file.get("compression").get("segmentation").get("path_wahet")+"?1.100.bmp.jpg.bmp.wahet.bmp.binmask.bmp"+"\""
        cmp_seg_image_jp2_10 = "\""+file.get("compression").get("segmentation").get("path_wahet")+"?1.50.bmp.jp2.bmp.wahet.bmp.binmask.bmp"+"\""
        cmp_seg_image_jp2_15 = "\""+file.get("compression").get("segmentation").get("path_wahet")+"?1.75.bmp.jp2.bmp.wahet.bmp.binmask.bmp"+"\""
        cmp_seg_image_jp2_20 = "\""+file.get("compression").get("segmentation").get("path_wahet")+"?1.100.bmp.jp2.bmp.wahet.bmp.binmask.bmp"+"\""
        cmp_seg_image_jxr_10 = "\""+file.get("compression").get("segmentation").get("path_wahet")+"?1.50.bmp.jxr.bmp.wahet.bmp.binmask.bmp"+"\""
        cmp_seg_image_jxr_15 = "\""+file.get("compression").get("segmentation").get("path_wahet")+"?1.75.bmp.jxr.bmp.wahet.bmp.binmask.bmp"+"\""
        cmp_seg_image_jxr_20 = "\""+file.get("compression").get("segmentation").get("path_wahet")+"?1.100.bmp.jxr.bmp.wahet.bmp.binmask.bmp"+"\""

        out_jpg_10 = "~/maskcmp_wahet_out_jpg_50"
        out_jpg_15 = "~/maskcmp_wahet_out_jpg_75"
        out_jpg_20 = "~/maskcmp_wahet_out_jpg_100"
        out_jp2_10 = "~/maskcmp_wahet_out_jp2_50"
        out_jp2_15 = "~/maskcmp_wahet_out_jp2_75"
        out_jp2_20 = "~/maskcmp_wahet_out_jp2_100"
        out_jxr_10 = "~/maskcmp_wahet_out_jxr_50"
        out_jxr_15 = "~/maskcmp_wahet_out_jxr_75"
        out_jxr_20 = "~/maskcmp_wahet_out_jxr_100"

        cmd1 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jpg_10+" -o "+out_jpg_10
        cmd2 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jpg_15+" -o "+out_jpg_15
        cmd3 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jpg_20+" -o "+out_jpg_20
        cmd4 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jp2_10+" -o "+out_jp2_10
        cmd5 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jp2_15+" -o "+out_jp2_15
        cmd6 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jp2_20+" -o "+out_jp2_20
        cmd7 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jxr_10+" -o "+out_jxr_10
        cmd8 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jxr_15+" -o "+out_jxr_15
        cmd9 = self.maskcmp+" -i "+ ref_seg_image+" "+ cmp_seg_image_jxr_20+" -o "+out_jxr_20

        print(cmd1)
        sp = os.system(cmd1)
        print(cmd2)
        sp = os.system(cmd2)
        print(cmd3)
        sp = os.system(cmd3)
        print(cmd4)
        sp = os.system(cmd4)
        print(cmd5)
        sp = os.system(cmd5)
        print(cmd6)
        sp = os.system(cmd6)
        print(cmd7)
        sp = os.system(cmd7)
        print(cmd8)
        sp = os.system(cmd8)
        print(cmd9)
        sp = os.system(cmd9)


def main():
    s = MaskCmp(sys.argv[1])
    s.execmaskcmp_caht()
    s.execmaskcmp_wahet()

if __name__ == "__main__":
    main()