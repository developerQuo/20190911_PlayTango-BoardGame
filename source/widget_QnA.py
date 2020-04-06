# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_QnA.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from block_init import QuestionObject, AnswerObject, Mp3Object
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QEasingCurve, QFileInfo, QLineF, QMimeData,
                          QParallelAnimationGroup, QPoint, QPointF, QPropertyAnimation, qrand,
                          QRectF, qsrand, Qt, QTime)
from PyQt5.QtGui import (QBrush, QColor, QDrag, QImage, QPainter, QPen,
                         QPixmap, QTransform)
from PyQt5.QtWidgets import (QApplication, QGraphicsItem, QGraphicsObject,
                             QGraphicsScene, QGraphicsView)
import pickle
import ast
import traceback, sys

loaded_blocks = []
standard_length = 32
question_scene = None
answer_scene = None
question_obj = []
answer_obj = []
selected_question_obj = None
changed_question_scene = None
selected_answer_obj = None
changed_answer_scene = None
class Ui_widget_QnA(object):
    def __init__(self):
        self.question_list = []
        self.answer_list = []
        self.mp3_list = []
        self.mp3_line_edit_list = []

        self.target = None

        self._translate = QtCore.QCoreApplication.translate
        self.font_basic = self.fontsettings_basic()
        self.font_basic2 = self.fontsettings_basic2()
        self.font = self.fontsettings()

        global ui
        ui = self


    def setupUi(self, widget_QnA):
        widget_QnA.setObjectName("widget_QnA")
        widget_QnA.resize(1029, 750)
        self.gridLayout = QtWidgets.QGridLayout(widget_QnA)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_bottom = QtWidgets.QHBoxLayout()
        self.horizontalLayout_bottom.setObjectName("horizontalLayout_bottom")
        self.btn_select_block = QtWidgets.QPushButton(widget_QnA)
        self.btn_select_block.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_select_block.setFont(self.font)
        self.btn_select_block.setObjectName("btn_select_block")
        self.btn_select_block.setMaximumSize(QtCore.QSize(100, 50))
        self.horizontalLayout_bottom.addWidget(self.btn_select_block)

        # 블럭 graphicsview
        self.graphicsView_blocks = QtWidgets.QGraphicsView(widget_QnA)
        # self.graphicsView_blocks.setGeometry(QtCore.QRect(0, 0, 303, 45))
        self.graphicsView_blocks.setMinimumSize(QtCore.QSize(350, 100))
        self.graphicsView_blocks.setMaximumSize(QtCore.QSize(16666666, 100))
        self.graphicsView_blocks.setAlignment(QtCore.Qt.AlignLeft)
        self.graphicsView_blocks.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.graphicsView_blocks.setObjectName("graphicsView_blocks")
        self.graphicsView_blocks.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsView_blocks.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.horizontalLayout_bottom.addWidget(self.graphicsView_blocks)

        self.btn_output = QtWidgets.QPushButton(widget_QnA)
        self.btn_output.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_output.setFont(self.font)
        self.btn_output.setObjectName("btn_output")
        self.btn_output.setMaximumSize(QtCore.QSize(100, 50))
        self.horizontalLayout_bottom.addWidget(self.btn_output)
        self.btn_cancel = QtWidgets.QPushButton(widget_QnA)
        self.btn_cancel.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_cancel.setMaximumSize(QtCore.QSize(100, 50))
        self.btn_cancel.setFont(self.font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_bottom.addWidget(self.btn_cancel)
        self.btn_ok = QtWidgets.QPushButton(widget_QnA)
        self.btn_ok.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_ok.setMaximumSize(QtCore.QSize(100, 50))
        self.btn_ok.setFont(self.font)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout_bottom.addWidget(self.btn_ok)
        self.gridLayout.addLayout(self.horizontalLayout_bottom, 2, 0, 1, 1)
        self.gridLayout_mid = QtWidgets.QGridLayout()
        self.gridLayout_mid.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_mid.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_mid.setVerticalSpacing(7)
        self.gridLayout_mid.setObjectName("gridLayout_mid")
        self.tab_widget = QtWidgets.QTabWidget(widget_QnA)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_widget.sizePolicy().hasHeightForWidth())
        self.tab_widget.setSizePolicy(sizePolicy)
        self.tab_widget.setSizeIncrement(QtCore.QSize(0, 0))
        font = self.font_basic
        font.setFamily("1훈정글북 R")
        self.tab_widget.setFont(font)
        self.tab_widget.setTabsClosable(False)
        self.tab_widget.setMovable(False)
        self.tab_widget.setTabBarAutoHide(False)
        self.tab_widget.setObjectName("tab_widget")

        # 문제
        self.tab_question_3 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_question_3.sizePolicy().hasHeightForWidth())
        self.tab_question_3.setSizePolicy(sizePolicy)
        self.tab_question_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.tab_question_3.setBaseSize(QtCore.QSize(0, 0))
        self.tab_question_3.setObjectName("tab_question_3")
        self.widget_question_list = QtWidgets.QListWidget(self.tab_question_3)
        self.widget_question_list.setMinimumSize(QtCore.QSize(0, 248))
        self.widget_question_list.setMaximumSize(QtCore.QSize(181, 16777215))
        self.widget_question_list.setObjectName("widget_question_list")
        self.graphicsView_question = QtWidgets.QGraphicsView(self.tab_question_3)
        sizePolicy_q = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy_q.setHorizontalStretch(0)
        sizePolicy_q.setVerticalStretch(0)
        sizePolicy_q.setHeightForWidth(self.graphicsView_question.sizePolicy().hasHeightForWidth())
        self.graphicsView_question.setSizePolicy(sizePolicy_q)
        self.graphicsView_question.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView_question.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.graphicsView_question.setObjectName("graphicsView_question")
        self.graphicsView_question.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsView_question.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.graphicsView_question.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)

        # 문제 컨트롤박스
        self.groupBox = QtWidgets.QGroupBox(self.tab_question_3)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setMaximumSize(QtCore.QSize(121, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        # 놀이판선택
        self.label_select_screen = QtWidgets.QLabel(self.groupBox)
        self.label_select_screen.setMinimumSize(QtCore.QSize(67, 0))
        self.label_select_screen.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_select_screen.setFont(self.font_basic2)
        self.label_select_screen.setAlignment(QtCore.Qt.AlignCenter)
        self.label_select_screen.setObjectName("label_select_screen")
        self.verticalLayout.addWidget(self.label_select_screen)
        self.comboBox_select_screen = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_select_screen.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_select_screen.setObjectName("comboBox_select_screen")
        self.verticalLayout.addWidget(self.comboBox_select_screen)
        self.label_mid_blank = QtWidgets.QLabel(self.groupBox)
        self.label_mid_blank.setObjectName("label_mid_blank1")
        self.verticalLayout.addWidget(self.label_mid_blank)
        self.label_mid_blank = QtWidgets.QLabel(self.groupBox)
        self.label_mid_blank.setObjectName("label_mid_blank")
        self.verticalLayout.addWidget(self.label_mid_blank)
        self.label_groupbox = QtWidgets.QLabel(self.groupBox)
        self.label_groupbox.setObjectName("label_groupbox")
        self.verticalLayout.addWidget(self.label_groupbox)
        # 문제 생성 버튼
        self.btn_init_question = QtWidgets.QPushButton(self.groupBox)
        self.btn_init_question.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_init_question.setFont(self.font)
        self.btn_init_question.setObjectName("btn_init_question")
        self.verticalLayout.addWidget(self.btn_init_question)
        # 문제 저장 버튼
        self.btn_save_question = QtWidgets.QPushButton(self.groupBox)
        self.btn_save_question.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_save_question.setFont(self.font)
        self.btn_save_question.setObjectName("btn_save_question")
        self.verticalLayout.addWidget(self.btn_save_question)
        # 문제 삭제 버튼
        self.btn_delete_question = QtWidgets.QPushButton(self.groupBox)
        self.btn_delete_question.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_delete_question.setFont(self.font)
        self.btn_delete_question.setObjectName("btn_delete_question")
        self.verticalLayout.addWidget(self.btn_delete_question)
        # 문제 탭 레이아웃
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_question_3)
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_5.setContentsMargins(-1, 11, -1, 11)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget_question_list, 0, 1, 3, 1)
        self.gridLayout_5.addWidget(self.graphicsView_question, 0, 2, 3, 1)

        self.tab_widget.addTab(self.tab_question_3, "")

        # 정답
        self.tab_Answer_3 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_Answer_3.sizePolicy().hasHeightForWidth())
        self.tab_Answer_3.setSizePolicy(sizePolicy)
        self.tab_Answer_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.tab_Answer_3.setBaseSize(QtCore.QSize(0, 0))
        self.tab_Answer_3.setObjectName("tab_Answer_3")
        self.widget_answer_list = QtWidgets.QListWidget(self.tab_Answer_3)
        self.widget_answer_list.setMinimumSize(QtCore.QSize(0, 248))
        self.widget_answer_list.setMaximumSize(QtCore.QSize(181, 16777215))
        self.widget_answer_list.setObjectName("widget_answer_list")
        self.graphicsView_answer = QtWidgets.QGraphicsView(self.tab_Answer_3)
        sizePolicy_a = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy_a.setHorizontalStretch(0)
        sizePolicy_a.setVerticalStretch(0)
        sizePolicy_a.setHeightForWidth(self.graphicsView_answer.sizePolicy().hasHeightForWidth())
        self.graphicsView_answer.setSizePolicy(sizePolicy_a)
        self.graphicsView_answer.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView_answer.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.graphicsView_answer.setObjectName("graphicsView_answer")
        self.graphicsView_answer.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsView_answer.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.graphicsView_answer.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)

        # 정답 컨트롤박스
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_Answer_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setMaximumSize(QtCore.QSize(121, 16777215))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # 문제선택
        self.label_select_question = QtWidgets.QLabel(self.groupBox_2)
        self.label_select_question.setMinimumSize(QtCore.QSize(67, 0))
        self.label_select_question.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_select_question.setFont(font)
        self.label_select_question.setAlignment(QtCore.Qt.AlignCenter)
        self.label_select_question.setObjectName("label_select_question")
        self.verticalLayout_2.addWidget(self.label_select_question)
        self.comboBox_select_question = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_select_question.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_select_question.setObjectName("comboBox_select_question")
        self.verticalLayout_2.addWidget(self.comboBox_select_question)
        self.tab_widget.addTab(self.tab_Answer_3, "")
        self.label_mid_balank = QtWidgets.QLabel(self.groupBox_2)
        self.label_mid_balank.setObjectName("label_mid_balank")
        self.verticalLayout_2.addWidget(self.label_mid_balank)
        self.label_mid_balank = QtWidgets.QLabel(self.groupBox_2)
        self.label_mid_balank.setObjectName("label_mid_balank")
        self.verticalLayout_2.addWidget(self.label_mid_balank)
        self.label_groupbox_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_groupbox_2.setObjectName("label_groupbox_2")
        self.verticalLayout_2.addWidget(self.label_groupbox_2)
        # 정답 생성 버튼
        self.btn_init_answer = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_init_answer.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_init_answer.setFont(self.font)
        self.btn_init_answer.setObjectName("btn_init_answer")
        self.verticalLayout_2.addWidget(self.btn_init_answer)
        # 정답 저장 버튼
        self.btn_save_answer = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_save_answer.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_save_answer.setFont(self.font)
        self.btn_save_answer.setObjectName("btn_save_answer")
        self.verticalLayout_2.addWidget(self.btn_save_answer)
        # 정답 삭제 버튼
        self.btn_delete_answer = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_delete_answer.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_delete_answer.setFont(self.font)
        self.btn_delete_answer.setObjectName("btn_delete_answer")
        self.verticalLayout_2.addWidget(self.btn_delete_answer)
        # 정답 탭 레이아웃
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_Answer_3)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(-1, 11, -1, 11)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget_answer_list, 0, 1, 3, 1)
        self.gridLayout_4.addWidget(self.graphicsView_answer, 0, 2, 3, 1)

        # 음원 탭
        self.tab_mp3_3 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_mp3_3.sizePolicy().hasHeightForWidth())
        self.tab_mp3_3.setSizePolicy(sizePolicy)
        self.tab_mp3_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.tab_mp3_3.setBaseSize(QtCore.QSize(0, 0))
        self.tab_mp3_3.setObjectName("tab_mp3_3")
        self.widget_mp3_list = QtWidgets.QListWidget(self.tab_mp3_3)
        self.widget_mp3_list.setMaximumSize(QtCore.QSize(181, 16777215))
        self.widget_mp3_list.setObjectName("widget_mp3_list")


        self.groupBox_mp3_setting = QtWidgets.QGroupBox(self.tab_mp3_3)
        self.groupBox_mp3_setting.setFont(self.font)
        self.groupBox_mp3_setting.setObjectName("groupBox_mp3_setting")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_mp3_setting)
        self.gridLayout_7.setObjectName("gridLayout_7")

        # mp3 groupbox
        self.mp3_groupbox = QtWidgets.QGroupBox(self.groupBox_mp3_setting)
        self.mp3_groupbox.setStyleSheet("border:none")
        # self.mp3_groupbox.setM
        # self.mp3_groupbox.setWidgetResizable(True)
        # self.mp3_groupbox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mp3_layout = QtWidgets.QHBoxLayout(self.mp3_groupbox)
        self.mp3_layout.setContentsMargins(0, 0, 0, 0)
        self.label_mp3_titles1 = QtWidgets.QLabel(self.groupBox_mp3_setting)
        self.label_mp3_titles1.setGeometry(QtCore.QRect(3, 115, 81, 21))
        font = self.fontsettings_basic()
        self.label_mp3_titles1.setFont(font)
        self.label_mp3_titles1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mp3_titles1.setObjectName("label_mp3_titles1")
        self.label_mp3_titles1.setMaximumWidth(130)
        self.label_mp3_titles2 = QtWidgets.QLabel(self.groupBox_mp3_setting)
        self.label_mp3_titles2.setGeometry(QtCore.QRect(83, 115, 30, 21))
        self.label_mp3_titles2.setFont(font)
        self.label_mp3_titles2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mp3_titles2.setObjectName("label_mp3_titles2")
        self.label_mp3_titles2.setMaximumWidth(130)
        self.label_mp3_address = QtWidgets.QLabel(self.groupBox_mp3_setting)
        self.label_mp3_address.setGeometry(QtCore.QRect(105, 115, 141, 21))
        self.label_mp3_address.setFont(font)
        self.label_mp3_address.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mp3_address.setObjectName("label_mp3_address")
        self.mp3_layout.addWidget(self.label_mp3_titles1)
        self.mp3_layout.addWidget(self.label_mp3_titles2)
        self.mp3_layout.addWidget(self.label_mp3_address)

        # 음원 추가버튼
        self.btn_new_mp3_line_edit = QtWidgets.QPushButton(self.groupBox_mp3_setting)
        self.btn_new_mp3_line_edit.setGeometry(QtCore.QRect(23, 300, 101, 28))
        font.setPointSize(10)
        self.btn_new_mp3_line_edit.setFont(font)
        self.btn_new_mp3_line_edit.setObjectName("btn_new_mp3_line_edit")
        self.btn_new_mp3_line_edit.setMaximumWidth(100)
        # 음원 삭제버튼
        self.btn_del_mp3_line_edit = QtWidgets.QPushButton(self.groupBox_mp3_setting)
        self.btn_del_mp3_line_edit.setGeometry(QtCore.QRect(145, 300, 101, 28))
        self.btn_del_mp3_line_edit.setFont(font)
        self.btn_del_mp3_line_edit.setObjectName("btn_del_mp3_line_edit")
        self.btn_del_mp3_line_edit.setMaximumWidth(100)
        self.mp3_layout.addWidget(self.btn_new_mp3_line_edit)
        self.mp3_layout.addWidget(self.btn_del_mp3_line_edit)
        self.btn_new_mp3_line_edit.setStyleSheet("color:skyblue")
        self.btn_del_mp3_line_edit.setStyleSheet("color:skyblue")

        # mp3 scrollarea
        self.mp3_scroll_area = QtWidgets.QScrollArea(self.groupBox_mp3_setting)
        self.mp3_scroll_area.setWidgetResizable(True)
        self.widget = QtWidgets.QWidget()
        self.mp3_scroll_area.setWidget(self.widget)
        self.mp3_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mp3_layout = QtWidgets.QVBoxLayout(self.widget)
        self.mp3_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_7.addWidget(self.mp3_groupbox, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.mp3_scroll_area, 1, 0, 1, 1)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.loadMp3Box()

        # 음원 컨트롤박스
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_mp3_3)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setMaximumSize(QtCore.QSize(121, 16777215))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        # 음원 생성 버튼
        self.btn_init_mp3 = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_init_mp3.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_init_mp3.setMaximumSize(QtCore.QSize(93, 16777215))
        self.btn_init_mp3.setFont(self.font)
        self.btn_init_mp3.setObjectName("btn_init_mp3")
        self.verticalLayout_3.addWidget(self.btn_init_mp3)
        # 음원 저장 버튼
        self.btn_save_mp3 = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_save_mp3.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_save_mp3.setMaximumSize(QtCore.QSize(93, 16777215))
        self.btn_save_mp3.setFont(self.font)
        self.btn_save_mp3.setObjectName("btn_save_mp3")
        self.verticalLayout_3.addWidget(self.btn_save_mp3)
        # 음원 삭제 버튼
        self.btn_delete_mp3 = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_delete_mp3.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_delete_mp3.setMaximumSize(QtCore.QSize(93, 16777215))
        self.btn_delete_mp3.setFont(self.font)
        self.btn_delete_mp3.setObjectName("btn_delete_mp3")
        self.verticalLayout_3.addWidget(self.btn_delete_mp3)
        self.tab_widget.addTab(self.tab_mp3_3, "")
        # 음원 탭 레이아웃
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_mp3_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_6.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.widget_mp3_list, 0, 1, 3, 1)
        self.gridLayout_6.addWidget(self.groupBox_mp3_setting, 0, 2, 3, 1)


        self.gridLayout_mid.addWidget(self.tab_widget, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_mid, 1, 0, 1, 1)
        self.horizontalLayout_top = QtWidgets.QHBoxLayout()
        self.horizontalLayout_top.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_top.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_top.setSpacing(10)
        self.horizontalLayout_top.setObjectName("horizontalLayout_top")
        self.groupBox_screen_num = QtWidgets.QGroupBox(widget_QnA)
        self.groupBox_screen_num.setMinimumSize(QtCore.QSize(241, 41))
        self.groupBox_screen_num.setTitle("")
        self.groupBox_screen_num.setObjectName("groupBox_screen_num")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_screen_num)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_screen_num = QtWidgets.QLabel(self.groupBox_screen_num)
        self.label_screen_num.setMinimumSize(QtCore.QSize(50, 0))
        self.label_screen_num.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_screen_num.setFont(self.font_basic2)
        self.label_screen_num.setObjectName("label_screen_num")
        self.horizontalLayout_2.addWidget(self.label_screen_num)
        self.lineEdit_screen_num = QtWidgets.QLineEdit(self.groupBox_screen_num)
        self.lineEdit_screen_num.setMinimumSize(QtCore.QSize(0, 22))
        self.lineEdit_screen_num.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_screen_num.setFont(self.font_basic2)
        self.lineEdit_screen_num.setObjectName("lineEdit_screen_num")
        self.horizontalLayout_2.addWidget(self.lineEdit_screen_num)
        self.label_top_blank = QtWidgets.QLabel(self.groupBox_screen_num)
        self.label_top_blank.setObjectName("label_top_blank")
        self.horizontalLayout_2.addWidget(self.label_top_blank)
        self.horizontalLayout_top.addWidget(self.groupBox_screen_num)

        # txt 저장
        self.groupBox_comboBox = QtWidgets.QGroupBox(widget_QnA)
        self.groupBox_comboBox.setMinimumSize(QtCore.QSize(461, 41))
        self.groupBox_comboBox.setTitle("")
        self.groupBox_comboBox.setObjectName("groupBox_comboBox")
        # 문제
        self.label_comboBox_question = QtWidgets.QLabel(self.groupBox_comboBox)
        self.label_comboBox_question.setGeometry(QtCore.QRect(13, 13, 31, 16))
        self.label_comboBox_question.setFont(self.font_basic2)
        self.label_comboBox_question.setObjectName("label_comboBox_question")
        self.comboBox_question = QtWidgets.QComboBox(self.groupBox_comboBox)
        self.comboBox_question.setGeometry(QtCore.QRect(50, 10, 94, 22))
        self.comboBox_question.setObjectName("comboBox_question")
        # 정답
        self.label_comboBox_answer = QtWidgets.QLabel(self.groupBox_comboBox)
        self.label_comboBox_answer.setGeometry(QtCore.QRect(167, 13, 31, 16))
        self.label_comboBox_answer.setFont(self.font_basic2)
        self.label_comboBox_answer.setObjectName("label_comboBox_answer")
        self.comboBox_answer = QtWidgets.QComboBox(self.groupBox_comboBox)
        self.comboBox_answer.setGeometry(QtCore.QRect(208, 10, 94, 22))
        self.comboBox_answer.setObjectName("comboBox_answer")
        # 음원
        self.label_comboBox_mp3 = QtWidgets.QLabel(self.groupBox_comboBox)
        self.label_comboBox_mp3.setGeometry(QtCore.QRect(323, 12, 31, 16))
        self.label_comboBox_mp3.setFont(self.font_basic2)
        self.label_comboBox_mp3.setObjectName("label_comboBox_mp3")
        self.comboBox_mp3 = QtWidgets.QComboBox(self.groupBox_comboBox)
        self.comboBox_mp3.setGeometry(QtCore.QRect(360, 10, 94, 22))
        self.comboBox_mp3.setObjectName("comboBox_mp3")
        self.horizontalLayout_top.addWidget(self.groupBox_comboBox)
        # 미리보기
        self.btn_preview = QtWidgets.QPushButton(widget_QnA)
        self.btn_preview.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_preview.setMaximumSize(QtCore.QSize(93, 28))
        self.btn_preview.setFont(self.font_basic2)
        self.btn_preview.setObjectName("btn_preview")
        self.horizontalLayout_top.addWidget(self.btn_preview)
        self.horizontalLayout_top.setStretch(0, 1)
        self.horizontalLayout_top.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_top, 0, 0, 1, 1)
        self.gridLayout.setRowStretch(1, 1)

        self.retranslateUi(widget_QnA)
        self.tab_widget.setCurrentIndex(0)
        self.btn_preview.clicked.connect(self.preview)
        self.btn_init_mp3.clicked.connect(self.initMp3)
        self.btn_save_mp3.clicked.connect(self.saveMp3)
        self.btn_delete_mp3.clicked.connect(self.deleteMp3)
        self.btn_new_mp3_line_edit.clicked.connect(self.initMp3LineEdit)
        self.btn_del_mp3_line_edit.clicked.connect(self.delMp3LineEdit)
        self.btn_output.clicked.connect(self.output)
        # self.btn_cancel.clicked.connect(widget_QnA.cancel)
        # self.btn_ok.clicked.connect(widget_QnA.confirm)
        self.btn_init_answer.clicked.connect(self.initAnswer)
        self.btn_save_answer.clicked.connect(self.saveAnswer)
        self.btn_delete_answer.clicked.connect(self.deleteAnswer)
        self.btn_delete_question.clicked.connect(self.deleteQuestion)
        self.btn_save_question.clicked.connect(self.saveQuestion)
        self.btn_init_question.clicked.connect(self.initQuestion)
        self.btn_select_block.clicked.connect(self.selectblocks)
        self.comboBox_select_question.activated.connect(self.selectQuestion)
        self.comboBox_select_screen.activated.connect(self.selectScreen)
        self.tab_widget.currentChanged.connect(self.changedTab)
        self.widget_question_list.itemClicked['QListWidgetItem*'].connect(self.widgetSelectQuestion)
        self.widget_answer_list.itemClicked['QListWidgetItem*'].connect(self.widgetSelectAnswer)
        self.widget_mp3_list.itemClicked['QListWidgetItem*'].connect(self.widgetSelectMp3)
        self.widget_question_list.itemChanged['QListWidgetItem*'].connect(self.modifyQuestionName)
        self.widget_answer_list.itemChanged['QListWidgetItem*'].connect(self.modifyAnswerName)
        self.widget_mp3_list.itemChanged['QListWidgetItem*'].connect(self.modifyMp3Name)
        QtCore.QMetaObject.connectSlotsByName(widget_QnA)

        self.initSettings()

    def retranslateUi(self, widget_QnA):
        _translate = QtCore.QCoreApplication.translate
        widget_QnA.setWindowTitle(_translate("widget_QnA", "Form"))
        self.btn_select_block.setText(_translate("widget_QnA", "블럭선택"))
        self.btn_output.setText(_translate("widget_QnA", "txt 출력"))
        self.btn_cancel.setText(_translate("widget_QnA", "취소"))
        self.btn_ok.setText(_translate("widget_QnA", "확인"))
        self.groupBox.setTitle(_translate("widget_QnA", ""))
        self.btn_init_question.setText(_translate("widget_QnA", "생성"))
        self.btn_save_question.setText(_translate("widget_QnA", "저장"))
        self.btn_delete_question.setText(_translate("widget_QnA", "삭제"))
        self.label_groupbox.setText(_translate("widget_QnA", "ControlBox"))
        self.label_groupbox_2.setText(_translate("widget_QnA", "ControlBox"))
        self.label_mid_blank.setText(_translate("widget_QnA", "       "))
        self.label_select_screen.setText(_translate("widget_QnA", "놀이판선택"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_question_3), _translate("widget_QnA", "문제"))
        self.groupBox_2.setTitle(_translate("widget_QnA", ""))
        self.btn_init_answer.setText(_translate("widget_QnA", "생성"))
        self.btn_save_answer.setText(_translate("widget_QnA", "저장"))
        self.btn_delete_answer.setText(_translate("widget_QnA", "삭제"))
        self.label_mid_balank.setText(_translate("widget_QnA", "       "))
        self.label_select_question.setText(_translate("widget_QnA", "문제선택"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_Answer_3), _translate("widget_QnA", "정답"))
        self.groupBox_mp3_setting.setTitle(_translate("widget_QnA", "설정"))
        self.groupBox_3.setTitle(_translate("widget_QnA", "ControlBox"))
        self.btn_init_mp3.setText(_translate("widget_QnA", "생성"))
        self.btn_save_mp3.setText(_translate("widget_QnA", "저장"))
        self.btn_delete_mp3.setText(_translate("widget_QnA", "삭제"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_mp3_3), _translate("widget_QnA", "음원"))
        self.label_screen_num.setText(_translate("widget_QnA", "문제번호"))
        self.label_top_blank.setText(_translate("widget_QnA", "       "))
        self.label_comboBox_answer.setText(_translate("widget_QnA", "정답"))
        self.label_comboBox_mp3.setText(_translate("widget_QnA", "음원"))
        self.label_comboBox_question.setText(_translate("widget_QnA", "문제"))
        self.btn_preview.setText(_translate("widget_QnA", "미리보기"))
        self.btn_new_mp3_line_edit.setText(_translate("Form", "음원 목록 추가"))
        self.btn_del_mp3_line_edit.setText(_translate("Form", "음원 목록 삭제"))
        self.label_mp3_titles1.setText(_translate("Form", "음원 항목1"))
        self.label_mp3_titles2.setText(_translate("Form", "음원 항목2"))
        self.label_mp3_address.setText(_translate("Form", "음원 주소"))

