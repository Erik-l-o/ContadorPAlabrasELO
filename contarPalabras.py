#importar
import sys
from PyQt5 import QtWidgets,uic

 
class contadorPalabras(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("contadorPalabras.ui",self)
        #conectar botones
        self.btnContar.clicked.connect(self.contarPalabras)
    def contarPalabras(self):
        #recuperar texto
        texto= self.edtCaracteres.text()
        #separar palabras
        TextoSeparado =texto.split() #separa las letras
        print(TextoSeparado)
        #contar las palabras
        #contar caraccteres
        print("se ha ejecutado")
    
app=QtWidgets.QApplication(sys.argv)
ventana = contadorPalabras()
ventana.show()
sys.exit(app.exec())