# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_block.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from block_init import BlockObject
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import pickle

table_widget_id = None
selected_block = None

class Ui_Form_Block(object):
    def __init__(self):
        self.block_list = []
        self._translate = QtCore.QCoreApplication.translate
        global window
        w = QtWidgets.QWidget()
        window = Window()
        window.InitWindow()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 512)
        Form.setMinimumSize(QtCore.QSize(1024, 512))

        # 블럭 컨테이너
        self.gb_block_init = QtWidgets.QGroupBox(Form)
        self.gb_block_init.setGeometry(QtCore.QRect(220, 30, 281, 186))
        font = self.fontsettings_basic()
        self.gb_block_init.setFont(font)
        self.gb_block_init.setObjectName("gb_block_init")
        self.label_blockname = QtWidgets.QLabel(self.gb_block_init)
        self.label_blockname.setGeometry(QtCore.QRect(20, 30, 64, 21))
        font = self.fontsettings_basic()
        self.label_blockname.setFont(font)
        self.label_blockname.setObjectName("label_blockname")
        self.label_set_size = QtWidgets.QLabel(self.gb_block_init)
        self.label_set_size.setGeometry(QtCore.QRect(20, 60, 64, 21))
        font = self.fontsettings_basic()
        self.label_set_size.setFont(font)
        self.label_set_size.setObjectName("label_set_size")
        # 블럭 사이즈 설정
        self.block_size_x = QtWidgets.QSpinBox(self.gb_block_init)
        self.block_size_x.setGeometry(QtCore.QRect(100, 60, 43, 22))
        font = self.fontsettings_basic()
        self.block_size_x.setFont(font)
        self.block_size_x.setObjectName("block_size_x")
        self.block_size_x.setMinimum(1)
        self.block_size_x.setValue(1)
        self.block_size_y = QtWidgets.QSpinBox(self.gb_block_init)
        self.block_size_y.setGeometry(QtCore.QRect(190, 60, 43, 22))
        font = self.fontsettings_basic()
        self.block_size_y.setFont(font)
        self.block_size_y.setObjectName("block_size_y")
        self.block_size_y.setValue(1)
        self.block_size_y.setMinimum(1)
        # 블럭 이름 설정
        self.set_blockname = QtWidgets.QLineEdit(self.gb_block_init)
        self.set_blockname.setGeometry(QtCore.QRect(90, 30, 151, 21))
        font = self.fontsettings_basic()
        self.set_blockname.setFont(font)
        self.set_blockname.setObjectName("set_blockname")
        self.label_set_size2 = QtWidgets.QLabel(self.gb_block_init)
        self.label_set_size2.setGeometry(QtCore.QRect(162, 61, 16, 16))
        font = self.fontsettings_basic()
        self.label_set_size2.setFont(font)
        self.label_set_size2.setObjectName("label_set_size2")
        # 블럭 별명 설정
        self.set_alias = QtWidgets.QLineEdit(self.gb_block_init)
        self.set_alias.setGeometry(QtCore.QRect(90, 100, 151, 21))
        font = self.fontsettings_basic()
        self.set_alias.setFont(font)
        self.set_alias.setObjectName("set_alias")
        self.label_alias = QtWidgets.QLabel(self.gb_block_init)
        self.label_alias.setGeometry(QtCore.QRect(20, 100, 64, 21))
        font = self.fontsettings_basic()
        self.label_alias.setFont(font)
        self.label_alias.setObjectName("label_alias")

        # 생성버튼
        self.btn_new = QtWidgets.QPushButton(self.gb_block_init)
        self.btn_new.setGeometry(QtCore.QRect(20, 140, 101, 28))
        font = self.fontsettings(10)
        self.btn_new.setFont(font)
        self.btn_new.setObjectName("btn_new")
        # 저장버튼
        self.btn_apply = QtWidgets.QPushButton(self.gb_block_init)
        self.btn_apply.setGeometry(QtCore.QRect(132, 140, 61, 28))
        font = self.fontsettings(10)
        self.btn_apply.setFont(font)
        self.btn_apply.setObjectName("btn_apply")
        # 삭제버튼
        self.btn_del = QtWidgets.QPushButton(self.gb_block_init)
        self.btn_del.setGeometry(QtCore.QRect(202, 140, 61, 28))
        font = self.fontsettings(10)
        self.btn_del.setFont(font)
        self.btn_del.setObjectName("btn_del")

        # 미리보기버튼
        self.btn_preview = QtWidgets.QPushButton(Form)
        self.btn_preview.setGeometry(QtCore.QRect(900, 25, 123, 58))
        self.btn_preview.setMaximumSize(QtCore.QSize(93, 28))
        font = self.fontsettings_basic()
        self.btn_preview.setFont(font)
        self.btn_preview.setObjectName("btn_preview")

        # 블럭 id 설정
        self.gb_block_size = QtWidgets.QGroupBox(Form)
        self.gb_block_size.setGeometry(QtCore.QRect(530, 60, 461, 361))
        font = self.fontsettings_basic()
        self.gb_block_size.setFont(font)
        self.gb_block_size.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.gb_block_size.setObjectName("gb_block_size")
        self.tableWidget = QtWidgets.QTableWidget(self.block_size_x.value(), self.block_size_y.value(), self.gb_block_size)
        self.tableWidget.setGeometry(QtCore.QRect(0, 20, 459, 331))
        font = self.fontsettings_basic()
        self.tableWidget.setFont(font)
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(35)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(35)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(35)
        self.tableWidget.verticalHeader().setMinimumSectionSize(35)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        stylesheet = "QHeaderView::section{Background-color:rgb(183, 140, 151); border - radius: 14px;}"
        self.tableWidget.setStyleSheet(stylesheet)

        # 블럭 목록
        self.widget_block_list = QtWidgets.QListWidget(Form)
        self.widget_block_list.setGeometry(QtCore.QRect(20, 30, 171, 421))
        font = self.fontsettings(10)
        self.widget_block_list.setFont(font)
        self.widget_block_list.setObjectName("widget_block_list")
        # for count in range(len(self.block_list)):
        #     print(self.block_list[count])
        #     self.widgetBlockList(self.widget_block_list, self.block_list[count], count)

        # 0타공버튼
        self.btn_punch0 = QtWidgets.QPushButton(Form)
        self.btn_punch0.setGeometry(QtCore.QRect(362, 440, 91, 48))
        font = self.fontsettings()
        self.btn_punch0.setFont(font)
        self.btn_punch0.setObjectName("btn_punch0")
        # 1타공버튼
        self.btn_punch1 = QtWidgets.QPushButton(Form)
        self.btn_punch1.setGeometry(QtCore.QRect(469, 440, 91, 48))
        font = self.fontsettings()
        self.btn_punch1.setFont(font)
        self.btn_punch1.setObjectName("btn_punch1")
        # 2타공버튼
        self.btn_punch2 = QtWidgets.QPushButton(Form)
        self.btn_punch2.setGeometry(QtCore.QRect(576, 440, 91, 48))
        font = self.fontsettings()
        self.btn_punch2.setFont(font)
        self.btn_punch2.setObjectName("btn_punch2")
        # x타공버튼
        self.btn_punchx = QtWidgets.QPushButton(Form)
        self.btn_punchx.setGeometry(QtCore.QRect(683, 440, 91, 48))
        font = self.fontsettings()
        self.btn_punchx.setFont(font)
        self.btn_punchx.setObjectName("btn_punchx")
        # 닫기버튼
        self.btn_close = QtWidgets.QPushButton(Form)
        self.btn_close.setGeometry(QtCore.QRect(880, 440, 111, 41))
        font = self.fontsettings()
        self.btn_close.setFont(font)
        self.btn_close.setObjectName("btn_close")

        self.retranslateUi(Form)
        self.set_blockname.textChanged.connect(self.nameInterlock)
        self.btn_apply.clicked.connect(self.saveBlock)
        self.btn_punch0.clicked.connect(self.punchBlock0)
        self.btn_punch1.clicked.connect(self.punchBlock1)
        self.btn_punch2.clicked.connect(self.punchBlock2)
        self.btn_punchx.clicked.connect(self.punchBlockx)
        self.widget_block_list.itemClicked['QListWidgetItem*'].connect(self.selectBlock)
        self.block_size_x.valueChanged['int'].connect(self.blocksizeControl)
        self.block_size_y.valueChanged['int'].connect(self.blocksizeControl)
        self.btn_new.clicked.connect(self.initBlock)
        self.btn_del.clicked.connect(self.deleteBlock)
        self.btn_preview.clicked.connect(self.preview)
        self.btn_close.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.gb_block_init.setTitle(self._translate("Form", "블럭"))
        self.loadData()
        self.widgetBlockList_reload()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.gb_block_init.setTitle(_translate("Form", "블럭"))
        self.label_blockname.setText(_translate("Form", "블럭이름"))
        self.label_alias.setText(_translate("Form", "블럭별명"))
        self.label_set_size.setText(_translate("Form", "블럭크기"))
        self.label_set_size2.setText(_translate("Form", "x"))
        self.btn_apply.setText(_translate("Form", "저장"))
        self.btn_preview.setText(_translate("Form", "미리보기"))
        self.gb_block_size.setTitle(_translate("Form", "블럭 id 설정 (검정: 0,  회색: 2,  하양: 1,  블럭X: x  입력)"))
        self.tableWidget.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.widget_block_list.isSortingEnabled()
        self.widget_block_list.setSortingEnabled(False)
        self.widget_block_list.setSortingEnabled(__sortingEnabled)
        self.btn_close.setText(_translate("Form", "닫기"))
        self.btn_punch0.setText(_translate("Form", "0 입력"))
        self.btn_punch1.setText(_translate("Form", "1 입력"))
        self.btn_punch2.setText(_translate("Form", "2 입력"))
        self.btn_punchx.setText(_translate("Form", "x 입력"))
        self.btn_del.setText(_translate("Form", "제거"))
        self.btn_new.setText(_translate("Form", "새로만들기"))

    # 가져올 데이터 선택
    def loadData(self):
        try:
            with open('block_info.p', 'rb') as file:
                self.block_list = pickle.load(file)[0]
        except:
            self.block_list = []
        self.widgetBlockList_reload()

    # widget_block_list 선택 시 정보 불러오기
    def selectBlock(self, count=None):
        if type(count) == int:
            self.target = count
        else:
            self.checkToSave()
            self.target = self.widget_block_list.currentRow()

        global selected_block
        selected_block = self.block_list[self.target]

        self.set_blockname.setText(self._translate("Form", "{}".format(selected_block.name)))
        self.block_size_x.setValue(selected_block.size[0])
        self.block_size_y.setValue(selected_block.size[1])
        self.set_alias.setText(selected_block.alias)

        self.blocksizeControl()

    # 블럭 사이즈 테이블 크기 조절
    def blocksizeControl(self):
        size_x = self.block_size_x.value()
        size_y = self.block_size_y.value()
        self.tableWidget.setRowCount(size_x)
        self.tableWidget.setColumnCount(size_y)
        self.tableWidget.setCellWidget(35, 35, QtWidgets.QTextEdit())
        self.tableWidget.resizeColumnsToContents()
        input = str(0)
        for x in range(size_x):
            for y in range(size_y):
                item = QtWidgets.QTableWidgetItem()
                try:
                    item.setText(str(selected_block.id[x][y]))
                except:
                    item.setText(input)
                item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(x, y, item)

    # 블럭 추가
    def initBlock(self):
        id = []
        for x in range(self.block_size_x.value()):
            tmp = []
            for y in range(self.block_size_y.value()):
                try:
                    tmp.append(int(self.tableWidget.item(x, y).text()))
                except:
                    tmp.append('')
            id.append(tmp)
        name = self.set_blockname.text()
        size = [self.block_size_x.value(), self.block_size_y.value()]
        block = BlockObject(name=name, x=size[0], y=size[1], id=id)
        self.block_list.append(block)
        count = len(self.block_list) - 1
        self.widgetBlockList(self.widget_block_list, block, count)
        self.selectBlock(-1)

        self.applyData()

    # 블럭 적용
    def saveBlock(self):
        id = []
        size_x = self.block_size_x.value()
        size_y = self.block_size_y.value()
        for x in range(size_x):
            id_tmp = []
            for y in range(size_y):
                try:
                    id_tmp.append(int(self.tableWidget.item(x, y).text()))
                except:
                    id_tmp.append('')
            id.append(id_tmp)
        # 같은 이름 저장 방지
        for n in self.block_list:
            if self.target != self.block_list.index(n) and self.set_blockname.text() == n.name:
                self.check_error = 1
                break
            else:
                self.check_error = 0
        if self.check_error == 1:
            self.error_dialog()
        else:
            selected_block.name = self.set_blockname.text()
            selected_block.size[0] = size_x
            selected_block.size[1] = size_y
            selected_block.id = id
            selected_block.alias = self.set_alias.text()

        o_count = self.widget_block_list.currentRow()
        self.widgetBlockList_reload(o_count)
        self.selectBlock(count=o_count)

        self.applyData()

    # 저장없이 다른 블럭 눌렀을 때 확인
    def checkToSave(self):
        global selected_block
        try:
            table_id = []
            for x in range(self.tableWidget.rowCount()):
                tmp = []
                for y in range(self.tableWidget.columnCount()):
                    tmp.append(int(self.tableWidget.item(x, y).text()))
                table_id.append(tmp)
            if selected_block.name == self.set_blockname.text() and selected_block.id == table_id and selected_block.size == [
                self.block_size_x.value(), self.block_size_y.value()] and selected_block.alias == self.set_alias.text():
                pass
            else:
                # print(selected_block.name,self.set_blockname.text(),'\n',
                #       selected_block.size,[self.block_size_x.value(), self.block_size_y.value()],'\n',
                #       selected_block.alias,self.set_alias.text(),'\n',
                #       selected_block.id,'\n',
                #       table_id)
                dlg = checkDialog(block=selected_block, name=self.set_blockname.text(), id=table_id,
                                  size=[self.block_size_x.value(), self.block_size_y.value()],
                                  alias=self.set_alias.text())
                dlg.exec_()
                selected_block = dlg.block
            self.applyData()
        except:
            pass


    # 블럭 삭제
    def deleteBlock(self):
        del self.block_list[self.target]
        try:
            self.selectBlock()
        except:
            self.selectBlock(-1)
        self.widgetBlockList_reload()
        self.applyData()

    # 파일에 정보 저장
    def applyData(self):
        with open('block_info.p', 'wb') as file:
            pickle.dump([self.block_list], file)

    # 놀이판에 타공
    def punchBlock0(self):
        selected_tablewidget_items = self.tableWidget.selectedItems()
        for item in selected_tablewidget_items:
            item.setText(str(0))
    def punchBlock1(self):
        selected_tablewidget_items = self.tableWidget.selectedItems()
        for item in selected_tablewidget_items:
            item.setText(str(1))
    def punchBlock2(self):
        selected_tablewidget_items = self.tableWidget.selectedItems()
        for item in selected_tablewidget_items:
            item.setText(str(2))
    def punchBlockx(self):
        selected_tablewidget_items = self.tableWidget.selectedItems()
        for item in selected_tablewidget_items:
            item.setText(str('x'))

    def error_dialog(self):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage('중복된 이름입니다!')
        error_dialog.exec_()

    # 미리보기버튼
    def preview(self):
        id = []
        for x in range(self.block_size_x.value()):
            tmp = []
            for y in range(self.block_size_y.value()):
                try:
                    tmp.append(int(self.tableWidget.item(x, y).text()))
                except:
                    tmp.append('')
            id.append(tmp)
        global table_widget_id, alias
        table_widget_id = id
        alias = self.set_alias.text()

        if selected_block == None:
            pass
        else:
            window.show()

    def fontsettings_basic(self):
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        return font
    def fontsettings(self, size=12):
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        font.setPointSize(size)
        return font

    def widgetBlockList_reload(self, o_count=-1):
        self.widget_block_list.clear()
        for count in range(len(self.block_list)):
            tmp_name = self.block_list[count].name
            self.widgetBlockList(self.widget_block_list, tmp_name, count)
        self.widget_block_list.setCurrentRow = o_count

    def widgetBlockList(self, widget_list, obj, count):
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        widget_list.addItem(item)
        item = widget_list.item(count)
        try:
            item.setText(self._translate("Form", "{}".format(obj.name)))
        except:
            item.setText(self._translate("Form", "{}".format(obj)))

    def nameInterlock(self):
        self.set_alias.setText(self.set_blockname.text())

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Tango"
        self.top = 150
        self.left = 150
        self.width = 840
        self.height = 680

        self.init_pos = 40
        self.xpos = 1
        self.ypos = 1
        self.id = []
        self.color = Qt.white

        self.block_length = 40

        self.block_x = 1
        self.block_y = 1

    def InitWindow(self):
        self.setWindowTitle(self.title)

    def paintEvent(self, event):

        self.setGeometry(self.top, self.left,
                         len(table_widget_id[0])*self.block_length*3.7+self.init_pos,
                         len(table_widget_id)*self.block_length*1.5+self.init_pos)
        # id 위치 표시
        for xpos in range(len(table_widget_id)):
            for ypos in range(len(table_widget_id[0])):
                if table_widget_id[xpos][ypos] == 1:
                    self.drawBlock(xpos, ypos, Qt.white)
                elif table_widget_id[xpos][ypos] == 0:
                    self.drawBlock(xpos, ypos, Qt.black)
                elif table_widget_id[xpos][ypos] == 2:
                    self.drawBlock(xpos, ypos, Qt.gray)
                else:
                    pass

        # 윗면 표시
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        rect = QtCore.QRectF(len(table_widget_id[0])*self.block_length*2+self.block_length, self.block_length,
                               self.block_length * len(table_widget_id[0]), self.block_length * len(table_widget_id))
        painter.setFont(QtGui.QFont("Serif", len(table_widget_id)*2+len(table_widget_id[0])*2))
        painter.drawText(rect, Qt.AlignCenter, "{}".format(alias))
        painter.setPen(Qt.black)
        painter.drawRect(rect)

    def drawBlock(self, xpos, ypos, color):
        block = QtGui.QPainter(self)
        block.setPen(QtGui.QPen(Qt.blue, 2))
        block.setBrush(QtGui.QBrush(color, Qt.SolidPattern))
        block.drawRect(self.block_length + self.init_pos * ypos, self.block_length + self.init_pos * xpos,
                              self.block_length * self.block_x, self.block_length * self.block_y)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