# 문제
    # 저장된 문제 불러오기
    def questionLoad(self):
        try:
            with open('question_info.p', 'rb') as file:
                # print(pickle.load(file)[0])
                self.question_list = pickle.load(file)[0]
        except:
            traceback.print_exc(file=sys.stdout)
            self.question_list = []
        self.widgetBlockList_reload(self.question_list, self.widget_question_list)

    # widget_question_list item 선택 시 정보 불러온 후 그리기
    def widgetSelectQuestion(self):
        self.checkToSave('question')
        if self.widget_question_list.currentRow() != -1:
            self.target = self.widget_question_list.currentRow()
        else:
            pass
        self.selected_question = self.question_list[self.target]

        self.drawQuestionScene(self.graphicsView_question, self.selected_question)

    # 문제 이름 변경
    def modifyQuestionName(self):
        try:
            self.selected_question.name = self.widget_question_list.item(self.target).text()
        except:
            pass

    # 문제 생성 버튼
    def initQuestion(self):
        try:
            id = self.selected_screen.id
            color = self.selected_screen.color
        except:
            self.error_dialog('놀이판을 선택해주세요!')
        else:
            question = QuestionObject(name='새로운 문제', id=list(reversed(id)), color=list(reversed(color)))
            self.drawQuestionScene(self.graphicsView_question, question)
            self.question_list.append(question)
            count = len(self.question_list) - 1
            self.widgetBlockList(self.question_list, self.widget_question_list, question, count)
            self.selected_question = self.question_list[-1]
            try:
                with open('question_info.p', 'wb') as file:
                    pickle.dump([self.question_list], file)
            except:
                traceback.print_exc(file=sys.stdout)

    # 문제 저장 버튼
    def saveQuestion(self):
        try:    # 문제 선택 안하고 저장할 때 에러 방지
            self.selected_question
        except:
            self.error_dialog('문제를 선택해주세요!')
        else:
            # 전부 삭제한 경우
            if len(self.question_list) == 0:
                pass
            else:
                info = self.punchSceneConverter(question_scene, question_obj, self.graphicsView_question)

                self.selected_question.color = info[1]
                self.selected_question.id = info[0]
                self.selected_question.blocks = info[2]
            with open('question_info.p', 'wb') as file:
                pickle.dump([self.question_list], file)
            self.loadComboBox(list=self.question_list, widget=self.comboBox_question)

    # 문제 삭제 버튼
    def deleteQuestion(self):
        del self.question_list[self.target]
        self.widgetBlockList_reload(self.question_list, self.widget_question_list)
        with open('question_info.p', 'wb') as file:
            pickle.dump([self.question_list], file)


    # 놀이판 가져오기
    def loadScreen(self):
        try:
            with open('screen_info.p', 'rb') as file:
                self.screen_list = pickle.load(file)[0]
        except:
            self.screen_list = []
        try:
            self.loadComboBox(list=self.screen_list, widget=self.comboBox_select_screen)
        except:
            pass

    # 콤보박스에서 놀이판 선택하고 그리기
    def selectScreen(self):
        # print('selected')
        self.selected_screen = self.screen_list[self.comboBox_select_screen.currentIndex()]

        self.drawQuestionScene(self.graphicsView_question, self.selected_screen)


