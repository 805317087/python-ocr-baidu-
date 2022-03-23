from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QFileDialog,QMessageBox
from imgview import IMG_WIN
from baiduocr import BaiduOCR
import cv2

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load('window.ui')
        self.graphic = IMG_WIN(self.ui.graphicsView)	# 实例化IMG_WIN类
        self.ui.btn_openImage.clicked.connect(self.openImage)
        self.ui.btn_base.clicked.connect(self.ocr_base)
        self.ui.btn_gjd1.clicked.connect(self.ocr_gjd1)
        self.ui.btn_gjd2.clicked.connect(self.ocr_gjd2)

    def openImage(self):
        try:
            imgPath,imgType = QFileDialog.getOpenFileName(
                self,  # 父窗口对象
                "选择你要上传的图片",  # 标题
                r".",  # 起始目录
                "图片类型 (*.png *.jpg *.bmp)"  # 选择类型过滤项，过滤内容在括号中
            )
            imgPath = r'%s'%(imgPath,)
            print(imgPath)

            if imgPath != '':
                img = cv2.imread(imgPath, cv2.COLOR_BGR2RGB)
                self.ui.lineEdit.setText(imgPath)
                self.graphic.addScenes(img)
            else:
                return

        except:
            QMessageBox.information(self, '图片显示失败', '请确保（路径/文件名）没有中文字样')

    def ocr_base(self):
        imgpath = self.ui.lineEdit.text()
        if imgpath != '':
            exp = BaiduOCR(imgpath)
            result = exp.base()
            self.print_textEdit(result)
        else:
            QMessageBox.information(self, '提示', '请打开图片再进行识别')

    def ocr_gjd1(self):
        imgpath = self.ui.lineEdit.text()
        if imgpath != '':
            exp = BaiduOCR(imgpath)
            result = exp.gjd1()
            self.print_textEdit(result)
        else:
            QMessageBox.information(self, '提示', '请打开图片再进行识别')

    def ocr_gjd2(self):
        imgpath = self.ui.lineEdit.text()
        if imgpath != '':
            exp = BaiduOCR(imgpath)
            result = exp.gjd2()
            self.print_textEdit(result)
        else:
            QMessageBox.information(self, '提示', '请打开图片再进行识别')

    def print_textEdit(self,result):
        print(result)
        content = ''
        for item in result['words_result']:
            content = content + '\n%s' % (item['words'])
        self.ui.textEdit.setText(content)