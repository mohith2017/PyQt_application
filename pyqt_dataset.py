from PyQt5 import QtWidgets, QtCore, QtGui
import pandas as pd

class PyQtApp(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.setWindowTitle('PyQt Application')
        self.setWindowIcon(QtGui.QIcon('D:/DESKTOP/COGNIZANT/1st task/rose.png'))
        self.setMinimumWidth(resolution.width() / 3)
        self.setMinimumHeight(resolution.height() / 1.5)

        self.label = QtWidgets.QLabel("This is a PyQt5 window!")

        #self.input = QtWidgets.QTextEdit(self)
        #self.input.setPlaceholderText("Type of data:")
        #self.output =QtWidgets.QTextEdit(self)

        self.fields , ok1 =QtWidgets.QInputDialog.getInt(self,'number of fields:','enter number of fields:')
        #if ok1:
        #    self.output.setText(str(self.fields))

        self.records , ok =QtWidgets.QInputDialog.getInt(self,'number of records:','enter no of records:')
        #if ok:
        #    self.input.setText(str(self.records))

        self.delimiter , ok =QtWidgets.QInputDialog.getText(self,'delimiter:','Delimiter:')
        #if ok:
        #    self.input.setText(self.delimiter)

        self.grid1 = QtWidgets.QGridLayout()

        input=[]
        x=10
        y=2
        for i in range(self.fields):
            items = ('blah','blah1')
            input='input'+str(i)
            input = QtWidgets.QComboBox(self)
            input.addItem("Field type"+str(i+1))
            input.addItem("ID")
            input.addItem("Serial No.")
            input.addItem("Name")
            #input.setPlaceholderText('Field'+str(i+1))
            self.grid1.addWidget(input, x, y)

            data='data_type'+str(i)
            data = QtWidgets.QComboBox(self)
            data.addItem("Data type"+str(i+1))
            data.addItem("Text")
            data.addItem("Number")
            #data.setPlaceholderText('Data Type'+str(i+1))
            self.grid1.addWidget(data, x, y+1)

            unique='unique'+str(i)
            unique = QtWidgets.QComboBox(self)
            unique.addItem("Unique")
            unique.addItem("Random")
            self.grid1.addWidget(unique, x, y+2)

            column_name='column_name'+str(i)
            column_name = QtWidgets.QTextEdit(self)
            column_name.setPlaceholderText('Column Name'+str(i+1))
            self.grid1.addWidget(column_name, x, y+3)

            x+=1

        self.btn = QtWidgets.QPushButton('Generate!',self)
        self.btn.clicked.connect(self.generate)

        self.grid1.addWidget(self.btn, x, y+2)

        #self.grid1.addWidget(self.label, 0, 0, 14, 13)
        #self.grid1.addWidget(self.text, 50, 50, 10, 13)
        #self.grid1.addWidget(self.output, 1000, 1000, 10, 13)

        self.setLayout(self.grid1)

    def generate(self):
        data = {'blah':['xd','lol']}
        df=pd.DataFrame(data)
        df.to_csv('D:/DESKTOP/COGNIZANT/1st task/output_csv.csv')

        self.close()



if __name__=='__main__':
    import sys
    app= QtWidgets.QApplication(sys.argv)
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()
    myapp = PyQtApp()
    myapp.show()
    sys.exit(app.exec_())