# 정답
    # 저장된 정답 불러오기
    def answerLoad(self):
        try:
            with open('answer_info.p', 'rb') as file:
                self.answer_list = pickle.load(file)[0]
        except:
            traceback.print_exc(file=sys.stdout)
            self.answer_list = []
        self.widgetBlockList_reload(self.answer_list, self.widget_answer_list)

    # widget_answer_list item 선택 시 정보 불러오기
    def widgetSelectAnswer(self):
        self.checkToSave('answer')
        if self.widget_answer_list.currentRow() != -1:
            self.target = self.widget_answer_list.currentRow()
        else:
            pass
        self.selected_answer = self.answer_list[self.target]
        self.drawAnswerScene(self.graphicsView_answer, self.selected_answer)

    # 정답 이름 변경
    def modifyAnswerName(self):
        try:
            self.answer_list[self.target].name = self.widget_answer_list.item(self.target).text()
        except:
            pass

    # 정답 생성 버튼
    def initAnswer(self):
        try:
            id = self.comboBox_selected_question.id
            color = self.comboBox_selected_question.color
            blocks = self.comboBox_selected_question.blocks
        except:
            self.error_dialog('문제를 선택해주세요!')
        else:
            # print(id)
            answer = AnswerObject(name='새로운 정답', id=id, color=color, blocks=blocks)
            self.answer_list.append(answer)
            count = len(self.answer_list) - 1
            self.widgetBlockList(self.answer_list, self.widget_answer_list, answer, count)
            self.selected_answer = self.answer_list[-1]
            self.drawAnswerScene(self.graphicsView_answer, self.selected_answer)
            try:
                with open('answer_info.p', 'wb') as file:
                    pickle.dump([self.answer_list], file)
            except:
                traceback.print_exc(file=sys.stdout)

    # 정답 저장 버튼
    def saveAnswer(self):
        try:    # 정답 선택 안하고 저장할 때 에러 방지
            self.selected_answer
        except:
            self.error_dialog('정답을 선택해주세요!')
        else:
            # 전부 삭제할 경우
            if len(self.answer_list) == 0:
                pass
            else:
                info = self.punchSceneConverter(answer_scene, answer_obj, self.graphicsView_answer)

                self.selected_answer.color = info[1]
                self.selected_answer.id = info[0]
                self.selected_answer.blocks = info[2]

            with open('answer_info.p', 'wb') as file:
                pickle.dump([self.answer_list], file)
            self.loadComboBox(list=self.answer_list, widget=self.comboBox_answer)

    # 정답 삭제 버튼
    def deleteAnswer(self):
        del self.answer_list[self.target]
        self.widgetBlockList_reload(self.answer_list, self.widget_answer_list)
        with open('answer_info.p', 'wb') as file:
            pickle.dump([self.answer_list], file)

    # 콤보박스에서 문제 놀이판 선택한 후 그리기
    def selectQuestion(self):
        self.comboBox_selected_question = self.question_list[self.comboBox_select_question.currentIndex()]
        # print(self.comboBox_selected_question.id)
        self.drawAnswerScene(self.graphicsView_answer, self.comboBox_selected_question)

