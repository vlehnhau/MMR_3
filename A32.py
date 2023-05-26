import sys
import numpy as np
import matplotlib.pyplot as plt
import PyQt6.QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc
import copy


class MainWidget(qtw.QWidget):
    imagewidth: int
    imageheight: int
    image: qtg.QImage
    x1: float
    x2: float
    y1: float
    y2: float

    def __init__(self, width, height):
        super().__init__()

        self.imagewidth = width
        self.imageheight = height
        self.labelimage = qtw.QLabel(self)
        self.image = qtg.QImage(qtc.QSize(self.imagewidth, self.imageheight), qtg.QImage.Format.Format_RGBA8888)
        self.image.fill(qtg.QColor(0, 0, 0))
        self.labelimage.setPixmap(qtg.QPixmap.fromImage(self.image))

        self.x1, self.x2, self.y1, self.y2 = -2, 1, -1, 1

        self.movestart = qtc.QPoint(0, 0)
        self.startcoordinate = qtc.QPoint(0, 0)
        self.oldpos = qtc.QPoint(0, 0)

        self.n_max = 100

        self.gen()


    def gen(self):
        x_s = abs(self.x2 - self.x1) / self.imagewidth
        y_s = abs(self.y2 - self.y1) / self.imageheight

        cn = np.empty([self.imageheight * self.imagewidth], dtype=np.clongdouble)

        # c Zahl ber.

        for x in range(self.imagewidth):
            for y in range(self.imageheight):
                cn[y * self.imagewidth + x] = complex(self.x1 + x * x_s, self.y1 + y * y_s)

        cn_copy = copy.deepcopy(cn)
        two_array = np.zeros([self.imageheight * self.imagewidth], dtype=np.float64) + 2
        counter = np.zeros([self.imageheight * self.imagewidth], dtype=np.uint8)

        # z Zahl ber

        for n in range(self.n_max):
            cn = cn ** 2 + cn_copy
            counter += np.less(cn, two_array)

        max = np.max(counter)
        min = np.min(counter)

        if max == 0:
            max = 1

        counter = (counter - min) / max
        colormap = plt.cm.hsv
        colfloat = colormap(counter)

        colint = np.asarray(colfloat * 255, dtype=np.uint8)
        self.image = qtg.QImage(colint.data.tobytes(), self.imagewidth, self.imageheight,
                                qtg.QImage.Format.Format_RGBA8888)

        self.labelimage.setPixmap(
            qtg.QPixmap.fromImage(self.image).scaled(self.imagewidth, self.imageheight, qtc.Qt.AspectRatioMode.KeepAspectRatio))

        # Farbe ber. eigener version (bevor ich gesehen habe wie es richtig geht)

        # color = []
        #
        # for i in counter:
        #     color.append(int(255 / 100 * i))
        #
        # self.image = qtg.QImage(self.imagewidth, self.imageheight,
        #                         qtg.QImage.Format.Format_RGBA8888)
        #
        # for x in range(self.imagewidth):
        #     for y in range(self.imageheight):
        #         self.image.setPixelColor(x, y, qtg.QColor(color[y * self.imagewidth + x], 0, color[y * self.imagewidth + x]))
        #
        # self.labelimage.setPixmap(qtg.QPixmap.fromImage(self.image).scaled(self.imagewidth, self.imageheight,
        #                                                                    qtc.Qt.AspectRatioMode.KeepAspectRatio))


def main():
    app = qtw.QApplication(sys.argv)
    width = 900
    height = 600
    window = MainWidget(width, height)
    window.setWindowTitle("Mandelbrot")
    window.setFixedWidth(width)
    window.setFixedHeight(height)

    window.setStyleSheet("background: #FFFFFF")

    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
