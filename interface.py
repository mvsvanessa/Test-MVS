from PyQt5 import uic, QtWidgets
import sys

app = QtWidgets.QApplication([])

tela_inicial = uic.loadUi('janelas/tela_inicial.ui')
tela_imc = uic.loadUi('janelas/tela_peso_altura.ui')
tela_calorias = uic.loadUi('janelas/tela_calorias.ui')
tela_finalizar_imc = uic.loadUi('janelas/tela_finalizar.ui')
tela_finalizar_calorias = uic.loadUi('janelas/tela_finalizar_calorias.ui')

def carregar_tela_imc():
    tela_inicial.close()
    tela_imc.show()

def carregar_tela_calorias():
    tela_inicial.close()
    tela_calorias.show()

def calculo_imc():
    tela_finalizar_imc.show()
    altura = tela_finalizar_imc.Line_altura.text()
    peso = tela_finalizar_imc.Line_peso.text()

    altura = float(altura)
    peso = float(peso)

    

def calculo_calorias():
    peso = tela_calorias.Line_peso.text()
    altura = tela_calorias.Line_altura.text()
    idade = tela_calorias.Line_idade.text()
    sexo = tela_calorias.comboBox_sexo.currentText()
    frequencia = tela_calorias.comboBox_freq.currentText()
    
    peso = float(peso)
    altura = float(altura)
    idade = float(idade)
    
    if frequencia == 'Sedentário':
        freq = 1.2

    elif frequencia == 'Leve, 1 à 3 dias por semana':
        freq = 1.375

    elif frequencia == 'Moderado, 3 à 5 dias por semana':
        freq = 1.550

    elif frequencia == 'Intenso, 6 à 7 dias por semana':
        freq = 1.725

    if sexo == 'Feminino':
        tbmF= 655.1 + (9.5 * peso) + (1.8 * altura) - (4.7 * idade)
        caloriasDesejadas = tbmF * freq
        caloriasDesejadas = round(caloriasDesejadas, 2)

    if sexo == 'Masculino':
        tbmM = 66.5 + (13.8 * peso) + (5 * altura) - (6.8 * idade)
        caloriasDesejadas = tbmM * freq
        caloriasDesejadas = round(caloriasDesejadas, 2)

    finalizar_calorias(caloriasDesejadas)

def finalizar_calorias(caloriasDesejadas):
    caloriasDesejadas = str(caloriasDesejadas)
    tela_finalizar_calorias.show()
    tela_finalizar_calorias.Line_caloria_ideal.setText(caloriasDesejadas)

def sair():
    tela_calorias.close()
    tela_imc.close()
    tela_inicial.show()

#BOTÕES DA TELA INICIAL
tela_inicial.Button_imc.clicked.connect(carregar_tela_imc)
tela_inicial.Button_calorias.clicked.connect(carregar_tela_calorias)

#BOTÕES DA TELA IMC
tela_imc.Button_sair.clicked.connect(sair)
tela_imc.Button_calcular.clicked.connect(calculo_imc)

#BOTÕES DA TELA DE CALORIAS
tela_calorias.Button_sair.clicked.connect(sair)
tela_calorias.Button_calcular.clicked.connect(calculo_calorias)
tela_calorias.comboBox_freq.addItem('Sedentário')
tela_calorias.comboBox_freq.addItem('Leve, 1 à 3 dias por semana')
tela_calorias.comboBox_freq.addItem('Moderado, 3 à 5 dias por semana')
tela_calorias.comboBox_freq.addItem('Intenso, 6 à 7 dias por semana')

tela_calorias.comboBox_sexo.addItem('Feminino')
tela_calorias.comboBox_sexo.addItem('Masculino')

tela_inicial.show()
app.exec()