# 음원
    # 저장된 음원 불러오기
    def mp3Load(self):
        try:
            with open('mp3_info.p', 'rb') as file:
                self.mp3_list = pickle.load(file)[0]
        except:
            self.mp3_list = []
        self.widgetBlockList_reload(self.mp3_list, self.widget_mp3_list)
    # widget_mp3_list 선택 시 정보 불러오기
    def widgetSelectMp3(self):
        self.checkToSave('mp3')
        if self.widget_mp3_list.currentRow() != -1:
            self.target = self.widget_mp3_list.currentRow()
        else:
            pass
        self.selected_mp3 = self.mp3_list[self.target]
        self.loadMp3()

    # 음원 이름 변경
    def modifyMp3Name(self):
        try:
            self.mp3_list[self.target].name = self.widget_mp3_list.item(self.target).text()
        except:
            pass

    # 음원 생성 버튼
    def initMp3(self):
        mp3 = []
        for obj in self.mp3_line_edit_list:
            tmp = []
            for count in obj:
                tmp.append(count.text())
            mp3.append(tmp)
        mp3obj = Mp3Object(name='새로운 음원', mp3=mp3)
        self.mp3_list.append(mp3obj)
        count = len(self.mp3_list) - 1
        self.widgetBlockList(self.mp3_list, self.widget_mp3_list, mp3obj, count)

        try:
            with open('mp3_info.p', 'wb') as file:
                pickle.dump([self.mp3_list], file)
        except:
            traceback.print_exc(file=sys.stdout)
    # 음원 저장 버튼
    def saveMp3(self):
        try:    # 문제 선택 안하고 저장할 때 에러 방지
            self.selected_mp3
        except:
            self.error_dialog('음원을 선택해주세요!')
        else:
            self.mp3_list[self.target].name = self.widget_mp3_list.item(self.target).text()
            mp3 = []
            for obj in self.mp3_line_edit_list:
                tmp = []
                for count in obj:
                    tmp.append(count.text())
                mp3.append(tmp)
            self.mp3_list[self.target].mp3 = mp3
            with open('mp3_info.p', 'wb') as file:
                pickle.dump([self.mp3_list], file)
            self.loadComboBox(list=self.mp3_list, widget=self.comboBox_mp3)
    # 음원 삭제 버튼
    def deleteMp3(self):
        del self.mp3_list[self.target]
        self.widgetBlockList_reload(self.mp3_list, self.widget_mp3_list)

    # 음원항목 추가
    def initMp3LineEdit(self):
        self.loadMp3Box()

    # 음원박스 추가
    def loadMp3Box(self):
        mp3groupbox = QtWidgets.QGroupBox()
        mp3groupbox.setStyleSheet("border:none")
        layout_groupbox = QtWidgets.QHBoxLayout(mp3groupbox)
        layout_groupbox.setContentsMargins(5, 3, 5, 3)

        label_title1 = QtWidgets.QLineEdit(mp3groupbox)
        label_title1.setMinimumHeight(30)
        label_title1.setMaximumWidth(130)
        layout_groupbox.addWidget(label_title1)
        label_title2 = QtWidgets.QLineEdit(mp3groupbox)
        label_title2.setMinimumHeight(30)
        label_title2.setMaximumWidth(130)
        layout_groupbox.addWidget(label_title2)
        label_address = QtWidgets.QLineEdit(mp3groupbox)
        label_address.setMinimumHeight(30)
        layout_groupbox.addWidget(label_address)
        self.mp3_layout.addWidget(mp3groupbox)

        mp3box = [label_title1, label_title2, label_address]
        self.mp3_line_edit_list.append(mp3box)

    # 음원항목 불러오기
    def loadMp3(self):
        # mp3 scrollarea reset
        self.widget = QtWidgets.QWidget()
        self.mp3_scroll_area.setWidget(self.widget)
        self.mp3_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mp3_layout = QtWidgets.QVBoxLayout(self.widget)
        self.mp3_layout.setContentsMargins(0, 0, 0, 0)
        # mp3 line edit에 정보 로드
        self.mp3_line_edit_list = []
        for obj in self.selected_mp3.mp3:
            self.loadMp3Box()
            for count in range(3):
                self.mp3_line_edit_list[-1][count].setText(self._translate("Form", "{}".format(obj[count])))

    # 음원항목 삭제
    def delMp3LineEdit(self):
        # mp3 정보 임시 저장
        mp3 = []
        for obj in self.mp3_line_edit_list:
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
        self.mp3_line_edit_list = []
        for obj in mp3:
            if mp3.index(obj) == len(mp3) - 1:
                break
            else:
                self.loadMp3Box()
                for count in range(3):
                    self.mp3_line_edit_list[-1][count].setText(self._translate("Form", "{}".format(obj[count][1])))

    # 공통
    # 폰트 세팅
    def fontsettings_basic(self, size=10):
        font = QtGui.QFont()
        font.setPointSize(size)
        return font
    def fontsettings_basic2(self):
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        return font
    def fontsettings(self, size=12):
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        font.setPointSize(size)
        return font

    # widgetList 새로고침
    def widgetBlockList_reload(self, list, widget_list):
        widget_list.clear()
        for count in range(len(list)):
            # 문제,정답과 음원의 list 구조가 다름
            try:
                tmp_name = list[count]['name']
                # print('try',tmp_name)
            except:
                tmp_name = list[count].name
                # print('except',tmp_name)
            self.widgetBlockList(list, widget_list, tmp_name, count)

    # widgetList 생성
    def widgetBlockList(self, list, widget_list, obj, count):
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
        widget_list.addItem(item)
        item = widget_list.item(count)
        try:
            item.setText(self._translate("Form", "{}".format(obj.name)))
        except:
            item.setText(self._translate("Form", "{}".format(obj)))

    # 탭 변경
    def changedTab(self):
        if self.tab_widget.currentIndex() == 0:
            self.loadComboBox(list=self.screen_list, widget=self.comboBox_select_screen)
            self.questionLoad()
            self.loadData('question_info.p', self.question_list, self.widget_question_list)
        elif self.tab_widget.currentIndex() == 1:
            self.loadComboBox(list=self.question_list, widget=self.comboBox_select_question)
            self.answerLoad()
            self.loadData('answer_info.p', self.answer_list, self.widget_answer_list)
        elif self.tab_widget.currentIndex() == 2:
            self.mp3Load()
            self.loadData('mp3_info.p', self.mp3_list, self.widget_mp3_list)
    #     print(self.list)
    # 가져올 데이터 선택
    def loadData(self, filename, list, widget_list):
        try:
            with open(filename, 'rb') as file:
                list = pickle.load(file)[0]
        except:
            list = []
        self.widgetBlockList_reload(list, widget_list)
        # print(list)
        # self.list = list
    # 콤보박스 로드
    def loadComboBox(self, list, widget):

        widget.clear()
        for n in list:
            widget.addItem(n.name)

    # 저장없이 다른 놀이판 눌렀을 때 확인
    def checkToSave(self, selector):
        if selector == 'question':
            try:
                item_id = []
                for item in question_scene.items():
                    try:
                        item.value
                        if item not in question_obj:  # question_scene만 선별
                            item_id.append(item)
                    except:
                        pass
                count = 293
                count2 = len(item_id) - 1
                id = []
                color = []
                for xpos in range(14):
                    for ypos in range(21):
                        try:
                            self.graphicsView_question.itemAt(ypos * standard_length + standard_length / 2,
                                                xpos * standard_length + standard_length / 2).color
                        except:
                            id.append(0)
                            color.append(Qt.black)
                        else:
                            id.append(item_id[count2].value)
                            color.append(item_id[count2].color)
                            count2 -= 1
                        count -= 1
                id.reverse()
                color.reverse()
                b_info = []
                for obj in question_obj:
                    b_info.append([obj.size, obj.id, obj.alias, obj.coordinate])
                if self.selected_question.name == self.widget_question_list.item(self.target).text() and self.selected_question.id == id:
                    pass
                else:
                    dlg = checkDialog(obj=self.selected_question, name=self.widget_question_list.item(self.target).text(), selector=selector, id=id, color=color, blocks=b_info)
                    dlg.exec_()
                    self.selected_question = dlg.obj

                with open('question_info.p', 'wb') as file:
                    pickle.dump([self.question_list], file)
            except:
                pass
        elif selector == 'answer':
            try:
                item_id = []
                for item in answer_scene.items():
                    try:
                        item.value
                        if item not in answer_obj:  # answer_scene만 선별
                            item_id.append(item)
                    except:
                        pass
                count = 293
                count2 = len(item_id) - 1
                id = []
                color = []
                for xpos in range(14):
                    for ypos in range(21):
                        try:
                            self.graphicsView_answer.itemAt(ypos * standard_length + standard_length / 2,
                                                              xpos * standard_length + standard_length / 2).color
                        except:
                            id.append(0)
                            color.append(Qt.black)
                        else:
                            id.append(item_id[count2].value)
                            color.append(item_id[count2].color)
                            count2 -= 1
                        count -= 1
                id.reverse()
                color.reverse()
                b_info = []
                for obj in answer_obj:
                    b_info.append([obj.size, obj.id, obj.alias, obj.coordinate])
                if self.selected_answer.name == self.widget_answer_list.item(self.target).text() and self.selected_answer.id == id:
                    pass
                else:
                    dlg = checkDialog(obj=self.selected_answer, name=self.widget_answer_list.item(self.target).text(), selector=selector, id=id, color=color, blocks=b_info)
                    dlg.exec_()
                    self.selected_answer = dlg.obj

                with open('answer_info.p', 'wb') as file:
                    pickle.dump([self.answer_list], file)
            except:
                pass
        elif selector == 'mp3':
            try:
                mp3 = []
                for obj in self.mp3_line_edit_list:
                    tmp = []
                    for count in obj:
                        tmp.append(count.text())
                    mp3.append(tmp)
                if self.mp3_list[self.target].name == self.widget_mp3_list.item(self.target).text() and self.mp3_list[self.target].mp3 == mp3:
                    pass
                else:
                    dlg = checkDialog(obj=self.mp3_list[self.target], name=self.widget_mp3_list.item(self.target).text(), selector=selector, mp3=mp3)
                    dlg.exec_()
                    self.mp3_list[self.target] = dlg.obj

                with open('mp3_info.p', 'wb') as file:
                    pickle.dump([self.mp3_list], file)
            except:
                pass

    # 블럭 선택
    def selectblocks(self):
        global block
        block = LoadBlock()
        block.show()
        scene = QGraphicsScene()
        pos = 0
        # for i in range(3):
        #     item = blockItem()
        #     pos += 40
        #     item.setPos(pos, 0)
        #     scene.addItem(item)

        view = GraphicsView(scene)
        view.setRenderHint(QPainter.Antialiasing)
        view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        view.setBackgroundBrush(QColor(230, 200, 167))

    # 블럭 그리기
    def drawblocks(self):
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView_blocks.setScene(scene)
        for obj in range(len(loaded_blocks)):
            item = blockItem(loaded_blocks[obj].size, loaded_blocks[obj].id, loaded_blocks[obj].alias)
            item.setPos(80 * (obj), 0)
            scene.addItem(item)

    # punch -> 저장될 scene
    def punchSceneConverter(self, scene, obj, graphicsview):
        tmp_id = []
        test = []
        for item in scene.items():
            try:
                item.value
                if item not in obj:  # question_scene만 선별
                    tmp_id.append(item)
                    test.append(item.value)
            except:
                pass
        # print(test)
        count = 293
        count2 = len(tmp_id) - 1
        id = []
        color = []
        for xpos in range(14):
            for ypos in range(21):
                # print(self.graphicsView_question.itemAt(ypos*standard_length + standard_length/2, xpos*standard_length + standard_length/2).color)
                try:
                    graphicsview.itemAt(ypos * standard_length + standard_length / 2,
                                                      xpos * standard_length + standard_length / 2).color
                except:
                    id.append(0)
                    color.append(Qt.black)
                else:
                    id.append(tmp_id[count2].value)
                    color.append(tmp_id[count2].color)
                    count2 -= 1
                count -= 1
        id.reverse()
        color.reverse()

        # count = 293
        # output = ''
        # for ypos in range(14):
        #     output += '\n'
        #     for xpos in range(21):
        #         # if id[count] == 0:
        #         #     output += str(0) + ', '
        #         # else:
        #         output += str(id[count]) + ', '
        #         count -= 1
        # output = output.lstrip('\n')
        # print(output)

        b_info = []
        for obj in obj:
            b_info.append([obj.size, obj.id, obj.alias, obj.coordinate])
            # print(obj.coordinate)
        return [id, color, b_info]
    # 스크린 블럭객체 그리기
    def drawBackgroundScene(self, scene):
        # print(viewer.sizeHint())
        # print(viewer.width())
        # width = viewer.sizeHint().width()/21
        # height = viewer.sizeHint().height()/14
        # print(list)
        # scene.setBackgroundBrush(Qt.red)

        # print('list_id = ', list.id)
        if self.tab_widget.currentIndex() == 0:
            screen_item = screenBackgroundQuestion()
        elif self.tab_widget.currentIndex() == 1:
            screen_item = screenBackgroundAnswer()
        screen_item.setPos(0,0)
        scene.addItem(screen_item)

        # viewer.fitInView(screen_item, Qt.IgnoreAspectRatio)
        # print('tmp__id = ', tmp)
        # print(scene.width(), scene.height())
        return scene
    def drawQuestionPunchScene(self, list, scene):
        global question_obj, question_scene
        try:
            # 놀이판 불러왔을 때
            if list == self.selected_screen:
                c_info=[]
                count = 0
                for xpos in range(14):
                    for ypos in range(21):
                        # print(list.id[count])
                        try:
                            if list.id[count] == 1:
                                screen_item = screenItemQuestion()
                                screen_item.setPos(ypos * standard_length, xpos * standard_length)
                                screen_item.color = Qt.white
                                screen_item.value = 0
                                scene.addItem(screen_item)
                                c_info.append(Qt.white)
                            else:
                                c_info.append(Qt.black)
                        except:
                            pass
                        count += 1
                list.color = c_info
                # print(len(list.color))
            else:
                count = 293
                for xpos in range(14):
                    for ypos in range(21):
                        try:
                            if list.color[count] == Qt.white:
                                screen_item = screenItemQuestion()
                                screen_item.setPos(ypos * standard_length, xpos * standard_length)
                                screen_item.color = Qt.white
                                screen_item.value = 0
                                scene.addItem(screen_item)
                                # t.append(Qt.white)
                            elif list.color[count] == Qt.green:
                                # print(list.id[count])
                                screen_item = screenItemQuestion()
                                screen_item.setPos(ypos * standard_length, xpos * standard_length)
                                screen_item.color = Qt.green
                                screen_item.value = list.id[count]
                                scene.addItem(screen_item)
                                # t.append(Qt.green)
                        except:
                            # t.append(Qt.black)
                            pass
                        count -= 1
                # self.selected_question.color = t
                question_obj = []
                for block in list.blocks:
                    b_info = block
                    # scene에 블럭 그리기 - id의 구조가 일차원 리스트 바꼈음
                    block_obj = questionBlockItem(b_info[0], b_info[1], b_info[2], b_info[3])
                    block_obj.setPos(b_info[3][0][1], b_info[3][0][0])
                    scene.addItem(block_obj)
                    question_obj.append(block_obj)
                # print(len(scene.items()))
        # 문제 불러왔을 때
        except:
            count = 293
        # print('start', len(list.id))
        # print('list_id = ', list.id)
        #     t=[]
            for xpos in range(14):
                for ypos in range(21):
                    # print(list.id[count])
                    try:
                        if list.color[count] == Qt.white:
                            screen_item = screenItemQuestion()
                            screen_item.setPos(ypos * standard_length, xpos * standard_length)
                            screen_item.color = Qt.white
                            screen_item.value = 0
                            scene.addItem(screen_item)
                            # t.append(Qt.white)
                        elif list.color[count] == Qt.green:
                            # print(list.id[count])
                            screen_item = screenItemQuestion()
                            screen_item.setPos(ypos * standard_length, xpos * standard_length)
                            screen_item.color = Qt.green
                            screen_item.value = list.id[count]
                            scene.addItem(screen_item)
                            # t.append(Qt.green)
                    except:
                        # t.append(Qt.black)
                        pass
                    count -= 1
            # self.selected_question.color = t
            question_obj = []
            for block in list.blocks:
                b_info = block
                # scene에 블럭 그리기 - id의 구조가 일차원 리스트 바꼈음
                block_obj = questionBlockItem(b_info[0], b_info[1], b_info[2], b_info[3])
                block_obj.setPos(b_info[3][0][1], b_info[3][0][0])
                scene.addItem(block_obj)
                question_obj.append(block_obj)
            # print(len(scene.items()))
        question_scene = scene

    def drawQuestionScene(self, viewer, list):
        # print(list.id)
        # 새로만든 문제 에러 방지
        # if len(list.id) == 0:
        #     self.selectScreen()
        # else:
        scene = QtWidgets.QGraphicsScene()
        viewer.setScene(scene)
        self.drawBackgroundScene(scene)
        self.drawQuestionPunchScene(list, scene)

    def drawAnswerPunchScene(self, list, scene):
        global answer_obj, answer_scene
        # print(list.id)
        # 문제 불러왔을 때
        if list == self.question_list[self.comboBox_select_question.currentIndex()]:
            count = 293
            for xpos in range(14):
                for ypos in range(21):
                    try:
                        if list.color[count] == Qt.white:
                            screen_item = screenItemAnswer()
                            screen_item.setPos(ypos * standard_length, xpos * standard_length)
                            screen_item.color = Qt.white
                            screen_item.value = 0
                            scene.addItem(screen_item)
                        elif list.color[count] == Qt.green:
                            screen_item = screenItemAnswer()
                            screen_item.setPos(ypos * standard_length, xpos * standard_length)
                            screen_item.color = Qt.green
                            screen_item.value = list.id[count]
                            scene.addItem(screen_item)
                    except:
                        pass
                    count -= 1

            for block in list.blocks:
                b_info = block
                block_obj = answerBlockItem(b_info[0], b_info[1], b_info[2], b_info[3])
                block_obj.setPos(b_info[3][0][1], b_info[3][0][0])
                scene.addItem(block_obj)
                answer_obj.append(block_obj)
        # 정답 불러왔을 때
        else:
            count = 293
            # print('start', len(list.id))
            # print('list_id = ', list.id)
            for xpos in range(14):
                for ypos in range(21):
                    # print(list.id[count])
                    try:
                        if list.color[count] == Qt.white:
                            screen_item = screenItemAnswer()
                            screen_item.setPos(ypos * standard_length, xpos * standard_length)
                            screen_item.color = Qt.white
                            screen_item.value = list.id[count]
                            scene.addItem(screen_item)
                        elif list.color[count] == Qt.green:
                            screen_item = screenItemAnswer()
                            screen_item.setPos(ypos * standard_length, xpos * standard_length)
                            screen_item.color = Qt.green
                            screen_item.value = list.id[count]
                            scene.addItem(screen_item)
                    except:
                        pass
                    count -= 1
            # print('draw',len(list.blocks),list.id)
            answer_obj = []
            for block in list.blocks:
                b_info = block
                # scene에 블럭 그리기 - id의 구조가 일차원 리스트 바꼈음
                block_obj = answerBlockItem(b_info[0], b_info[1], b_info[2], b_info[3])
                block_obj.setPos(b_info[3][0][1], b_info[3][0][0])
                scene.addItem(block_obj)
                answer_obj.append(block_obj)
            # print('tmp__id = ', tmp)
        # print('answer scene 개수',len(scene.items()),scene.items())
        answer_scene = scene

    def drawAnswerScene(self, viewer, list):
        # 새로만든 문제 에러 방지
        if len(list.id) == 0:
            self.selectScreen()
        else:
            scene = QtWidgets.QGraphicsScene()
            viewer.setScene(scene)
            self.drawBackgroundScene(scene)
            self.drawAnswerPunchScene(list, scene)

