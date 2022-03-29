from aip import AipOcr

class BaiduOCR(object):
    APP_ID = 'xxx'
    API_KEY = 'xxx'
    SECRET_KEY = 'xxx'
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
