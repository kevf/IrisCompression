import os
import sys

__author__ = 'kevin'
from pymongo import MongoClient


class Hdverify:
    def __init__(self, iris_db):
        self.client = MongoClient()
        self.db = self.client.iris_db
        self.coll = self.db[iris_db]

        self.usit_path = self.db["sys_param"].find_one({"program": "USIT"}, {"_id": 0, "path": 1}).get("path")
        self.hdverify = self.usit_path+"hdverify"

    def exec(self):
        docs = self.coll.find_one({},{"_id": 0,
                                "segmentation.feature extraction.path_caht_lg": 1,
                                "segmentation.feature extraction.path_wahet_lg": 1,
                                "segmentation.feature extraction.path_caht_qsw": 1,
                                "segmentation.feature extraction.path_wahet_qsw": 1,
                                "segmentation.feature extraction.path_caht_cr": 1,
                                "segmentation.feature extraction.path_wahet_cr": 1,
                                "compression.segmentation.feature extraction.path_caht_lg": 1,
                                "compression.segmentation.feature extraction.path_wahet_lg": 1,
                                "compression.segmentation.feature extraction.path_caht_qsw": 1,
                                "compression.segmentation.feature extraction.path_wahet_qsw": 1,
                                "compression.segmentation.feature extraction.path_caht_cr": 1,
                                "compression.segmentation.feature extraction.path_wahet_cr": 1})

        cmd1 = self.hdverify+" -i \""+docs.get("segmentation").get("feature extraction").get("path_caht_lg")+"*_*_*.bmp.*\" "+"\"?1\""+" -r "+"~/hdverify_caht_lg.dat"
        cmd2 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_lg")+"*_*_*.50.bmp.jp2.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_lg_50_jp2.dat"
        cmd3 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_lg")+"*_*_*.75.bmp.jp2.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_lg_75_jp2.dat"
        cmd4 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_lg")+"*_*_*.100.bmp.jp2.*\" "+"\"?1\""+" -r " +"~/hdverify_caht_lg_100_jp2.dat"
        cmd5 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_lg")+"*_*_*.50.bmp.jpg.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_lg_50_jpg.dat"
        cmd6 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_lg")+"*_*_*.75.bmp.jpg.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_lg_75_jpg.dat"
        cmd7 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_lg")+"*_*_*.100.bmp.jpg.*\" "+"\"?1\""+" -r " +"~/hdverify_caht_lg_100_jpg.dat"
        cmd8 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_lg")+"*_*_*.50.bmp.jxr.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_lg_50_jxr.dat"
        cmd9 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_lg")+"*_*_*.75.bmp.jxr.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_lg_75_jxr.dat"
        cmd10 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_lg")+"*_*_*.100.bmp.jxr.*\" "+"\"?1\""+" -r "+"~/hdverify_caht_lg_100_jxr.dat"

        cmd11 = self.hdverify+" -i \""+docs.get("segmentation").get("feature extraction").get("path_wahet_lg")+"*_*_*.bmp.*\" "+"\"?1\""+" -r "+"~/hdverify_wahet_lg.dat"
        cmd12 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_lg")+"*_*_*.50.bmp.jp2.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_lg_50_jp2.dat"
        cmd13 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_lg")+"*_*_*.75.bmp.jp2.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_lg_75_jp2.dat"
        cmd14 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_lg")+"*_*_*.100.bmp.jp2.*\" "+"\"?1\""+" -r "+"~/hdverify_wahet_lg_100_jp2.dat"
        cmd15 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_lg")+"*_*_*.50.bmp.jpg.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_lg_50_jpg.dat"
        cmd16 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_lg")+"*_*_*.75.bmp.jpg.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_lg_75_jpg.dat"
        cmd17 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_lg")+"*_*_*.100.bmp.jpg.*\" "+"\"?1\""+" -r "+"~/hdverify_wahet_lg_100_jpg.dat"
        cmd18 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_lg")+"*_*_*.50.bmp.jxr.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_lg_50_jxr.dat"
        cmd19 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_lg")+"*_*_*.75.bmp.jxr.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_lg_75_jxr.dat"
        cmd20 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_lg")+"*_*_*.100.bmp.jxr.*\" "+"\"?1\""+" -r "+"~/hdverify_wahet_lg_100_jxr.dat"

        print(cmd1)
        os.system(cmd1)
        os.system(cmd2)
        os.system(cmd3)
        os.system(cmd4)
        os.system(cmd5)
        os.system(cmd6)
        os.system(cmd7)
        os.system(cmd8)
        os.system(cmd9)
        os.system(cmd10)
        os.system(cmd11)
        os.system(cmd12)
        os.system(cmd13)
        os.system(cmd14)
        os.system(cmd15)
        os.system(cmd16)
        os.system(cmd17)
        os.system(cmd18)
        os.system(cmd19)
        os.system(cmd20)

        cmd1 = self.hdverify+" -i \""+docs.get("segmentation").get("feature extraction").get("path_caht_qsw")+"*_*_*.bmp.*\" "+"\"?1\""+" -r "+"~/hdverify_caht_qsw.dat"
        cmd2 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_qsw")+"*_*_*.50.bmp.jp2.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_qsw_50_jp2.dat"
        cmd3 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_qsw")+"*_*_*.75.bmp.jp2.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_qsw_75_jp2.dat"
        cmd4 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_qsw")+"*_*_*.100.bmp.jp2.*\" "+"\"?1\""+" -r " +"~/hdverify_caht_qsw_100_jp2.dat"
        cmd5 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_qsw")+"*_*_*.50.bmp.jpg.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_qsw_50_jpg.dat"
        cmd6 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_qsw")+"*_*_*.75.bmp.jpg.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_qsw_75_jpg.dat"
        cmd7 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_qsw")+"*_*_*.100.bmp.jpg.*\" "+"\"?1\""+" -r " +"~/hdverify_caht_qsw_100_jpg.dat"
        cmd8 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_qsw")+"*_*_*.50.bmp.jxr.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_qsw_50_jxr.dat"
        cmd9 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_qsw")+"*_*_*.75.bmp.jxr.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_qsw_75_jxr.dat"
        cmd10 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_qsw")+"*_*_*.100.bmp.jxr.*\" "+"\"?1\""+" -r "+"~/hdverify_caht_qsw_100_jxr.dat"

        cmd11 = self.hdverify+" -i \""+docs.get("segmentation").get("feature extraction").get("path_wahet_qsw")+"*_*_*.bmp.*\" "+"\"?1\""+" -r "+"~/hdverify_wahet_qsw.dat"
        cmd12 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_qsw")+"*_*_*.50.bmp.jp2.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_qsw_50_jp2.dat"
        cmd13 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_qsw")+"*_*_*.75.bmp.jp2.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_qsw_75_jp2.dat"
        cmd14 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_qsw")+"*_*_*.100.bmp.jp2.*\" "+"\"?1\""+" -r "+"~/hdverify_wahet_qsw_100_jp2.dat"
        cmd15 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_qsw")+"*_*_*.50.bmp.jpg.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_qsw_50_jpg.dat"
        cmd16 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_qsw")+"*_*_*.75.bmp.jpg.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_qsw_75_jpg.dat"
        cmd17 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_qsw")+"*_*_*.100.bmp.jpg.*\" "+"\"?1\""+" -r "+"~/hdverify_wahet_qsw_100_jpg.dat"
        cmd18 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_qsw")+"*_*_*.50.bmp.jxr.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_qsw_50_jxr.dat"
        cmd19 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_qsw")+"*_*_*.75.bmp.jxr.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_qsw_75_jxr.dat"
        cmd20 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_qsw")+"*_*_*.100.bmp.jxr.*\" "+"\"?1\""+" -r "+"~/hdverify_wahet_qsw_100_jxr.dat"

        os.system(cmd1)
        os.system(cmd2)
        os.system(cmd3)
        os.system(cmd4)
        os.system(cmd5)
        os.system(cmd6)
        os.system(cmd7)
        os.system(cmd8)
        os.system(cmd9)
        os.system(cmd10)
        os.system(cmd11)
        os.system(cmd12)
        os.system(cmd13)
        os.system(cmd14)
        os.system(cmd15)
        os.system(cmd16)
        os.system(cmd17)
        os.system(cmd18)
        os.system(cmd19)
        os.system(cmd20)

        cmd1 = self.hdverify+" -i \""+docs.get("segmentation").get("feature extraction").get("path_caht_cr")+"*_*_*.bmp.*\" "+"\"?1\""+" -r "+"~/hdverify_caht_cr.dat"
        cmd2 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_cr")+"*_*_*.50.bmp.jp2.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_cr_50_jp2.dat"
        cmd3 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_cr")+"*_*_*.75.bmp.jp2.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_cr_75_jp2.dat"
        cmd4 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_cr")+"*_*_*.100.bmp.jp2.*\" "+"\"?1\""+" -r " +"~/hdverify_caht_cr_100_jp2.dat"
        cmd5 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_cr")+"*_*_*.50.bmp.jpg.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_cr_50_jpg.dat"
        cmd6 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_cr")+"*_*_*.75.bmp.jpg.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_cr_75_jpg.dat"
        cmd7 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_cr")+"*_*_*.100.bmp.jpg.*\" "+"\"?1\""+" -r " +"~/hdverify_caht_cr_100_jpg.dat"
        cmd8 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_cr")+"*_*_*.50.bmp.jxr.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_cr_50_jxr.dat"
        cmd9 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_cr")+"*_*_*.75.bmp.jxr.*\" "+"\"?1\""+" -r "  +"~/hdverify_caht_cr_75_jxr.dat"
        cmd10 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_caht_cr")+"*_*_*.100.bmp.jxr.*\" "+"\"?1\""+" -r "+"~/hdverify_caht_cr_100_jxr.dat"

        cmd11 = self.hdverify+" -i \""+docs.get("segmentation").get("feature extraction").get("path_wahet_cr")+"*_*_*.bmp.*\" "+"\"?1\""+" -r "+"~/hdverify_wahet_cr.dat"
        cmd12 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_cr")+"*_*_*.50.bmp.jp2.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_cr_50_jp2.dat"
        cmd13 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_cr")+"*_*_*.75.bmp.jp2.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_cr_75_jp2.dat"
        cmd14 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_cr")+"*_*_*.100.bmp.jp2.*\" "+"\"?1\""+" -r "+"~/hdverify_wahet_cr_100_jp2.dat"
        cmd15 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_cr")+"*_*_*.50.bmp.jpg.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_cr_50_jpg.dat"
        cmd16 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_cr")+"*_*_*.75.bmp.jpg.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_cr_75_jpg.dat"
        cmd17 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_cr")+"*_*_*.100.bmp.jpg.*\" "+"\"?1\""+" -r "+"~/hdverify_wahet_cr_100_jpg.dat"
        cmd18 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_cr")+"*_*_*.50.bmp.jxr.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_cr_50_jxr.dat"
        cmd19 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_cr")+"*_*_*.75.bmp.jxr.*\" "+"\"?1\""+" -r " +"~/hdverify_wahet_cr_75_jxr.dat"
        cmd20 = self.hdverify+" -i \""+docs.get("compression").get("segmentation").get("feature extraction").get("path_wahet_cr")+"*_*_*.100.bmp.jxr.*\" "+"\"?1\""+" -r "+"~/hdverify_wahet_cr_100_jxr.dat"

        os.system(cmd1)
        os.system(cmd2)
        os.system(cmd3)
        os.system(cmd4)
        os.system(cmd5)
        os.system(cmd6)
        os.system(cmd7)
        os.system(cmd8)
        os.system(cmd9)
        os.system(cmd10)
        os.system(cmd11)
        os.system(cmd12)
        os.system(cmd13)
        os.system(cmd14)
        os.system(cmd15)
        os.system(cmd16)
        os.system(cmd17)
        os.system(cmd18)
        os.system(cmd19)
        os.system(cmd20)


def main():
    s = Hdverify(sys.argv[1])
    s.exec()

if __name__ == "__main__":
    main()