# txt 저장할 파일 선택
    def txt_items(self):
        num = self.lineEdit_screen_num.text()
        output_question, output_answer, output_mp3 = None, None, None
        for q in self.question_list:
            if q.name == self.comboBox_question.currentText():
                output_question = q
        for a in self.answer_list:
            if a.name == self.comboBox_answer.currentText():
                output_answer = a
        for m in self.mp3_list:
            if m.name == self.comboBox_mp3.currentText():
                output_mp3 = m
        output = [num, output_question, output_answer, output_mp3]
        return output

    def preview(self):
        self.txt_items()

    # txt 출력
    def output(self):
        output = self.txt_items()

        question = '{}_question.txt'.format(output[0])
        question_contents = self.output_id(output[1].id)
        with open(question, 'wt') as f:
            f.write(question_contents)

        answer = '{}_answer.txt'.format(output[0])
        answer_contents = self.output_id(output[2].id)
        with open(answer, 'wt') as f:
            f.write(answer_contents)

        mp3 = '{}.txt'.format(output[0])
        mp3_contents = self.output_mp3(output[3].mp3)
        with open(mp3, 'wt') as f:
            f.write(mp3_contents)

    # 음원 출력 형식
    def output_mp3(self, mp3_tmp):
        mp3_count = []
        for count in mp3_tmp:
            if len(count[-1]) > 2:
                mp3_count.append(count[-1].count(',') + 1)
            else:
                # 언어 변경
                if count[0] == 'en':
                    mp3_count.append('')
                else:
                    mp3_count.append(0)

        mp3_contents = ''
        mp3_save_list = []
        mp3_info = '{},{},{},{},\n'
        mp3_save_list2 = []
        for count in range(len(mp3_tmp)):
            mp3_save_list2.append(mp3_info)
        mp3_save_list += mp3_save_list2

        count = 0
        for i in mp3_save_list:
            mp3_contents += i.format(mp3_tmp[count][0], mp3_tmp[count][1],
                                     mp3_count[count], mp3_tmp[count][2])
            count += 1
        return mp3_contents

    # id 출력 형식
    def output_id(self, id):
        count = 293
        output = ''
        for ypos in range(14):
            output += '\n'
            for xpos in range(21):
                output += str(id[count]) + ', '
                count -= 1
        output = output.lstrip('\n')
        return output

    def error_dialog(self, str):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(str)
        error_dialog.exec_()

    def initSettings(self):
        self.loadScreen()
        self.questionLoad()
        self.answerLoad()
        self.mp3Load()
        self.loadComboBox(list=self.question_list, widget=self.comboBox_question)
        self.loadComboBox(list=self.answer_list, widget=self.comboBox_answer)
        self.loadComboBox(list=self.mp3_list, widget=self.comboBox_mp3)
        # global question_scene
        # question_scene = self.drawQuestionScene(self.graphicsView_question, self.selected_screen)