class checkDialog(QtWidgets.QDialog):
    def __init__(self, block, name, id, size, alias):
        super().__init__()
        self.setupUI()
        self.block = block
        self.name = name
        self.id = id
        self.size = size
        self.alias = alias

    def setupUI(self):
        self.setGeometry(600, 400, 300, 100)
        self.setWindowTitle("입력된 정보 저장 확인")

        text = QtWidgets.QLabel("입력한 정보를 저장하시겠습니까?")
        font = self.fontsettings()
        text.setFont(font)
        text.setAlignment(QtCore.Qt.AlignCenter)

        self.pushButton1 = QtWidgets.QPushButton("저장")
        font = self.fontsettings(10)
        self.pushButton1.setFont(font)
        self.pushButton1.clicked.connect(self.pushSaveButtonClicked)
        self.pushButton2 = QtWidgets.QPushButton("취소")
        self.pushButton2.setFont(font)
        self.pushButton2.clicked.connect(self.pushCancelButtonClicked)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(text, 0, 0)
        layout.addWidget(self.pushButton1, 1, 1)
        layout.addWidget(self.pushButton2, 1, 2)

        self.setLayout(layout)

    def pushSaveButtonClicked(self):
        self.block.name = self.name
        self.block.id = self.id
        self.block.size = self.size
        self.block.alias = self.alias
        self.close()

    def pushCancelButtonClicked(self):
        self.close()

    def fontsettings(self, size=12):
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        font.setPointSize(size)
        return font

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Block()
    ui.setupUi(Form)
    Form.show()

    w = QtWidgets.QWidget()
    window = Window()
    window.InitWindow()

    sys.exit(app.exec_())
