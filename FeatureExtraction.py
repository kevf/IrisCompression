import os
import sys
from pymongo import MongoClient

__author__ = 'kevin'


class FeatureExtraction:
    def __init__(self, iris_db):
        self.client = MongoClient()
        self.db = self.client.iris_db
        self.coll = self.db[iris_db]

        self.usit_path = self.db["sys_param"].find_one({"program": "USIT"}, {"_id": 0, "path": 1}).get("path")
        self.lg = self.usit_path+"lg"
        self.qsw = self.usit_path+"qsw"
        self.ko = self.usit_path+"ko"
        self.cr = self.usit_path+"cr"
        self.cb = self.usit_path+"cb"
        self.dct = self.usit_path+"dct"

    def getFile(self):
        file = self.coll.find_one({}, {"_id": 0,
                                       "segmentation.path_caht": 1,
                                       "segmentation.path_wahet": 1,
                                       "extension": 1,
                                       "segmentation.extension_caht": 1,
                                       "segmentation.extension_wahet": 1,

                                       "segmentation.feature extraction.path_caht_lg": 1,
                                       "segmentation.feature extraction.path_wahet_lg": 1,
                                       "segmentation.feature extraction.extension_lg": 1,
                                       "segmentation.feature extraction.path_caht_qsw": 1,
                                       "segmentation.feature extraction.path_wahet_qsw": 1,
                                       "segmentation.feature extraction.extension_qsw": 1,
                                       "segmentation.feature extraction.path_caht_ko": 1,
                                       "segmentation.feature extraction.path_wahet_ko": 1,
                                       "segmentation.feature extraction.extension_ko": 1,
                                       "segmentation.feature extraction.path_caht_cr": 1,
                                       "segmentation.feature extraction.path_wahet_cr": 1,
                                       "segmentation.feature extraction.extension_cr": 1,
                                       "segmentation.feature extraction.path_caht_cb": 1,
                                       "segmentation.feature extraction.path_wahet_cb": 1,
                                       "segmentation.feature extraction.extension_cb": 1,
                                       "segmentation.feature extraction.path_caht_dct": 1,
                                       "segmentation.feature extraction.path_wahet_dct": 1,
                                       "segmentation.feature extraction.extension_dct": 1,

                                       "compression.segmentation.path_caht": 1,
                                       "compression.segmentation.path_wahet": 1,

                                       "compression.segmentation.feature extraction.path_caht_lg": 1,
                                       "compression.segmentation.feature extraction.path_wahet_lg": 1,
                                       "compression.segmentation.feature extraction.path_caht_qsw": 1,
                                       "compression.segmentation.feature extraction.path_wahet_qsw": 1,
                                       "compression.segmentation.feature extraction.path_caht_ko": 1,
                                       "compression.segmentation.feature extraction.path_wahet_ko": 1,
                                       "compression.segmentation.feature extraction.path_caht_cr": 1,
                                       "compression.segmentation.feature extraction.path_wahet_cr": 1,
                                       "compression.segmentation.feature extraction.path_caht_cb": 1,
                                       "compression.segmentation.feature extraction.path_wahet_cb": 1,
                                       "compression.segmentation.feature extraction.path_caht_dct": 1,
                                       "compression.segmentation.feature extraction.path_wahet_dct": 1})
        return file

    ################################################################################################################
    ## lg
    ################################################################################################################
    def exec_caht_lg(self):
        file = self.getFile()

        # for uncompressed images
        source = "\""+file.get("segmentation").get("path_caht")+"*"+file.get("extension")+file.get("segmentation").get("extension_caht")+"\""
        target = "\""+file.get("segmentation").get("feature extraction").get("path_caht_lg")+"?1"+file.get("extension")+file.get("segmentation").get("extension_caht")+file.get("segmentation").get("feature extraction").get("extension_lg")+"\""
        cmd = self.lg+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_dec_caht_lg(self):
        file = self.getFile()

        # for decompressed images
        source = "\""+file.get("compression").get("segmentation").get("path_caht")+"*"+file.get("extension")+file.get("segmentation").get("extension_caht")+"\""
        target = "\""+file.get("compression").get("segmentation").get("feature extraction").get("path_caht_lg")+"?1"+file.get("extension")+file.get("segmentation").get("extension_caht")+file.get("segmentation").get("feature extraction").get("extension_lg")+"\""
        cmd = self.lg+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_wahet_lg(self):
        file = self.getFile()

        # for uncompressed images
        source = "\""+file.get("segmentation").get("path_wahet")+"*"+file.get("extension")+file.get("segmentation").get("extension_wahet")+"\""
        target = "\""+file.get("segmentation").get("feature extraction").get("path_wahet_lg")+"?1"+file.get("extension")+file.get("segmentation").get("extension_wahet")+file.get("segmentation").get("feature extraction").get("extension_lg")+"\""
        cmd = self.lg+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_dec_wahet_lg(self):
        file = self.getFile()

        # for decompressed images
        source = "\""+file.get("compression").get("segmentation").get("path_wahet")+"*"+file.get("extension")+file.get("segmentation").get("extension_wahet")+"\""
        target = "\""+file.get("compression").get("segmentation").get("feature extraction").get("path_wahet_lg")+"?1"+file.get("extension")+file.get("segmentation").get("extension_wahet")+file.get("segmentation").get("feature extraction").get("extension_lg")+"\""
        cmd = self.lg+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    ################################################################################################################
    ## qsw
    ################################################################################################################
    def exec_caht_qsw(self):
        file = self.getFile()

        # for uncompressed images
        source = "\""+file.get("segmentation").get("path_caht")+"*"+file.get("extension")+file.get("segmentation").get("extension_caht")+"\""
        target = "\""+file.get("segmentation").get("feature extraction").get("path_caht_qsw")+"?1"+file.get("extension")+file.get("segmentation").get("extension_caht")+file.get("segmentation").get("feature extraction").get("extension_qsw")+"\""
        cmd = self.qsw+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_dec_caht_qsw(self):
        file = self.getFile()

        # for decompressed images
        source = "\""+file.get("compression").get("segmentation").get("path_caht")+"*"+file.get("extension")+file.get("segmentation").get("extension_caht")+"\""
        target = "\""+file.get("compression").get("segmentation").get("feature extraction").get("path_caht_qsw")+"?1"+file.get("extension")+file.get("segmentation").get("extension_caht")+file.get("segmentation").get("feature extraction").get("extension_qsw")+"\""
        cmd = self.qsw+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_wahet_qsw(self):
        file = self.getFile()

        # for uncompressed images
        source = "\""+file.get("segmentation").get("path_wahet")+"*"+file.get("extension")+file.get("segmentation").get("extension_wahet")+"\""
        target = "\""+file.get("segmentation").get("feature extraction").get("path_wahet_qsw")+"?1"+file.get("extension")+file.get("segmentation").get("extension_wahet")+file.get("segmentation").get("feature extraction").get("extension_qsw")+"\""
        cmd = self.qsw+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_dec_wahet_qsw(self):
        file = self.getFile()

        # for decompressed images
        source = "\""+file.get("compression").get("segmentation").get("path_wahet")+"*"+file.get("extension")+file.get("segmentation").get("extension_wahet")+"\""
        target = "\""+file.get("compression").get("segmentation").get("feature extraction").get("path_wahet_qsw")+"?1"+file.get("extension")+file.get("segmentation").get("extension_wahet")+file.get("segmentation").get("feature extraction").get("extension_qsw")+"\""
        cmd = self.qsw+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    ################################################################################################################
    ## ko
    ################################################################################################################
    def exec_caht_ko(self):
        file = self.getFile()

        # for uncompressed images
        source = "\""+file.get("segmentation").get("path_caht")+"*"+file.get("extension")+file.get("segmentation").get("extension_caht")+"\""
        target = "\""+file.get("segmentation").get("feature extraction").get("path_caht_ko")+"?1"+file.get("extension")+file.get("segmentation").get("extension_caht")+file.get("segmentation").get("feature extraction").get("extension_ko")+"\""
        cmd = self.ko+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_dec_caht_ko(self):
        file = self.getFile()

        # for decompressed images
        source = "\""+file.get("compression").get("segmentation").get("path_caht")+"*"+file.get("extension")+file.get("segmentation").get("extension_caht")+"\""
        target = "\""+file.get("compression").get("segmentation").get("feature extraction").get("path_caht_ko")+"?1"+file.get("extension")+file.get("segmentation").get("extension_caht")+file.get("segmentation").get("feature extraction").get("extension_ko")+"\""
        cmd = self.ko+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_wahet_ko(self):
        file = self.getFile()

        # for uncompressed images
        source = "\""+file.get("segmentation").get("path_wahet")+"*"+file.get("extension")+file.get("segmentation").get("extension_wahet")+"\""
        target = "\""+file.get("segmentation").get("feature extraction").get("path_wahet_ko")+"?1"+file.get("extension")+file.get("segmentation").get("extension_wahet")+file.get("segmentation").get("feature extraction").get("extension_ko")+"\""
        cmd = self.ko+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_dec_wahet_ko(self):
        file = self.getFile()

        # for decompressed images
        source = "\""+file.get("compression").get("segmentation").get("path_wahet")+"*"+file.get("extension")+file.get("segmentation").get("extension_wahet")+"\""
        target = "\""+file.get("compression").get("segmentation").get("feature extraction").get("path_wahet_ko")+"?1"+file.get("extension")+file.get("segmentation").get("extension_wahet")+file.get("segmentation").get("feature extraction").get("extension_ko")+"\""
        cmd = self.ko+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    ################################################################################################################
    ## cr
    ################################################################################################################
    def exec_caht_cr(self):
        file = self.getFile()

        # for uncompressed images
        source = "\""+file.get("segmentation").get("path_caht")+"*"+file.get("extension")+file.get("segmentation").get("extension_caht")+"\""
        target = "\""+file.get("segmentation").get("feature extraction").get("path_caht_cr")+"?1"+file.get("extension")+file.get("segmentation").get("extension_caht")+file.get("segmentation").get("feature extraction").get("extension_cr")+"\""
        cmd = self.cr+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_dec_caht_cr(self):
        file = self.getFile()

        # for decompressed images
        source = "\""+file.get("compression").get("segmentation").get("path_caht")+"*"+file.get("extension")+file.get("segmentation").get("extension_caht")+"\""
        target = "\""+file.get("compression").get("segmentation").get("feature extraction").get("path_caht_cr")+"?1"+file.get("extension")+file.get("segmentation").get("extension_caht")+file.get("segmentation").get("feature extraction").get("extension_cr")+"\""
        cmd = self.cr+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_wahet_cr(self):
        file = self.getFile()

        # for uncompressed images
        source = "\""+file.get("segmentation").get("path_wahet")+"*"+file.get("extension")+file.get("segmentation").get("extension_wahet")+"\""
        target = "\""+file.get("segmentation").get("feature extraction").get("path_wahet_cr")+"?1"+file.get("extension")+file.get("segmentation").get("extension_wahet")+file.get("segmentation").get("feature extraction").get("extension_cr")+"\""
        cmd = self.cr+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_dec_wahet_cr(self):
        file = self.getFile()

        # for decompressed images
        source = "\""+file.get("compression").get("segmentation").get("path_wahet")+"*"+file.get("extension")+file.get("segmentation").get("extension_wahet")+"\""
        target = "\""+file.get("compression").get("segmentation").get("feature extraction").get("path_wahet_cr")+"?1"+file.get("extension")+file.get("segmentation").get("extension_wahet")+file.get("segmentation").get("feature extraction").get("extension_cr")+"\""
        cmd = self.cr+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    ################################################################################################################
    ## cb
    ################################################################################################################
    def exec_caht_cb(self):
        file = self.getFile()

        # for uncompressed images
        source = "\""+file.get("segmentation").get("path_caht")+"*"+file.get("extension")+file.get("segmentation").get("extension_caht")+"\""
        target = "\""+file.get("segmentation").get("feature extraction").get("path_caht_cb")+"?1"+file.get("extension")+file.get("segmentation").get("extension_caht")+file.get("segmentation").get("feature extraction").get("extension_cb")+"\""
        cmd = self.cb+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_dec_caht_cb(self):
        file = self.getFile()

        # for decompressed images
        source = "\""+file.get("compression").get("segmentation").get("path_caht")+"*"+file.get("extension")+file.get("segmentation").get("extension_caht")+"\""
        target = "\""+file.get("compression").get("segmentation").get("feature extraction").get("path_caht_cb")+"?1"+file.get("extension")+file.get("segmentation").get("extension_caht")+file.get("segmentation").get("feature extraction").get("extension_cb")+"\""
        cmd = self.cb+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_wahet_cb(self):
        file = self.getFile()

        # for uncompressed images
        source = "\""+file.get("segmentation").get("path_wahet")+"*"+file.get("extension")+file.get("segmentation").get("extension_wahet")+"\""
        target = "\""+file.get("segmentation").get("feature extraction").get("path_wahet_cb")+"?1"+file.get("extension")+file.get("segmentation").get("extension_wahet")+file.get("segmentation").get("feature extraction").get("extension_cb")+"\""
        cmd = self.cb+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_dec_wahet_cb(self):
        file = self.getFile()

        # for decompressed images
        source = "\""+file.get("compression").get("segmentation").get("path_wahet")+"*"+file.get("extension")+file.get("segmentation").get("extension_wahet")+"\""
        target = "\""+file.get("compression").get("segmentation").get("feature extraction").get("path_wahet_cb")+"?1"+file.get("extension")+file.get("segmentation").get("extension_wahet")+file.get("segmentation").get("feature extraction").get("extension_cb")+"\""
        cmd = self.cb+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    ################################################################################################################
    ## dct
    ################################################################################################################
    def exec_caht_dct(self):
        file = self.getFile()

        # for uncompressed images
        source = "\""+file.get("segmentation").get("path_caht")+"*"+file.get("extension")+file.get("segmentation").get("extension_caht")+"\""
        target = "\""+file.get("segmentation").get("feature extraction").get("path_caht_dct")+"?1"+file.get("extension")+file.get("segmentation").get("extension_caht")+file.get("segmentation").get("feature extraction").get("extension_dct")+"\""
        cmd = self.dct+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_dec_caht_dct(self):
        file = self.getFile()

        # for decompressed images
        source = "\""+file.get("compression").get("segmentation").get("path_caht")+"*"+file.get("extension")+file.get("segmentation").get("extension_caht")+"\""
        target = "\""+file.get("compression").get("segmentation").get("feature extraction").get("path_caht_dct")+"?1"+file.get("extension")+file.get("segmentation").get("extension_caht")+file.get("segmentation").get("feature extraction").get("extension_dct")+"\""
        cmd = self.dct+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_wahet_dct(self):
        file = self.getFile()

        # for uncompressed images
        source = "\""+file.get("segmentation").get("path_wahet")+"*"+file.get("extension")+file.get("segmentation").get("extension_wahet")+"\""
        target = "\""+file.get("segmentation").get("feature extraction").get("path_wahet_dct")+"?1"+file.get("extension")+file.get("segmentation").get("extension_wahet")+file.get("segmentation").get("feature extraction").get("extension_dct")+"\""
        cmd = self.dct+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def exec_dec_wahet_dct(self):
        file = self.getFile()

        # for decompressed images
        source = "\""+file.get("compression").get("segmentation").get("path_wahet")+"*"+file.get("extension")+file.get("segmentation").get("extension_wahet")+"\""
        target = "\""+file.get("compression").get("segmentation").get("feature extraction").get("path_wahet_dct")+"?1"+file.get("extension")+file.get("segmentation").get("extension_wahet")+file.get("segmentation").get("feature extraction").get("extension_dct")+"\""
        cmd = self.dct+" -i "+source+" -o "+target
        print(cmd)
        os.system(cmd)

    def createDirs(self):
        paths = self.getFile()
        if not os.path.exists(paths.get("segmentation").get("feature extraction").get("path_wahet_lg")):
            os.makedirs(paths.get("segmentation").get("feature extraction").get("path_wahet_lg"))
        if not os.path.exists(paths.get("segmentation").get("feature extraction").get("path_caht_lg")):
            os.makedirs(paths.get("segmentation").get("feature extraction").get("path_caht_lg"))
        if not os.path.exists(paths.get("compression").get("segmentation").get("feature extraction").get("path_wahet_lg")):
            os.makedirs(paths.get("compression").get("segmentation").get("feature extraction").get("path_wahet_lg"))
        if not os.path.exists(paths.get("compression").get("segmentation").get("feature extraction").get("path_caht_lg")):
            os.makedirs(paths.get("compression").get("segmentation").get("feature extraction").get("path_caht_lg"))

        if not os.path.exists(paths.get("segmentation").get("feature extraction").get("path_wahet_qsw")):
            os.makedirs(paths.get("segmentation").get("feature extraction").get("path_wahet_qsw"))
        if not os.path.exists(paths.get("segmentation").get("feature extraction").get("path_caht_qsw")):
            os.makedirs(paths.get("segmentation").get("feature extraction").get("path_caht_qsw"))
        if not os.path.exists(paths.get("compression").get("segmentation").get("feature extraction").get("path_wahet_qsw")):
            os.makedirs(paths.get("compression").get("segmentation").get("feature extraction").get("path_wahet_qsw"))
        if not os.path.exists(paths.get("compression").get("segmentation").get("feature extraction").get("path_caht_qsw")):
            os.makedirs(paths.get("compression").get("segmentation").get("feature extraction").get("path_caht_qsw"))

        if not os.path.exists(paths.get("segmentation").get("feature extraction").get("path_wahet_ko")):
            os.makedirs(paths.get("segmentation").get("feature extraction").get("path_wahet_ko"))
        if not os.path.exists(paths.get("segmentation").get("feature extraction").get("path_caht_ko")):
            os.makedirs(paths.get("segmentation").get("feature extraction").get("path_caht_ko"))
        if not os.path.exists(paths.get("compression").get("segmentation").get("feature extraction").get("path_wahet_ko")):
            os.makedirs(paths.get("compression").get("segmentation").get("feature extraction").get("path_wahet_ko"))
        if not os.path.exists(paths.get("compression").get("segmentation").get("feature extraction").get("path_caht_ko")):
            os.makedirs(paths.get("compression").get("segmentation").get("feature extraction").get("path_caht_ko"))

        if not os.path.exists(paths.get("segmentation").get("feature extraction").get("path_wahet_cr")):
            os.makedirs(paths.get("segmentation").get("feature extraction").get("path_wahet_cr"))
        if not os.path.exists(paths.get("segmentation").get("feature extraction").get("path_caht_cr")):
            os.makedirs(paths.get("segmentation").get("feature extraction").get("path_caht_cr"))
        if not os.path.exists(paths.get("compression").get("segmentation").get("feature extraction").get("path_wahet_cr")):
            os.makedirs(paths.get("compression").get("segmentation").get("feature extraction").get("path_wahet_cr"))
        if not os.path.exists(paths.get("compression").get("segmentation").get("feature extraction").get("path_caht_cr")):
            os.makedirs(paths.get("compression").get("segmentation").get("feature extraction").get("path_caht_cr"))

        if not os.path.exists(paths.get("segmentation").get("feature extraction").get("path_wahet_cb")):
            os.makedirs(paths.get("segmentation").get("feature extraction").get("path_wahet_cb"))
        if not os.path.exists(paths.get("segmentation").get("feature extraction").get("path_caht_cb")):
            os.makedirs(paths.get("segmentation").get("feature extraction").get("path_caht_cb"))
        if not os.path.exists(paths.get("compression").get("segmentation").get("feature extraction").get("path_wahet_cb")):
            os.makedirs(paths.get("compression").get("segmentation").get("feature extraction").get("path_wahet_cb"))
        if not os.path.exists(paths.get("compression").get("segmentation").get("feature extraction").get("path_caht_cb")):
            os.makedirs(paths.get("compression").get("segmentation").get("feature extraction").get("path_caht_cb"))

        if not os.path.exists(paths.get("segmentation").get("feature extraction").get("path_wahet_dct")):
            os.makedirs(paths.get("segmentation").get("feature extraction").get("path_wahet_dct"))
        if not os.path.exists(paths.get("segmentation").get("feature extraction").get("path_caht_dct")):
            os.makedirs(paths.get("segmentation").get("feature extraction").get("path_caht_dct"))
        if not os.path.exists(paths.get("compression").get("segmentation").get("feature extraction").get("path_wahet_dct")):
            os.makedirs(paths.get("compression").get("segmentation").get("feature extraction").get("path_wahet_dct"))
        if not os.path.exists(paths.get("compression").get("segmentation").get("feature extraction").get("path_caht_dct")):
            os.makedirs(paths.get("compression").get("segmentation").get("feature extraction").get("path_caht_dct"))


def main():
    f = FeatureExtraction(sys.argv[1])
    f.createDirs()
    f.exec_caht_lg()
    f.exec_wahet_lg()
    f.exec_caht_qsw()
    f.exec_wahet_qsw()
    f.exec_caht_ko()
    f.exec_wahet_ko()
    f.exec_caht_cr()
    f.exec_wahet_cr()
    f.exec_caht_cb()
    f.exec_wahet_cb()
    f.exec_caht_dct()
    f.exec_wahet_dct()


    f.exec_dec_caht_lg()
    f.exec_dec_wahet_lg()
    f.exec_dec_caht_qsw()
    f.exec_dec_wahet_qsw()
    f.exec_dec_caht_ko()
    f.exec_dec_wahet_ko()
    f.exec_dec_caht_cr()
    f.exec_dec_wahet_cr()
    f.exec_dec_caht_cb()
    f.exec_dec_wahet_cb()
    f.exec_dec_caht_dct()
    f.exec_dec_wahet_dct()


if __name__ == "__main__":
    main()