class checkDialog(QtWidgets.QDialog):
    def __init__(self, obj, name, selector, id=None, color=None, blocks=None, minmax=None, mp3=None):
        super().__init__()
        self.setupUI()
        self.obj = obj
        self.name = name
        self.selector = selector
        self.id = id
        self.color = color
        self.blocks = blocks
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
        if self.selector == 'question':
            self.obj.name = self.name
            self.obj.id = self.id
            self.obj.color = self.color
            self.obj.blocks = self.blocks
        elif self.selector == 'answer':
            self.obj.name = self.name
            self.obj.id = self.id
            self.obj.color = self.color
            self.obj.blocks = self.blocks
        elif self.selector == 'mp3':
            self.obj.name = self.name
            self.obj.mp3 = self.mp3
        self.close()

    def pushCancelButtonClicked(self):
        self.close()

    def fontsettings(self, size=12):
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        font.setPointSize(size)
        return font

# 블럭 가져오기
class LoadBlock(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.label_message = QtWidgets.QLabel('원하는 블럭을 드래그하여 오른쪽으로 옮겨주세요.')
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        font.setPointSize(10)
        self.label_message.setFont(font)
        self.label_message.setAlignment(QtCore.Qt.AlignCenter)
        self.label_message.setObjectName("label_message")

        self.loadBlockListWidget = QtWidgets.QListWidget()
        self.importBlockListWidget = QtWidgets.QListWidget()
        self.importBlockListWidget.setViewMode(QtWidgets.QListWidget.IconMode)
        self.loadBlockListWidget.setDragEnabled(True)
        self.importBlockListWidget.setAcceptDrops(True)

        self.label_text = QtWidgets.QLabel('->')
        self.label_text.setFont(font)
        self.label_text.setObjectName("label_text")

        self.setGeometry(300, 350, 500, 300)
        self.groupbox = QtWidgets.QGroupBox()
        self.layout_lower = QtWidgets.QHBoxLayout(self.groupbox)
        self.layout_lower.addWidget(self.loadBlockListWidget)
        self.layout_lower.addWidget(self.label_text)
        self.layout_lower.addWidget(self.importBlockListWidget)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_message)
        self.layout.addWidget(self.groupbox)

        try:
            with open('block_info.p', 'rb') as file:
                self.block_list = pickle.load(file)[0]
        except:
            self.block_list = []

        for count in range(len(self.block_list)):
            item = QtWidgets.QListWidgetItem(self.block_list[count].name)
            # item = QtWidgets.QListWidgetItem(self.draw_icon(count), self.block_list[count].name)
            self.loadBlockListWidget.insertItem(count+1, item)

        self.setWindowTitle('블럭 선택')
        self.setLayout(self.layout)

        self.loadBlockListWidget.itemDoubleClicked['QListWidgetItem*'].connect(self.add_block)
        self.importBlockListWidget.itemDoubleClicked['QListWidgetItem*'].connect(self.delete)
        self.importBlockListWidget.itemChanged['QListWidgetItem*'].connect(self.save_list)

        # self.draw_icon()
    def draw_icon(self, count):
        # px = QPixmap(50,50)
        # painter = QPainter(self)
        # rect = QtCore.QRect(20,20,30,30)
        # painter.drawText(rect,0,'ssd')
        # px = QPixmap(50,50)
        # px.rect(rect)
        # "{}".format(self.block_list[count].alias)
        # b = blockIcon()
        # print(px, b)
        # pixmap = QPixmap(34, 34)
        # pixmap.fill(Qt.white)
        #
        # painter = QtGui.QPainter(pixmap)

        icon = QtGui.QIcon.pixmap(32,32)
        return icon

    def add_block(self):
        print(self.importBlockListWidget.count(), self.loadBlockListWidget.currentItem())
        # self.importBlockListWidget.addItem(self.loadBlockListWidget.currentItem())
        self.importBlockListWidget.insertItem(self.importBlockListWidget.count() + 1, self.loadBlockListWidget.currentItem())
        print(self.importBlockListWidget.count())

    def save_list(self):
        global loaded_blocks
        tmp_block_list = []
        for count in range(self.importBlockListWidget.count()):
            tmp_block_list.append(self.importBlockListWidget.item(count).text())
        loaded_blocks = []
        for obj in self.block_list:
            if obj.name in tmp_block_list:
                loaded_blocks.append(obj)
        self.show_blocks()

    def delete(self):
        self.importBlockListWidget.takeItem(self.importBlockListWidget.currentRow())
        del loaded_blocks[self.importBlockListWidget.currentRow()]
        # print(loaded_blocks)
        self.show_blocks()

    def show_blocks(self):
        pass

    def closeEvent(self, event):
        try:
            ui.drawblocks()
        except:
            pass
        event.accept()
################################## screen ################################################
class screenPartQuestion(QGraphicsObject):
    def __init__(self, parent=None):
        super(screenPartQuestion, self).__init__(parent)

        self.value = None
        self.color = QColor(Qt.black)
        self.dragOver = False

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.setAccepted(True)
            self.dragOver = True
        else:
            event.setAccepted(False)

    def dragLeaveEvent(self, event):
        self.dragOver = False

    def dropEvent(self, event):
        global question_obj, question_scene
        self.dragOver = False
        if event.mimeData().hasText():
            tmp = event.mimeData().text().split('_')
            # print(tmp)
            b_info = []
            for i in range(2):
                x = u'{}'.format(tmp[i])
                x = ast.literal_eval(x)
                b_info.append(x)
            # print(b_info)

            # 적용될 scene 정보
            tmp_list = []
            tmp_id = []
            for x in range(b_info[0][0]):
                for y in range(b_info[0][1]):
                    tmp_list.append([self.y()+(standard_length*x), self.x()+(standard_length*y)])
                    try:
                        tmp_id.append(b_info[1][x][y])
                    except:
                        tmp_id = b_info[1]
            tmp_list = sorted(tmp_list, key=lambda x: (x[0], x[1]))
            b_info[1] = tmp_id
            b_info.append(tmp[2])
            b_info.append(tmp_list)

            if selected_question_obj in question_obj:
                # 기존 scene마다 id값과 색 초기화
                for scene in question_scene.items():
                    try:     # question block item만 선별
                        if [scene.y(), scene.x()] in selected_question_obj.coordinate:
                            scene.value = 0
                            scene.color = Qt.white
                            scene.update()
                    except:
                        pass
                # 대상 scene마다 id값과 색 부여
                for scene in question_scene.items():
                    try:  # question block item만 선별
                        if [scene.y(), scene.x()] in b_info[3]:
                            index = b_info[3].index([scene.y(), scene.x()])
                            if b_info[1][index] == '':
                                pass
                            else:
                                scene.value = b_info[1][index]
                            scene.color = Qt.green
                            scene.update()
                    except:
                        pass
                tmp_id = []
                for item in question_scene.items():
                    try:
                        tmp_id.append(item.value)
                    except:
                        pass
                # print(len(tmp_id), tmp_id)
                # 블럭 객체모양 위치 이동
                selected_question_obj.setPos(tmp_list[0][1], tmp_list[0][0])
                selected_question_obj.coordinate = b_info[3]
                selected_question_obj.color = Qt.green
            else:
                # scene에 블럭 그리기 - id의 구조가 일차원 리스트 바꼈음
                block_obj = questionBlockItem(b_info[0], b_info[1], b_info[2], b_info[3])
                block_obj.setPos(tmp_list[0][1], tmp_list[0][0])
                question_scene.addItem(block_obj)
                question_obj.append(block_obj)
                # 대상 scene마다 id값과 색 부여
                for scene in question_scene.items():
                    try:  # question block item만 선별
                        if [scene.y(), scene.x()] in b_info[3]:
                            index = b_info[3].index([scene.y(), scene.x()])
                            if b_info[1][index] == '':
                                pass
                            else:
                                scene.value = b_info[1][index]
                            scene.color = Qt.green
                            scene.update()
                    except:
                        pass
                tmp_id = []
                for item in question_scene.items():
                    try:
                        tmp_id.append(item.value)
                    except:
                        pass
                # print(len(tmp_id), tmp_id)
        # t = []
        # for scene in question_scene.items():
        #     try:
        #         t.append(scene.value)
        #     except:
        #         pass
        # count = 0
        # output = ''
        # for ypos in range(12):
        #     output += '\n'
        #     for xpos in range(12):
        #         try:
        #             # 임시로 초록색 -> 검은색
        #             if t[count] == 2:
        #                 output += str(1) + ', '
        #             else:
        #                 output += str(t[count]) + ', '
        #             count += 1
        #         except:
        #             output += str(0) + ', '
        # output = output.lstrip('\n')
        # print(output)


