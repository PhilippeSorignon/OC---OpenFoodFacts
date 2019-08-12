from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from functools import partial
import Api
import Database


class Display(object):
    """Class with display functions"""

    def setupUi(self, MainWindow):
        """Set up the UI widgets"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 631, 441))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(30, 70, 571, 81))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(20, 230, 581, 151))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.listWidget = QtWidgets.QListWidget(self.page_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 631, 421))
        self.listWidget.setObjectName("listWidget")
        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.listWidget_3 = QtWidgets.QListWidget(self.page_4)
        self.listWidget_3.setGeometry(QtCore.QRect(0, 0, 631, 421))
        self.listWidget_3.setObjectName("listWidget_3")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.listWidget_4 = QtWidgets.QListWidget(self.page_5)
        self.listWidget_4.setGeometry(QtCore.QRect(0, 0, 631, 421))
        self.listWidget_4.setObjectName("listWidget_4")
        self.stackedWidget.addWidget(self.page_5)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 611, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 131, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(150, 50, 89, 28))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 111, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.listWidget_2 = QtWidgets.QListWidget(self.page_3)
        self.listWidget_2.setGeometry(QtCore.QRect(150, 91, 471, 181))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(10, 300, 89, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(70, 300, 550, 28))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_3)
        self.label_9.setGeometry(QtCore.QRect(10, 370, 121, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.checkBox = QtWidgets.QCheckBox(self.page_3)
        self.checkBox.setGeometry(QtCore.QRect(130, 370, 117, 32))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 35))
        self.menubar.setObjectName("menubar")
        self.menuRemplacer = QtWidgets.QMenu(self.menubar)
        self.menuRemplacer.setObjectName("menuRemplacer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSnack = QtWidgets.QAction(MainWindow)
        self.actionSnack.setObjectName("actionSnack")
        self.actionRetrouver = QtWidgets.QAction(MainWindow)
        self.actionRetrouver.setObjectName("actionRetrouver")
        self.actionDrinks = QtWidgets.QAction(MainWindow)
        self.actionDrinks.setObjectName("actionDrinks")
        self.actionAp_ritif = QtWidgets.QAction(MainWindow)
        self.actionAp_ritif.setObjectName("actionAp_ritif")
        self.actionBiscuits = QtWidgets.QAction(MainWindow)
        self.actionBiscuits.setObjectName("actionBiscuits")
        self.actionBoissons = QtWidgets.QAction(MainWindow)
        self.actionBoissons.setObjectName("actionBoissons")
        self.actionConfiseries = QtWidgets.QAction(MainWindow)
        self.actionConfiseries.setObjectName("actionConfiseries")
        self.actionProduits_tartiner = QtWidgets.QAction(MainWindow)
        self.actionProduits_tartiner.setObjectName("actionProduits_tartiner")
        self.actionEnregistr_s = QtWidgets.QAction(MainWindow)
        self.actionEnregistr_s.setObjectName("actionEnregistr_s")
        self.menuRemplacer.addAction(self.actionAp_ritif)
        self.menuRemplacer.addAction(self.actionBiscuits)
        self.menuRemplacer.addAction(self.actionBoissons)
        self.menuRemplacer.addAction(self.actionConfiseries)
        self.menuRemplacer.addAction(self.actionProduits_tartiner)
        self.menuRemplacer.addSeparator()
        self.menuRemplacer.addAction(self.actionEnregistr_s)
        self.menubar.addAction(self.menuRemplacer.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """Translate"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Open Food Facts"))
        self.label.setText(_translate("MainWindow", "Pour afficher la liste des aliments cliquez sur \"Menu\" puis la \n"
" catégorie souhaité"))
        self.label_2.setText(_translate("MainWindow", "Pour afficher les aliments enregistrés cliquez sur \"Menu\" puis \n"
" sur \"Enregistrés\""))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Nutri-score :"))
        self.label_5.setText(_translate("MainWindow", "NS"))
        self.label_6.setText(_translate("MainWindow", "Magasins :"))
        self.label_7.setText(_translate("MainWindow", "URL : "))
        self.label_8.setText(_translate("MainWindow", "url"))
        self.label_9.setText(_translate("MainWindow", "Enregistré :"))
        self.menuRemplacer.setTitle(_translate("MainWindow", "Menu"))
        self.actionSnack.setText(_translate("MainWindow", "Snack"))
        self.actionRetrouver.setText(_translate("MainWindow", "Retrouver"))
        self.actionDrinks.setText(_translate("MainWindow", "Drinks"))
        self.actionAp_ritif.setText(_translate("MainWindow", "Apéritif"))
        self.actionBiscuits.setText(_translate("MainWindow", "Biscuits"))
        self.actionBoissons.setText(_translate("MainWindow", "Boissons"))
        self.actionConfiseries.setText(_translate("MainWindow", "Confiseries"))
        self.actionProduits_tartiner.setText(_translate("MainWindow", "Produits à tartiner"))
        self.actionEnregistr_s.setText(_translate("MainWindow", "Enregistrés"))

        self.actionAp_ritif.triggered.connect(partial(self.show_category_list, "aperitif"))
        self.actionBiscuits.triggered.connect(partial(self.show_category_list, "biscuits"))
        self.actionBoissons.triggered.connect(partial(self.show_category_list, "boissons"))
        self.actionConfiseries.triggered.connect(partial(self.show_category_list, "confiseries"))
        self.actionProduits_tartiner.triggered.connect(partial(self.show_category_list,\
         "produits-a-tartiner-sucres"))
        self.actionEnregistr_s.triggered.connect(self.show_saved_products)
        self.label_8.linkActivated.connect(self.link)

    def init(self):
        """Initialisation"""
        categories = ['aperitif', 'biscuits', 'boissons', 'confiseries',\
         'produits-a-tartiner-sucres']
        self.db = Database.Database()
        if not self.db.does_database_exists():
            self.db.create_database()
            self.db.connect()
            self.db.create_tables()

            api_data = []
            for current_category in range(len(categories)):
                api_data.append(Api.Api(categories[current_category]))
                api_data[current_category].get_data()
                for current_product in range(len(api_data[current_category].name)):
                    self.db.save_product(api_data[current_category].name[current_product],\
                     api_data[current_category].category,\
                     api_data[current_category].nutri_score[current_product],\
                      api_data[current_category].url[current_product],\
                       api_data[current_category].stores[current_product])
            self.db.disconnect()
        self.db.connect()


    def show_saved_products(self):
        """Show the saved products in a list"""
        self.listWidget_4.clear()
        product_dict = self.db.get_saved_products()

        for current_product in range(len(product_dict)):
            self.listWidget_4.insertItem(current_product, product_dict[current_product]['name'])
        self.stackedWidget.setCurrentIndex(3)

        self.listWidget_4.itemClicked.connect(partial(self.show_product_data, 'saved'))


    def show_category_list(self, cat):
        """Show a list of all the products in the selected category"""
        self.listWidget.clear()
        product_dict = self.db.get_products(cat)

        for current_product in range(len(product_dict)):
            self.listWidget.insertItem(current_product, product_dict[current_product]['name'])
        self.stackedWidget.setCurrentIndex(1)

        self.listWidget.clicked.connect(partial(self.show_replaced_list, cat))


    def show_replaced_list(self, cat):
        """Show a list with better products"""
        self.listWidget.clicked.disconnect()
        self.listWidget_3.clear()
        product_dict = self.db.replace_product(cat)

        for current_product in range(len(product_dict)):
            self.listWidget_3.insertItem(current_product, product_dict[current_product]['name'])
        self.stackedWidget.setCurrentIndex(2)
        self.listWidget_3.itemClicked.connect(partial(self.show_product_data, 'replaced'))


    def show_product_data(self, show):
        """Show all the products infos"""
        if show == 'replaced':
            self.listWidget_3.itemClicked.disconnect()
            name = self.listWidget_3.item(self.listWidget_3.currentRow()).text()
        else:
            self.listWidget_4.itemClicked.disconnect()
            name = self.listWidget_4.item(self.listWidget_4.currentRow()).text()

        product = self.db.get_product_data(name)

        self.label_3.setText(str(product['name']))
        self.label_5.setText(str(product['nutri_score']))
        self.label_8.setText('<a href="'+str(product['url']+'">OpenFoodFacts</a>'))

        self.listWidget_2.clear()

        product_dict = self.db.get_stores(str(product['id']))

        for current_product in range(len(product_dict)):
            self.listWidget_2.insertItem(current_product,\
             self.db.get_store_name(str(product_dict[current_product]['store'])))

        if product['saved'] == 1:
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)

        self.checkBox.stateChanged.connect(partial(self.save_product, str(product['id'])))

        self.stackedWidget.setCurrentIndex(4)


    def save_product(self, id_product):
        """Save or unsave the product"""
        self.checkBox.stateChanged.disconnect()
        if self.checkBox.isChecked():
            self.db.product_saved(id_product, True)
        else:
            self.db.product_saved(id_product, False)


    def link(self, linkStr):
        """Used to display web links"""
        QDesktopServices.openUrl(QUrl(linkStr))


if __name__ == "__main__":
    """Main"""
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Display()
    ui.init()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
