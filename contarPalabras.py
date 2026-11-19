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
        cantidadPalabras = len(TextoSeparado)
        print("palabras",cantidadPalabras)
        self.tvPalabras.setText(f"palabras:{cantidadPalabras}")
        #contar caraccteres
        totalCaracteres=0
        for palabra in TextoSeparado:
            totalCaracteres += len(palabra)
        totalCaracteres
        self.tvCaracteres.setText(f"caracteres: {totalCaracteres}")
        #TODO configurar el cambio de texto dinamico
        #Condicionar la alerta
        if cantidadPalabras >= 20:
            self.tvPalabras.setStyleSheet("color: #ff756b")
        else:
            self.tvPalabras.setStyleSheet("color: #000000")
        if totalCaracteres >= 120:
            self.tvCaracteres.setStyleSheet("color: #ff756b")
        else:
            self.tvCaracteres.setStyleSheet("color: #000000")
                                    


app=QtWidgets.QApplication(sys.argv)
ventana = contadorPalabras()
ventana.show()
sys.exit(app.exec())