class screenBackgroundQuestion(QGraphicsObject):
    def __init__(self, parent=None):
        super(screenBackgroundQuestion, self).__init__(parent)
        self.dragOver = False

    def boundingRect(self):
        return QRectF( 0, 0, standard_length*21, standard_length*14)

    def paint(self, painter, option, widget=None):
        painter.setPen(QtCore.Qt.blue)
        painter.setBrush(QColor(Qt.black))
        painter.drawRect(self.boundingRect())
        for i in range(20):
            painter.drawLine( standard_length + standard_length*i, 0, standard_length + standard_length*i, standard_length*14)
        for i in range(13):
            painter.drawLine( 0, standard_length + standard_length*i, standard_length*21, standard_length + standard_length*i)

class screenItemQuestion(screenPartQuestion):
    def __init__(self, parent=None):
        super(screenItemQuestion, self).__init__(parent)

    def boundingRect(self):
        return QRectF(0, 0, standard_length, standard_length)

    def paint(self, painter, option, widget=None):
        painter.setPen(QtCore.Qt.blue)
        painter.setBrush(self.color.lighter(130) if self.dragOver else self.color)
        painter.drawRect(self.boundingRect())

class screenPartAnswer(QGraphicsObject):
    def __init__(self, parent=None):
        super(screenPartAnswer, self).__init__(parent)

        self.value = None
        self.color = QColor(Qt.black)
        self.dragOver = False

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.setAccepted(True)
            self.dragOver = True
        else:
            event.setAccepted(False)

    def dragLeaveEvent(self, event):
        self.dragOver = False

    def dropEvent(self, event):
        global answer_obj, answer_scene
        self.dragOver = False
        if event.mimeData().hasText():
            # 텍스트 정보 리스트로 변환
            tmp = event.mimeData().text().split('_')
            b_info = []
            for i in range(2):
                x = u'{}'.format(tmp[i])
                x = ast.literal_eval(x)
                b_info.append(x)

            # 적용될 scene 정보
            tmp_list = []
            tmp_id = []
            for x in range(b_info[0][0]):
                for y in range(b_info[0][1]):
                    tmp_list.append([self.y() + (standard_length * x), self.x() + (standard_length * y)])
                    try:
                        tmp_id.append(b_info[1][x][y])
                    except:
                        tmp_id = b_info[1]
            tmp_list = sorted(tmp_list, key=lambda x: (x[0], x[1]))
            b_info[1] = tmp_id
            b_info.append(tmp[2])
            b_info.append(tmp_list)

            if selected_answer_obj in answer_obj:
                # 기존 scene마다 id값과 색 초기화
                for scene in answer_scene.items():
                    try:     # answer block item만 선별
                        if [scene.y(), scene.x()] in selected_answer_obj.coordinate:
                            scene.value = 0
                            scene.color = Qt.white
                            scene.update()
                    except:
                        pass
                # 대상 scene마다 id값과 색 부여
                for scene in answer_scene.items():
                    try:  # answer block item만 선별
                        if [scene.y(), scene.x()] in b_info[3]:
                            index = b_info[3].index([scene.y(), scene.x()])
                            if b_info[1][index] == '':
                                pass
                            else:
                                scene.value = b_info[1][index]
                            scene.color = Qt.green
                            scene.update()
                    except:
                        pass
                tmp_id = []
                for item in answer_scene.items():
                    try:
                        tmp_id.append(item.value)
                    except:
                        pass
                # print(len(tmp_id), tmp_id)
                # 블럭 객체모양 위치 이동
                selected_answer_obj.setPos(tmp_list[0][1], tmp_list[0][0])
                selected_answer_obj.coordinate = b_info[3]
                selected_answer_obj.color = Qt.green
            else:
                # scene에 블럭 그리기 - id의 구조가 일차원 리스트 바꼈음
                block_obj = answerBlockItem(b_info[0], b_info[1], b_info[2], b_info[3])
                block_obj.setPos(tmp_list[0][1], tmp_list[0][0])
                answer_scene.addItem(block_obj)
                answer_obj.append(block_obj)
                # 대상 scene마다 id값과 색 부여
                for scene in answer_scene.items():
                    try:  # answer block item만 선별
                        if [scene.y(), scene.x()] in b_info[3]:
                            index = b_info[3].index([scene.y(), scene.x()])
                            if b_info[1][index] == '':
                                pass
                            else:
                                scene.value = b_info[1][index]
                            scene.color = Qt.green
                            scene.update()
                    except:
                        pass
                tmp_id = []
                for item in answer_scene.items():
                    try:
                        tmp_id.append(item.value)
                    except:
                        pass
                # print(len(tmp_id), tmp_id)

            # 대상 scene마다 값과 색 부여
            # for scene in answer_scene.items():
            #     if [scene.x(),scene.y()] in b_info[2]:
            #         scene.value = b_info[1][b_info[2].index([scene.x(), scene.y()])]
            #         # print(scene.color)
            #         scene.color = Qt.red
            #         scene.update()
                    # print(scene.value, scene.color)
        # self.update()

class screenBackgroundAnswer(QGraphicsObject):
    def __init__(self, parent=None):
        super(screenBackgroundAnswer, self).__init__(parent)
        self.dragOver = False

    def boundingRect(self):
        return QRectF( 0, 0, standard_length*21, standard_length*14)

    def paint(self, painter, option, widget=None):
        painter.setPen(QtCore.Qt.blue)
        painter.setBrush(QColor(Qt.black))
        painter.drawRect(self.boundingRect())
        for i in range(20):
            painter.drawLine( standard_length + standard_length*i, 0, standard_length + standard_length*i, standard_length*14)
        for i in range(13):
            painter.drawLine( 0, standard_length + standard_length*i, standard_length*21, standard_length + standard_length*i)


class screenItemAnswer(screenPartAnswer):
    def __init__(self, parent=None):
        super(screenItemAnswer, self).__init__(parent)

    def boundingRect(self):
        return QRectF(0, 0, standard_length, standard_length)

    def paint(self, painter, option, widget=None):
        painter.setPen(QtCore.Qt.blue)
        painter.setBrush(self.color.lighter(130) if self.dragOver else self.color)
        painter.drawRect(self.boundingRect())

################################## /screen ################################################
class blockIcon(QGraphicsItem):
    def __init__(self, parent=None):
        super(blockIcon, self).__init__(parent)
        self.pixmap = QPixmap()

    def boundingRect(self):
        return QRectF(-15, -50, 30, 30)

    def paint(self, painter, option, widget=None):
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        rect = QtCore.QRectF(0,0,50,50)
        painter.setFont(QtGui.QFont("Serif", 20))
        painter.drawText(rect, Qt.AlignCenter, "{}".format('alias'))
        painter.setPen(Qt.black)
        return rect

class blockItem(QGraphicsItem):
    n = 0

    def __init__(self, size, id, alias):
        super(blockItem, self).__init__()
        self.size = size
        self.id = id
        self.alias = alias
        self.coordinate = None

        self.block_length = 20
        self.color = Qt.white

        self.setToolTip(
            "놀이판으로 드래그하세요!"
        )
        self.setCursor(Qt.OpenHandCursor)
        self.setAcceptedMouseButtons(Qt.LeftButton)

    def boundingRect(self):
        return QRectF(0, 0, self.block_length * self.size[1], self.block_length * self.size[0])

    def paint(self, painter, option, widget, length=None):
        painter.setPen(QPen(Qt.black, 2))
        if length == None:
            rect = QtCore.QRectF(0, 0, self.block_length * self.size[1], self.block_length * self.size[0])
        else:
            rect = QtCore.QRectF(0, 0, length * self.size[1], length * self.size[0])
            self.color = Qt.green
        painter.fillRect(rect, self.color)
        painter.setFont(QtGui.QFont("1훈정글북 R", self.size[1] * 2 + self.size[0] * 2))
        painter.drawText(rect, Qt.AlignCenter, "{}".format(self.alias))
        painter.drawRect(rect)

    def mousePressEvent(self, event):
        self.setCursor(Qt.ClosedHandCursor)
        global selected_question_obj
        selected_question_obj = self
        global selected_answer_obj
        selected_answer_obj = self

    def mouseMoveEvent(self, event):
        # if QLineF(QPointF(event.screenPos()),
        #           QPointF(event.buttonDownScreenPos(Qt.LeftButton))).length() < QApplication.startDragDistance():
        #     print(QPointF(event.screenPos()), QPointF(event.buttonDownScreenPos(Qt.LeftButton)))
        #     print(QApplication.startDragDistance())
        #     return

        drag = QDrag(event.widget())
        mime = QMimeData()
        drag.setMimeData(mime)

        mime.setText('{}_{}_{}_{}'.format(self.size, self.id, self.alias, self.coordinate))
        # print(mime.text())
        pixmap = QPixmap(self.size[1] * standard_length, self.size[0] * standard_length)
        pixmap.fill(Qt.white)

        painter = QPainter(pixmap)
        painter.setPen(Qt.black)
        painter.translate(0, 0)
        painter.setRenderHint(QPainter.Antialiasing)
        self.paint(painter, None, None, length=standard_length)
        painter.end()

        pixmap.setMask(pixmap.createHeuristicMask())

        drag.setPixmap(pixmap)
        drag.setHotSpot(QPoint(15, 20))

        drag.exec_()
        self.setCursor(Qt.OpenHandCursor)

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.OpenHandCursor)


