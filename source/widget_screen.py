# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from block_init import ScreenObject
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import pickle

table_widget_id = None
selected_screen = None
size_x = 14
size_y = 21

class Ui_Form_Screen(object):
    def __init__(self):
        self.mp3_list = []
        self.screen_list = []
        self._translate = QtCore.QCoreApplication.translate

        global ui
        ui = self

        w = QtWidgets.QWidget()
        self.window = Window()
        self.window.InitWindow()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1197, 800)
        Form.setMinimumSize(QtCore.QSize(1024, 512))

        # 놀이판 설정 groupbox
        self.gb_screen_init = QtWidgets.QGroupBox(Form)
        self.gb_screen_init.setGeometry(QtCore.QRect(20, 20, 271, 341))
        font = self.fontsettings_basic()
        self.gb_screen_init.setFont(font)
        self.gb_screen_init.setObjectName("gb_screen_init")
        # 놀이판 이름 설정
        self.label_screen_name = QtWidgets.QLabel(self.gb_screen_init)
        self.label_screen_name.setGeometry(QtCore.QRect(10, 20, 81, 41))
        font = self.fontsettings_basic()
        self.label_screen_name.setFont(font)
        self.label_screen_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_screen_name.setObjectName("label_screen_name")
        self.set_screen_num = QtWidgets.QLineEdit(self.gb_screen_init)
        self.set_screen_num.setGeometry(QtCore.QRect(100, 30, 141, 21))
        self.set_screen_num.setObjectName("set_screen_num")
        # 인식 범위
        self.label_minmax = QtWidgets.QLabel(self.gb_screen_init)
        self.label_minmax.setGeometry(QtCore.QRect(10, 60, 81, 41))
        font = self.fontsettings_basic()
        self.label_minmax.setFont(font)
        self.label_minmax.setAlignment(QtCore.Qt.AlignCenter)
        self.label_minmax.setObjectName("label_minmax")
        self.spinBox_min = QtWidgets.QSpinBox(self.gb_screen_init)
        self.spinBox_min.setGeometry(QtCore.QRect(102, 70, 61, 22))
        self.spinBox_min.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox_min.setMaximum(10000)
        self.spinBox_min.setObjectName("spinBox_min")
        self.label_minmax_x = QtWidgets.QLabel(self.gb_screen_init)
        self.label_minmax_x.setGeometry(QtCore.QRect(160, 70, 21, 21))
        font = self.fontsettings_basic()
        self.label_minmax_x.setFont(font)
        self.label_minmax_x.setAlignment(QtCore.Qt.AlignCenter)
        self.label_minmax_x.setObjectName("label_minmax_x")
        self.spinBox_max = QtWidgets.QSpinBox(self.gb_screen_init)
        self.spinBox_max.setGeometry(QtCore.QRect(180, 70, 61, 22))
        self.spinBox_max.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox_max.setMaximum(10000)
        self.spinBox_max.setObjectName("spinBox_max")

        self.label_mp3_title = QtWidgets.QLabel(self.gb_screen_init)
        self.label_mp3_title.setGeometry(QtCore.QRect(3, 115, 81, 21))
        font = self.fontsettings_basic()
        self.label_mp3_title.setFont(font)
        self.label_mp3_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mp3_title.setObjectName("label_mp3_title")
        self.label_mp3_lang = QtWidgets.QLabel(self.gb_screen_init)
        self.label_mp3_lang.setGeometry(QtCore.QRect(83, 115, 30, 21))
        font = self.fontsettings_basic()
        self.label_mp3_lang.setFont(font)
        self.label_mp3_lang.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mp3_lang.setObjectName("label_mp3_lang")
        self.label_mp3_address = QtWidgets.QLabel(self.gb_screen_init)
        self.label_mp3_address.setGeometry(QtCore.QRect(105, 115, 141, 21))
        font = self.fontsettings_basic()
        self.label_mp3_address.setFont(font)
        self.label_mp3_address.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mp3_address.setObjectName("label_mp3_address")
        # 음원
        self.mp3_scroll_area = QtWidgets.QScrollArea(self.gb_screen_init)
        self.mp3_scroll_area.setGeometry(QtCore.QRect(5, 140, 261, 150))
        self.mp3_scroll_area.setWidgetResizable(True)
        self.widget = QtWidgets.QWidget()
        self.mp3_scroll_area.setWidget(self.widget)
        self.mp3_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mp3_layout = QtWidgets.QVBoxLayout(self.widget)
        self.mp3_layout.setContentsMargins(0, 0, 0, 0)
        self.loadMp3Box()
        # 음원 추가버튼
        self.btn_new_mp3 = QtWidgets.QPushButton(self.gb_screen_init)
        self.btn_new_mp3.setGeometry(QtCore.QRect(23, 300, 101, 28))
        font = self.fontsettings_basic()
        font.setPointSize(10)
        self.btn_new_mp3.setFont(font)
        self.btn_new_mp3.setObjectName("btn_new_mp3")
        # 음원 삭제버튼
        self.btn_del_mp3 = QtWidgets.QPushButton(self.gb_screen_init)
        self.btn_del_mp3.setGeometry(QtCore.QRect(145, 300, 101, 28))
        font = self.fontsettings_basic()
        font.setPointSize(10)
        self.btn_del_mp3.setFont(font)
        self.btn_del_mp3.setObjectName("btn_del_mp3")

        # 생성버튼
        self.btn_new = QtWidgets.QPushButton(Form)
        self.btn_new.setGeometry(QtCore.QRect(30, 370, 101, 28))
        font = self.fontsettings_basic()
        font.setPointSize(10)
        self.btn_new.setFont(font)
        self.btn_new.setObjectName("btn_new")
        # 저장 버튼
        self.btn_apply = QtWidgets.QPushButton(Form)
        self.btn_apply.setGeometry(QtCore.QRect(142, 370, 61, 28))
        font = self.fontsettings_basic()
        font.setPointSize(10)
        self.btn_apply.setFont(font)
        self.btn_apply.setObjectName("btn_apply")
        # 삭제버튼
        self.btn_del = QtWidgets.QPushButton(Form)
        self.btn_del.setGeometry(QtCore.QRect(214, 370, 61, 28))
        font = self.fontsettings_basic()
        font.setPointSize(10)
        self.btn_del.setFont(font)
        self.btn_del.setObjectName("btn_del")

        # 미리보기버튼
        self.btn_preview = QtWidgets.QPushButton(Form)
        self.btn_preview.setGeometry(QtCore.QRect(1070, 25, 117, 38))
        self.btn_preview.setMaximumSize(QtCore.QSize(93, 28))
        font = self.fontsettings_basic()
        self.btn_preview.setFont(font)
        self.btn_preview.setObjectName("btn_preview")

        # 타공위치 설정
        self.gb_block_size = QtWidgets.QGroupBox(Form)
        self.gb_block_size.setGeometry(QtCore.QRect(310, 60, 881, 631))
        font = self.fontsettings_basic()
        self.gb_block_size.setFont(font)
        self.gb_block_size.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.gb_block_size.setObjectName("gb_block_size")
        self.tableWidget = QtWidgets.QTableWidget(self.gb_block_size)
        self.tableWidget.setGeometry(QtCore.QRect(0, 25, 867, 586))
        font = self.fontsettings_basic()
        self.tableWidget.setFont(font)
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(14)
        self.tableWidget.setColumnCount(21)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(40)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setMinimumSectionSize(40)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        stylesheet = "QHeaderView::section{Background-color:rgb(183, 140, 151); border - radius: 14px;}"
        self.tableWidget.setStyleSheet(stylesheet)
        self.tableWidget.setRowCount(size_x)
        self.tableWidget.setColumnCount(size_y)
        self.tableWidget.setCellWidget(40,40, QtWidgets.QTextEdit())
        self.tableWidget.resizeColumnsToContents()

        # 놀이판 목록
        self.gb_screen_init_2 = QtWidgets.QGroupBox(Form)
        self.gb_screen_init_2.setGeometry(QtCore.QRect(20, 410, 271, 381))
        font = self.fontsettings_basic()
        self.gb_screen_init_2.setFont(font)
        self.gb_screen_init_2.setObjectName("gb_screen_init_2")
        # 목록 칸 생성
        self.widget_screen_list = QtWidgets.QListWidget(self.gb_screen_init_2)
        self.widget_screen_list.setGeometry(QtCore.QRect(50, 30, 171, 325))
        font = self.fontsettings(10)
        self.widget_screen_list.setFont(font)
        self.widget_screen_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.widget_screen_list.setItemAlignment(QtCore.Qt.AlignCenter)
        self.widget_screen_list.setObjectName("widget_screen_list")

        # 닫기버튼
        self.btn_close = QtWidgets.QPushButton(Form)
        self.btn_close.setGeometry(QtCore.QRect(1060, 735, 111, 41))
        font = self.fontsettings()
        self.btn_close.setFont(font)
        self.btn_close.setObjectName("btn_close")
        # 타공버튼
        self.btn_punch = QtWidgets.QPushButton(Form)
        self.btn_punch.setGeometry(QtCore.QRect(650, 715, 151, 61))
        font = self.fontsettings()
        self.btn_punch.setFont(font)
        self.btn_punch.setObjectName("btn_punch")
        # txt 출력 버튼
        self.btn_output = QtWidgets.QPushButton(Form)
        self.btn_output.setGeometry(QtCore.QRect(930, 735, 111, 41))
        font = self.fontsettings()
        self.btn_output.setFont(font)
        self.btn_output.setObjectName("btn_output")

        self.retranslateUi(Form)
        self.btn_new_mp3.clicked.connect(self.initMp3)
        self.btn_del_mp3.clicked.connect(self.delMp3)
        self.btn_new.clicked.connect(self.initScreen)
        self.btn_del.clicked.connect(self.deleteScreen)
        self.btn_punch.clicked.connect(self.punchScreen)
        self.btn_output.clicked.connect(self.output)
        self.btn_close.clicked.connect(Form.close)
        self.btn_apply.clicked.connect(self.saveScreen)
        self.widget_screen_list.itemClicked['QListWidgetItem*'].connect(self.selectScreen)
        self.tableWidget.itemChanged['QTableWidgetItem*'].connect(self.tableItemChanged)
        self.btn_preview.clicked.connect(self.preview)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.loadData()
        self.blocksizeLoad(self.tableWidget)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.gb_screen_init.setTitle(_translate("Form", "놀이판"))
        self.label_screen_name.setText(_translate("Form", "놀이판 \n식별번호"))
        self.label_minmax.setText(_translate("Form", "낱말카드 \n인식 범위"))
        self.label_minmax_x.setText(_translate("Form", "~"))
        self.label_mp3_title.setText(_translate("Form", "음원 항목"))
        self.label_mp3_lang.setText(_translate("Form", "언어"))
        self.label_mp3_address.setText(_translate("Form", "음원 주소"))
        self.btn_apply.setText(_translate("Form", "저장"))
        self.btn_preview.setText(_translate("Form", "미리보기"))
        self.gb_block_size.setTitle(_translate("Form", "타공위치 (하양: 1,  검정: 0  입력)"))
        self.tableWidget.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.gb_screen_init_2.setTitle(_translate("Form", "놀이판 목록"))
        self.btn_del.setText(_translate("Form", "제거"))
        self.btn_new.setText(_translate("Form", "새로만들기"))
        self.btn_new_mp3.setText(_translate("Form", "음원 목록 추가"))
        self.btn_del_mp3.setText(_translate("Form", "음원 목록 삭제"))
        __sortingEnabled = self.widget_screen_list.isSortingEnabled()
        self.widget_screen_list.setSortingEnabled(False)
        self.widget_screen_list.setSortingEnabled(__sortingEnabled)
        self.btn_close.setText(_translate("Form", "닫기"))
        self.btn_punch.setText(_translate("Form", "타공"))
        self.btn_output.setText(_translate("Form", "txt출력"))


    # 가져올 데이터 선택
    def loadData(self):
        try:
            with open('screen_info.p', 'rb') as file:
                self.screen_list = pickle.load(file)[0]
        except:
            print('failed to load data')
            self.screen_list = []
        self.widgetScreenList_reload()

    # widget_screen_list 선택 시 정보 불러오기
    def selectScreen(self, count=None):
        # self.target = self.widget_screen_list.currentRow()
        if type(count) == int:
            self.target = count
        else:
            self.checkToSave()
            self.target = self.widget_screen_list.currentRow()

        global selected_screen
        selected_screen = self.screen_list[self.target]

        self.set_screen_num.setText(self._translate("Form", "{}".format(selected_screen.name)))
        self.spinBox_min.setValue(selected_screen.minmax[0])
        self.spinBox_max.setValue(selected_screen.minmax[1])
        self.loadMp3()

        self.blocksizeLoad(selected_screen)

    # 저장된 블럭 값 가져오기
    def blocksizeLoad(self, tablewidget):
        self.tableWidget.setRowCount(size_x)
        self.tableWidget.setColumnCount(size_y)
        self.tableWidget.setCellWidget(40, 40, QtWidgets.QTextEdit())
        self.tableWidget.resizeColumnsToContents()
        input = str(0)
        count = 0
        for x in range(size_x):
            for y in range(size_y):
                item = QtWidgets.QTableWidgetItem()
                try:
                    item.setText(str(table_widget_id[count]))
                except:
                    try:
                        item.setText(str(tablewidget.id[count]))
                    except:
                        item.setText(input)
                item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(x, y, item)
                try:
                    if self.tableWidget.item(x, y).text() == '0':
                        self.tableWidget.item(x, y).setBackground(Qt.black)
                except:
                    pass
                count += 1


    # 타공시 색변경
    def tableItemChanged(self):
        for item in self.tableWidget.selectedItems():
            if item.text() == '1':
                print(self.tableWidget.row(item))
                if self.tableWidget.row(item) % 2 == 1:
                    item.setBackground(QtGui.QColor(244,244,244))
                else:
                    item.setBackground(Qt.white)

    # 놀이판 추가
    def initScreen(self):
        id = []
        for x in range(size_x):
            for y in range(size_y):
                try:
                    id.append(int(self.tableWidget.item(x, y).text()))
                except:
                    id.append(0)
        name = self.set_screen_num.text()
        size = [size_x, size_y]
        minmax = [self.spinBox_min.value(), self.spinBox_max.value()]
        mp3 = []
        for obj in self.mp3_list:
            tmp = []
            for count in obj:
                tmp.append(count.text())
            mp3.append(tmp)
        screen = ScreenObject(name=name, x=size[0], y=size[1], id=id, minmax=minmax, mp3=mp3)
        self.screen_list.append(screen)
        count = len(self.screen_list)-1
        self.widgetBlockList(self.widget_screen_list, screen, count)
        self.selectScreen(-1)

        self.applyData()

    # 놀이판 삭제
    def deleteScreen(self):
        try:
            del self.screen_list[self.target]
            self.selectScreen()
        except:
            pass
        self.widgetScreenList_reload()

        self.applyData()

    # 놀이판 적용
    def saveScreen(self):
        id = []
        for x in range(size_x):
            for y in range(size_y):
                id.append(int(self.tableWidget.item(x, y).text()))
        # 같은 이름 중복 제거
        for n in self.screen_list:
            if self.target != self.screen_list.index(n) and self.set_screen_num.text() == n.name:
                self.check_error = 1
                break
            else:
                self.check_error = 0
        if self.check_error == 1:
            self.error_dialog()
        elif self.check_error == 0:
            selected_screen.name = self.set_screen_num.text()
            selected_screen.size = [size_x, size_y]
            selected_screen.id = id
            selected_screen.minmax = [self.spinBox_min.value(), self.spinBox_max.value()]
            mp3 = []
            for obj in self.mp3_list:
                tmp = []
                for count in obj:
                    tmp.append(count.text())
                mp3.append(tmp)
            selected_screen.mp3 = mp3
        count = self.widget_screen_list.currentRow()
        self.widgetScreenList_reload(count)
        self.selectScreen(count=count)

        self.applyData()

    # 저장없이 다른 놀이판 눌렀을 때 확인
    def checkToSave(self):
        global selected_screen
        try:
            table_id = []
            for x in range(14):
                for y in range(21):
                    table_id.append(int(self.tableWidget.item(x, y).text()))
            mp3 = []
            for obj in self.mp3_list:
                tmp = []
                for count in obj:
                    tmp.append(count.text())
                mp3.append(tmp)
            if selected_screen.name == self.set_screen_num.text() and selected_screen.id == table_id and selected_screen.minmax == [self.spinBox_min.value(), self.spinBox_max.value()] and selected_screen.mp3 == mp3:
                pass
            else:
                dlg = checkDialog(screen=selected_screen, name=self.set_screen_num.text(), id=table_id, minmax=[self.spinBox_min.value(), self.spinBox_max.value()], mp3=mp3)
                dlg.exec_()
                selected_screen = dlg.screen
            self.applyData()
        except:
            pass

    # 파일에 정보 저장
    def applyData(self):
        with open('screen_info.p', 'wb') as file:
            pickle.dump([self.screen_list], file)

    def widgetScreenList_reload(self, o_count=-1):
        self.widget_screen_list.clear()
        for count in range(len(self.screen_list)):
            tmp_name = self.screen_list[count].name
            self.widgetBlockList(self.widget_screen_list, tmp_name, count)
        self.widget_screen_list.setCurrentRow = o_count

    def widgetBlockList(self, widget_list, obj, count):
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.widget_screen_list.addItem(item)
        item = widget_list.item(count)
        try:
            item.setText(self._translate("Form", "{}".format(obj.name)))
        except:
            item.setText(self._translate("Form", "{}".format(obj)))

    # 놀이판에 타공
    def punchScreen(self):
        selected_tablewidget_items = self.tableWidget.selectedItems()
        for item in selected_tablewidget_items:
            item.setText(str(1))

    def error_dialog(self):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage('중복된 이름입니다!')
        error_dialog.exec_()

    def preview(self):
        id = []
        for x in range(14):
            for y in range(21):
                id.append(int(self.tableWidget.item(x, y).text()))
        global table_widget_id
        table_widget_id = id

        if selected_screen == None:
            pass
        else:
            self.window.show()
        # self.blocksizeLoad(self.tableWidget)

    # txt 출력
    def output(self):
        screen = '{}_screen.txt'.format(selected_screen.name)
        screen_contents = self.output_id(selected_screen.id)
        with open(screen, 'wt') as f:
            f.write(screen_contents)

        ready = '{}_ready.txt'.format(selected_screen.name)
        ready_contents = self.output_mp3(selected_screen.mp3)
        with open(ready, 'wt') as f:
            f.write(ready_contents)

    # 음원항목 추가
    def initMp3(self):
        self.loadMp3Box()

    # 음원박스 추가
    def loadMp3Box(self):
        mp3groupbox = QtWidgets.QGroupBox()
        mp3groupbox.setStyleSheet("border:none")
        layout_groupbox = QtWidgets.QHBoxLayout(mp3groupbox)
        layout_groupbox.setContentsMargins(0,0,0,0)

        label_title = QtWidgets.QLineEdit(mp3groupbox)
        label_title.setMaximumWidth(90)
        layout_groupbox.addWidget(label_title)
        label_lang = QtWidgets.QLineEdit(mp3groupbox)
        label_lang.setMaximumWidth(40)
        layout_groupbox.addWidget(label_lang)
        label_address = QtWidgets.QLineEdit(mp3groupbox)
        layout_groupbox.addWidget(label_address)
        self.mp3_layout.addWidget(mp3groupbox)

        mp3box = [label_lang, label_title, label_address]
        self.mp3_list.append(mp3box)

    # 음원항목 불러오기
    def loadMp3(self):
        # mp3 scrollarea reset
        self.widget = QtWidgets.QWidget()
        self.mp3_scroll_area.setWidget(self.widget)
        self.mp3_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mp3_layout = QtWidgets.QVBoxLayout(self.widget)
        self.mp3_layout.setContentsMargins(0, 0, 0, 0)
        # mp3 line edit에 정보 로드
        self.mp3_list = []
        for obj in selected_screen.mp3:
            self.loadMp3Box()
            for count in range(3):
                self.mp3_list[-1][count].setText(self._translate("Form", "{}".format(obj[count])))

    # 음원항목 삭제
    def delMp3(self):
        # mp3 정보 임시 저장
        mp3 = []
        for obj in self.mp3_list:
            tmp = []
            for count in obj:
                tmp.append([count,count.text()])
            mp3.append(tmp)
        # mp3 scrollarea reset
        self.widget = QtWidgets.QWidget()
        self.mp3_scroll_area.setWidget(self.widget)
        self.mp3_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mp3_layout = QtWidgets.QVBoxLayout(self.widget)
        self.mp3_layout.setContentsMargins(0, 0, 0, 0)
        # mp3 line edit에 정보 로드
        self.mp3_list = []
        for obj in mp3:
            if mp3.index(obj) == len(mp3) - 1:
                break
            else:
                self.loadMp3Box()
                for count in range(3):
                    self.mp3_list[-1][count].setText(self._translate("Form", "{}".format(obj[count][1])))

    # 음원 출력 형식
    def output_mp3(self, mp3_tmp):
        mp3_count = []
        for count in mp3_tmp:
            if len(count[-1]) > 2:
                mp3_count.append(count[-1].count(',') + 1)
            else:
                mp3_count.append(0)
        mp3_contents = 'wordcard,none,0,\n'
        mp3_save_list = ['wordcard,min,{},\n',
                         'wordcard,max,{},\n',]
        mp3_info = '{},{},{},{},\n'
        mp3_save_list2 = []
        for count in range(len(mp3_tmp)):
           mp3_save_list2.append(mp3_info)
        mp3_save_list += mp3_save_list2

        count = 0
        new_count = 0
        for i in mp3_save_list:
            if count == 0:
                mp3_contents += i.format(selected_screen.minmax[0])
            elif count == 1:
                mp3_contents += i.format(selected_screen.minmax[1])
            else:
                mp3_contents += i.format(mp3_tmp[new_count][1], mp3_tmp[new_count][0], mp3_count[new_count], mp3_tmp[new_count][2])
                new_count += 1
            count += 1

        return mp3_contents

    # id 출력 형식
    def output_id(self, id):
        count = 0
        output = ''
        for ypos in range(size_x):
            output += '\n'
            for xpos in range(size_y):
                # 임시로 초록색 -> 검은색
                if id[count] == 2:
                    output += str(1) + ','
                else:
                    output += str(id[count]) + ','
                count += 1
        output = output.lstrip('\n')
        return output

    def fontsettings_basic(self):
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        return font
    def fontsettings(self, size=12):
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        font.setPointSize(size)
        return font


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Tango"
        self.top = 150
        self.left = 150
        self.width = 840
        self.height = 560

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
        self.setGeometry(self.top, self.left, self.width, self.height)

    def paintEvent(self, event):
        # global screen
        # screen
        screen = QtGui.QPainter(self)
        screen.setBrush(QtGui.QBrush(Qt.black, Qt.SolidPattern))
        screen.drawRect(0, 0, self.block_length * 21, self.block_length * 14)

        inline = QtGui.QPen(Qt.blue, 1)
        screen.setPen(inline)
        for i in range(20):
            screen.drawLine(self.init_pos*(1+i), 0, self.init_pos*(1+i), self.init_pos*14)
        for i in range(13):
            screen.drawLine(0, self.init_pos * (1 + i), self.init_pos * 21, self.init_pos * (1 + i))

        count = 0
        for xpos in range(14):
            for ypos in range(21):
                if table_widget_id[count] == 1:
                    self.drawBlock(ypos, xpos, self.color)
                count += 1

        # count = 0
        # output = ''
        # for ypos in range(14):
        #     output += '\n'
        #     for xpos in range(21):
        #         # 임시로 초록색 -> 검은색
        #         if selected_screen.id[count] == 2:
        #             output += str(1) + ', '
        #         else:
        #             output += str(selected_screen.id[count]) + ', '
        #         count += 1
        # output = output.lstrip('\n')
        # print(output)

    def drawBlock(self, xpos, ypos, color):
        # screen
        block = QtGui.QPainter(self)
        # block
        block.setBrush(QtGui.QBrush(color, Qt.SolidPattern))
        block.drawRect(self.init_pos * xpos, self.init_pos * ypos, self.block_length * self.block_x,
                       self.block_length * self.block_y)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, e):
        global table_widget_id
        table_widget_id = None

class checkDialog(QtWidgets.QDialog):
    def __init__(self, screen, name, id, minmax, mp3):
        super().__init__()
        self.setupUI()
        self.screen = screen
        self.name = name
        self.id = id
        self.minmax = minmax
        self.mp3 = mp3

    def setupUI(self):
        self.setGeometry(600, 400, 300, 100)
        self.setWindowTitle("변경된 정보 저장 확인")

        text = QtWidgets.QLabel("변경한 정보를 저장하시겠습니까?")
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
        self.screen.name = self.name
        self.screen.id = self.id
        self.screen.minmax = self.minmax
        self.screen.mp3 = self.mp3
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
    ui = Ui_Form_Screen()
    ui.setupUi(Form)
    Form.show()

    w = QtWidgets.QWidget()
    window = Window()
    window.InitWindow()


    sys.exit(app.exec_())
