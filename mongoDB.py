from configparser import ConfigParser
import sys

__author__ = 'Kevin'
from pymongo import MongoClient
import os


class MongoDB:

    def __init__(self, iris_db):
        self.client = MongoClient()
        self.db = self.client.iris_db
        self.coll = self.db[iris_db]

    def getdb(self):
        return self.db

    def drop(self):
        self.coll.drop()

    def traverse(self, dir):
        for path, subdirs, files in os.walk(dir):
            for name in files:
                self.insert(path, name)

    def insert(self, path, name):
        fileName, fileExtension = os.path.splitext(name)
        doc =  {"name": fileName,
                "path": path,
                "extension": fileExtension,
                "compression": {"formats": [".jpg", ".jp2", ".jxr"],
                                "ratios": [10, 15, 20],
                                "path_compressed": os.path.split(path)[0]+"_compressed/",
                                "path_decompressed": os.path.split(path)[0]+"_decompressed/",
                                "segmentation": {"extension_wahet": ".wahet.bmp",
                                                 "extension_caht": ".caht.bmp",
                                                 "path_caht": os.path.split(path)[0]+"_decompressed_caht/",
                                                 "path_wahet": os.path.split(path)[0]+"_decompressed_wahet/",
                                                 "feature extraction": {"extension_lg": ".lg.bmp",
                                                                        "extension_qsw": ".qsw.bmp",
                                                                        "extension_ko": ".ko.bmp",
                                                                        "extension_cr": ".cr.bmp",
                                                                        "extension_cb": ".cb.bmp",
                                                                        "extension_dct": ".dct.bmp",
                                                                        "path_caht_lg": os.path.split(path)[0]+"_decompressed_caht_lg/",
                                                                        "path_wahet_lg": os.path.split(path)[0]+"_decompressed_wahet_lg/",
                                                                        "path_caht_qsw": os.path.split(path)[0]+"_decompressed_caht_qsw/",
                                                                        "path_wahet_qsw": os.path.split(path)[0]+"_decompressed_wahet_qsw/",
                                                                        "path_caht_ko": os.path.split(path)[0]+"_decompressed_caht_ko/",
                                                                        "path_wahet_ko": os.path.split(path)[0]+"_decompressed_wahet_ko/",
                                                                        "path_caht_cr": os.path.split(path)[0]+"_decompressed_caht_cr/",
                                                                        "path_wahet_cr": os.path.split(path)[0]+"_decompressed_wahet_cr/",
                                                                        "path_caht_cb": os.path.split(path)[0]+"_decompressed_caht_cb/",
                                                                        "path_wahet_cb": os.path.split(path)[0]+"_decompressed_wahet_cb/",
                                                                        "path_caht_dct": os.path.split(path)[0]+"_decompressed_caht_dct/",
                                                                        "path_wahet_dct": os.path.split(path)[0]+"_decompressed_wahet_dct/"}}},
                "segmentation": {"extension_wahet": ".wahet.bmp",
                                 "extension_caht": ".caht.bmp",
                                 "path_caht": os.path.split(path)[0]+"_caht/",
                                 "path_wahet": os.path.split(path)[0]+"_wahet/",
                                 "feature extraction": {"extension_lg": ".lg.bmp",
                                                        "extension_qsw": ".qsw.bmp",
                                                        "extension_ko": ".ko.bmp",
                                                        "extension_cr": ".cr.bmp",
                                                        "extension_cb": ".cb.bmp",
                                                        "extension_dct": ".dct.bmp",
                                                        "path_caht_lg": os.path.split(path)[0]+"_caht_lg/",
                                                        "path_wahet_lg": os.path.split(path)[0]+"_wahet_lg/",
                                                        "path_caht_qsw": os.path.split(path)[0]+"_caht_qsw/",
                                                        "path_wahet_qsw": os.path.split(path)[0]+"_wahet_qsw/",
                                                        "path_caht_ko": os.path.split(path)[0]+"_caht_ko/",
                                                        "path_wahet_ko": os.path.split(path)[0]+"_wahet_ko/",
                                                        "path_caht_cr": os.path.split(path)[0]+"_caht_cr/",
                                                        "path_wahet_cr": os.path.split(path)[0]+"_wahet_cr/",
                                                        "path_caht_cb": os.path.split(path)[0]+"_caht_cb/",
                                                        "path_wahet_cb": os.path.split(path)[0]+"_wahet_cb/",
                                                        "path_caht_dct": os.path.split(path)[0]+"_caht_dct/",
                                                        "path_wahet_dct": os.path.split(path)[0]+"_wahet_dct/"}}}
        self.coll.insert(doc)

    def close(self):
        self.client.close()

    def setSysParam(self):
        config = ConfigParser()
        config.read('db.ini')

        USIT_PATH = config.get('USIT', 'path')
        cjpeg_PATH = config.get('cjpeg', 'path')
        djpeg_PATH = config.get('djpeg', 'path')
        opj_compress_PATH = config.get('opj_compress', 'path')
        opj_decompress_PATH = config.get('opj_decompress', 'path')
        JxrEncApp_PATH = config.get('JxrEncApp', 'path')
        JxrDecApp_PATH = config.get('JxrDecApp', 'path')

        self.db["sys_param"].remove()
        self.db["sys_param"].insert({"program": "USIT", "path": USIT_PATH})
        self.db["sys_param"].insert({"program": "cjpeg", "path": cjpeg_PATH})
        self.db["sys_param"].insert({"program": "djpeg", "path": djpeg_PATH})
        self.db["sys_param"].insert({"program": "opj_compress", "path": opj_compress_PATH})
        self.db["sys_param"].insert({"program": "opj_decompress", "path": opj_decompress_PATH})
        self.db["sys_param"].insert({"program": "JxrEncApp", "path": JxrEncApp_PATH})
        self.db["sys_param"].insert({"program": "JxrDecApp", "path": JxrDecApp_PATH})


def main():
    x = MongoDB(sys.argv[1])
    x.drop()
    x.traverse(sys.argv[2])
    x.setSysParam()
    x.close()

if __name__ == "__main__":
    main()