class questionBlockItem(QGraphicsItem):
    n = 0

    def __init__(self, size, id, alias, coordinate=None):
        super(questionBlockItem, self).__init__()
        self.size = size
        self.origin_size = self.size
        self.id = id
        self.origin_id = self.id
        self.alias = alias
        self.rotated_coordinate = []
        self.coordinate = coordinate
        self.direction = 0

        self.block_length = standard_length
        self.color = Qt.green

        self.setToolTip(
            "드래그하거나 더블클릭하여 회전시키세요."
        )
        self.setCursor(Qt.OpenHandCursor)
        self.setAcceptedMouseButtons(Qt.LeftButton)

    def boundingRect(self):
        # block_items = []
        # count = 0
        # for y in range(self.size[0]):
        #     for x in range(self.size[1]):
        #         if self.id[count] != '':
        #             block_items.append(QtCore.QRectF(x*self.block_length, y*self.block_length, self.block_length, self.block_length))
        #         count += 1
        return QRectF(0, 0, self.block_length * self.size[1], self.block_length * self.size[0])

    def paint(self, painter, option, widget):
        painter.setPen(QPen(Qt.black, 2))
        rect = QtCore.QRectF(0, 0, self.block_length * self.size[1], self.block_length * self.size[0])

        painter.fillRect(rect, self.color)
        painter.drawRect(rect)

        painter.setPen(QPen(Qt.blue, 1))
        count = 0

        for y in range(self.size[0]):
            for x in range(self.size[1]):
                if self.id[count] == '':
                    blank = QtCore.QRectF(x*self.block_length, y*self.block_length, self.block_length, self.block_length)
                    painter.fillRect(blank, Qt.white)
                    painter.drawRect(blank)
                count += 1

        if self.direction == 0:
            painter.rotate(0)
        elif self.direction == 1:
            painter.translate(self.block_length * self.size[1], 0)
            painter.rotate(90)
        elif self.direction == 2:
            painter.translate(self.block_length * self.size[1], self.block_length * self.size[0])
            painter.rotate(180)
        elif self.direction == 3:
            painter.translate(0, self.block_length * self.size[0])
            painter.rotate(270)
        painter.setFont(QtGui.QFont("1훈정글북 R", self.size[1] * 2 + self.size[0] * 2))
        painter.setPen(QPen(Qt.blue, 1))
        painter.drawText(rect, Qt.AlignCenter, "{}".format(self.alias))

    def mousePressEvent(self, event):
        self.setCursor(Qt.ClosedHandCursor)
        global selected_question_obj
        selected_question_obj = self

    def mouseMoveEvent(self, event):
        # if QLineF(QPointF(event.screenPos()),
        #           QPointF(event.buttonDownScreenPos(Qt.LeftButton))).length() < QApplication.startDragDistance():
        #     print(QPointF(event.screenPos()), QPointF(event.buttonDownScreenPos(Qt.LeftButton)))
        #     print(QApplication.startDragDistance())
        #     return

        drag = QDrag(event.widget())
        mime = QMimeData()
        drag.setMimeData(mime)

        mime.setText('{}_{}_{}_{}'.format(self.size, self.id, self.alias, self.coordinate))
        # print(mime.text())
        pixmap = QPixmap(self.size[1]*self.block_length, self.block_length * self.size[0])
        pixmap.fill(Qt.white)

        painter = QPainter(pixmap)
        painter.setPen(Qt.black)
        painter.translate(0, 0)
        painter.setRenderHint(QPainter.Antialiasing)
        self.paint(painter, None, None)
        painter.end()

        pixmap.setMask(pixmap.createHeuristicMask())

        drag.setPixmap(pixmap)
        drag.setHotSpot(QPoint(15, 20))

        drag.exec_()
        self.setCursor(Qt.OpenHandCursor)

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.OpenHandCursor)

    # 방향은 0, 1, 2, 3, 0 순서
    def mouseDoubleClickEvent(self, event):
        self.direction += 1
        if self.direction > 3:
            self.direction = 0
        tmp_list1 = []
        tmp_list2 = []
        # print('origin_id = ',self.origin_id)
        if self.direction == 0:
            print('0도')
            self.size = self.origin_size
            self.id = self.origin_id
            self.id.reverse()

            self.resetScene()

        elif self.direction == 1:
            print('90도')
            tmp = {}
            id = []
            count = 0
            for i in range(self.origin_size[1]):
                tmp[i] = []
            for y in range(self.origin_size[1]):
                for x in range(self.origin_size[0]):
                    tmp[count % self.origin_size[1]].append(self.origin_id[count])
                    count += 1
            for i in range(self.origin_size[1]):
                tmp[i].reverse()
                id += tmp[i]
            self.id = id
            self.size = [self.origin_size[1], self.origin_size[0]]

            self.resetScene()

        elif self.direction == 2:
            print('180도')
            self.size = self.origin_size
            self.id = self.origin_id
            self.id.reverse()

            self.resetScene()

        elif self.direction == 3:
            print('270도')
            tmp = {}
            id = []
            count = 0
            for i in range(self.origin_size[1]):
                tmp[i] = []
            for y in range(self.origin_size[1]):
                for x in range(self.origin_size[0]):
                    tmp[count % self.origin_size[1]].append(self.origin_id[count])
                    count += 1
            for i in reversed(range(self.origin_size[1])):
                id += tmp[i]
            id.reverse()
            self.id = id
            self.size = [self.origin_size[1], self.origin_size[0]]

            self.resetScene()
        # print(self.id)


    def resetScene(self):
        # 적용될 scene 정보
        self.rotated_coordinate = []
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.rotated_coordinate.append([self.y() + (standard_length * x), self.x() + (standard_length * y)])
        self.rotated_coordinate = sorted(self.rotated_coordinate, key=lambda x: (x[0], x[1]))

        if selected_question_obj in question_obj:
            # print(selected_question_obj, selected_question_obj.pos())
            # 기존 scene마다 id값과 색 초기화
            for scene in question_scene.items():
                if [scene.y(), scene.x()] in selected_question_obj.coordinate:
                    scene.value = 0
                    scene.color = Qt.white
                    scene.update()
        # print(self.id)
        # 대상 scene마다 id값과 색 부여
        for scene in question_scene.items():
            if [scene.y(), scene.x()] in self.rotated_coordinate:
                index = self.rotated_coordinate.index([scene.y(), scene.x()])
                scene.value = self.id[index]
                scene.color = Qt.green
                scene.update()
        selected_question_obj.coordinate = self.rotated_coordinate


class answerBlockItem(QGraphicsItem):
    n = 0

    def __init__(self, size, id, alias, coordinate=None):
        super(answerBlockItem, self).__init__()
        self.size = size
        self.origin_size = self.size
        self.id = id
        self.origin_id = self.id
        self.alias = alias
        self.rotated_coordinate = []
        self.coordinate = coordinate
        self.direction = 0

        self.block_length = standard_length
        self.color = Qt.green

        self.setToolTip(
            "드래그하거나 더블클릭하여 회전시키세요."
        )
        self.setCursor(Qt.OpenHandCursor)
        self.setAcceptedMouseButtons(Qt.LeftButton)

    def boundingRect(self):
        return QRectF(0, 0, self.block_length * self.size[1], self.block_length * self.size[0])

    def paint(self, painter, option, widget):
        painter.setPen(QPen(Qt.black, 2))
        rect = QtCore.QRectF(0, 0, self.block_length * self.size[1], self.block_length * self.size[0])

        painter.fillRect(rect, self.color)
        painter.drawRect(rect)
        painter.setPen(QPen(Qt.blue, 1))
        count = 0
        for y in range(self.size[0]):
            for x in range(self.size[1]):
                if self.id[count] == '':
                    blank = QtCore.QRectF(x*self.block_length, y*self.block_length, self.block_length, self.block_length)
                    painter.fillRect(blank, Qt.white)
                    painter.drawRect(blank)
                count += 1

        if self.direction == 0:
            painter.rotate(0)
        elif self.direction == 1:
            painter.translate(self.block_length * self.size[1], 0)
            painter.rotate(90)
        elif self.direction == 2:
            painter.translate(self.block_length * self.size[1], self.block_length * self.size[0])
            painter.rotate(180)
        elif self.direction == 3:
            painter.translate(0, self.block_length * self.size[0])
            painter.rotate(270)
        painter.setFont(QtGui.QFont("1훈정글북 R", self.size[1] * 2 + self.size[0] * 2))
        painter.drawText(rect, Qt.AlignCenter, "{}".format(self.alias))
    def mousePressEvent(self, event):
        self.setCursor(Qt.ClosedHandCursor)
        global selected_answer_obj
        selected_answer_obj = self

    def mouseMoveEvent(self, event):
        # if QLineF(QPointF(event.screenPos()),
        #           QPointF(event.buttonDownScreenPos(Qt.LeftButton))).length() < QApplication.startDragDistance():
        #     print(QPointF(event.screenPos()), QPointF(event.buttonDownScreenPos(Qt.LeftButton)))
        #     print(QApplication.startDragDistance())
        #     return

        drag = QDrag(event.widget())
        mime = QMimeData()
        drag.setMimeData(mime)

        mime.setText('{}_{}_{}_{}'.format(self.size, self.id, self.alias, self.coordinate))
        # print(mime.text())
        pixmap = QPixmap(self.size[1]*self.block_length, self.block_length * self.size[0])
        pixmap.fill(Qt.white)

        painter = QPainter(pixmap)
        painter.setPen(Qt.black)
        painter.translate(0, 0)
        painter.setRenderHint(QPainter.Antialiasing)
        self.paint(painter, None, None)
        painter.end()

        pixmap.setMask(pixmap.createHeuristicMask())

        drag.setPixmap(pixmap)
        drag.setHotSpot(QPoint(15, 20))

        drag.exec_()
        self.setCursor(Qt.OpenHandCursor)

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.OpenHandCursor)

    # 방향은 0, 1, 2, 3, 0 순서
    def mouseDoubleClickEvent(self, event):
        self.direction += 1
        if self.direction > 3:
            self.direction = 0
        tmp_list1 = []
        tmp_list2 = []
        # print('origin_id = ',self.origin_id)
        if self.direction == 0:
            self.size = self.origin_size
            self.id = self.origin_id
            self.id.reverse()

            self.resetScene()

        elif self.direction == 1:
            print('90도')
            tmp = {}
            id = []
            count = 0
            for i in range(self.origin_size[1]):
                tmp[i] = []
            for y in range(self.origin_size[1]):
                for x in range(self.origin_size[0]):
                    tmp[count % self.origin_size[1]].append(self.origin_id[count])
                    count += 1
            for i in range(self.origin_size[1]):
                tmp[i].reverse()
                id += tmp[i]
            self.id = id
            self.size = [self.origin_size[1], self.origin_size[0]]

            self.resetScene()

        elif self.direction == 2:
            self.size = self.origin_size
            self.id = self.origin_id
            self.id.reverse()

            self.resetScene()

        elif self.direction == 3:
            print('270도')
            tmp = {}
            id = []
            count = 0
            for i in range(self.origin_size[1]):
                tmp[i] = []
            for y in range(self.origin_size[1]):
                for x in range(self.origin_size[0]):
                    tmp[count % self.origin_size[1]].append(self.origin_id[count])
                    count += 1
            for i in reversed(range(self.origin_size[1])):
                id += tmp[i]
            id.reverse()
            self.id = id
            self.size = [self.origin_size[1], self.origin_size[0]]

            self.resetScene()


    def resetScene(self):
        # 적용될 scene 정보
        self.rotated_coordinate = []
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.rotated_coordinate.append([self.y() + (standard_length * x), self.x() + (standard_length * y)])
        self.rotated_coordinate = sorted(self.rotated_coordinate, key=lambda x: (x[0], x[1]))

        if selected_answer_obj in answer_obj:
            # print(selected_answer_obj, selected_answer_obj.pos())
            # 기존 scene마다 id값과 색 초기화
            for scene in answer_scene.items():
                if [scene.y(), scene.x()] in selected_answer_obj.coordinate:
                    scene.value = 1
                    scene.color = Qt.white
                    scene.update()
        # print(self.id)
        # 대상 scene마다 id값과 색 부여
        for scene in answer_scene.items():
            if [scene.y(), scene.x()] in self.rotated_coordinate:
                index = self.rotated_coordinate.index([scene.y(), scene.x()])
                scene.value = self.id[index]
                scene.color = Qt.green
                scene.update()
        selected_answer_obj.coordinate = self.rotated_coordinate



class GraphicsView(QGraphicsView):

    def resizeEvent(self, e):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget_QnA = QtWidgets.QWidget()
    ui = Ui_widget_QnA()
    ui.setupUi(widget_QnA)
    widget_QnA.show()

    # block = LoadBlock()

    sys.exit(app.exec_())
