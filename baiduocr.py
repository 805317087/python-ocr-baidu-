from aip import AipOcr

class BaiduOCR(object):
    APP_ID = '17010327'
    API_KEY = 'X2MWCU1LG1PX5H6GAXgdlWD7'
    SECRET_KEY = 'vz6GZ6TkhSFvY3quqcuC3EG8oEW3kThB'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    def __init__(self, img):
        super().__init__()
        self.img = img
        self.client = AipOcr(BaiduOCR.APP_ID, BaiduOCR.API_KEY, BaiduOCR.SECRET_KEY)

    def base(self):
        i = open(self.img,'rb')
        image = i.read()
        result = self.client.basicGeneral(image)
        # 将所有的文字都合并到一起
        return result

    def gjd1(self):
        i = open(self.img,'rb')
        image = i.read()
        result = self.client.basicAccurate(image)
        # 将所有的文字都合并到一起
        return result

    def gjd2(self):
        i = open(self.img,'rb')
        image = i.read()
        result = self.client.accurate(image)
        # 将所有的文字都合并到一起
        return result
