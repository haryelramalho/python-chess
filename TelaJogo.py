from Pecas import *
from gi.repository import Gtk, Gdk
import gi
gi.require_version('Gtk', '3.0')

pecaClicada = [None, None] #lista que pega a posicao de duas casas
qtdClicada = -1

def casaClicada(widget):
	global pecaClicada
	global qtdClicada
	global janela
	if widget.getSelecionar():
		widget.retirarSelecao()
		qtdClicada -= 1
	elif qtdClicada < 1:
		if qtdClicada != -1 or widget.getPeca() != None:
			widget.selecionar()
			qtdClicada += 1
			pecaClicada[qtdClicada] = widget
	if qtdClicada == 1:
		if pecaClicada[0].getPeca().verificaMovimento(pecaClicada[1], janela.tabuleiro.casas):
			if pecaClicada[1].getPeca() != None:
				if pecaClicada[1].getPeca().getCor() == 'Brancas':
					janela.capBrancos.addPeca(pecaClicada[1].getPeca())
				elif pecaClicada[1].getPeca().getCor() == 'Pretas':
					janela.capPretos.addPeca(pecaClicada[1].getPeca())
			janela.tabuleiro.casas[pecaClicada[1].getPosicao()[0]][pecaClicada[1].getPosicao()[1]].setPeca(pecaClicada[0].getPeca())
			janela.tabuleiro.casas[pecaClicada[0].getPosicao()[0]][pecaClicada[0].getPosicao()[1]].setPeca(None)
			
		janela.tabuleiro.casas[pecaClicada[1].getPosicao()[0]][pecaClicada[1].getPosicao()[1]].retirarSelecao()
		janela.tabuleiro.casas[pecaClicada[0].getPosicao()[0]][pecaClicada[0].getPosicao()[1]].retirarSelecao()
		
		qtdClicada = -1
			
   
   
class CasaTabuleiro(Gtk.Button):
	def __init__(self, posicao, cor, peca):
		Gtk.Button.__init__(self)
		self.__imagem = Gtk.Image()
		self.set_image(self.__imagem)
		self.set_relief(Gtk.ReliefStyle.NONE)
		self.__posicao = posicao
		self.__selecionar = False
		self.__cor = 'Claro' if cor else 'Escuro'
		self.__peca = peca
		if self.__peca != None:
			self.__endImg = self.__peca.getEnderecoImg() + self.__cor + '.svg'
		else:
			self.__endImg = 'Img/Tabuleiro/casa' + self.__cor + '.svg'
		self.__imagem.set_from_file(self.__endImg)
		self.connect('clicked', casaClicada)
		
		
	def __atualizaImg(self):
		if self.__peca != None:
			self.__endImg = self.__peca.getEnderecoImg() + self.__cor + '.svg'
		else:
			self.__endImg = 'Img/Tabuleiro/casa' + self.__cor + '.svg'
		self.__imagem.set_from_file(self.__endImg)
		
		
	def selecionar(self):
		if self.__peca == None:
			self.__endImg = 'Img/Tabuleiro/casa' + self.__cor + 'C.svg'
		elif not self.__selecionar:
			self.__endImg = self.__peca.getEnderecoImg() + self.__cor + 'C.svg'
		self.__imagem.set_from_file(self.__endImg)
		self.__selecionar = True
		
	def retirarSelecao(self):
		self.__atualizaImg()
		self.__selecionar = False
		
	def setPeca(self, peca):
		self.__peca = peca
		if self.__peca != None:
			self.__peca.setPosicao(self.__posicao)
		self.__atualizaImg()
		
	def getPeca(self):
		return self.__peca

	def getSelecionar(self):
		return self.__selecionar

	def getPosicao(self):
		return self.__posicao

class Tabuleiro(Gtk.Grid):
	def __init__(self):
		Gtk.Grid.__init__(self)
		self.set_name('Tabuleiro')
		self.set_halign(Gtk.Align.CENTER)
		self.casas = [[], [], [], [], [], [], [], []]
		
		
		cor = True
		i = 0
		while i < 8:
			j = 0
			while j < 8:
				self.casas[i].append(CasaTabuleiro([i, j], cor, None))
				cor = not cor
				j += 1
			cor = not cor
			i += 1

		# Peças Pretas
		# Linha do Rei
		self.casas[0][0].setPeca(Torre([0, 0], False))
		self.casas[0][1].setPeca(Cavalo([0, 1], False))
		self.casas[0][2].setPeca(Bispo([0, 2], False))
		self.casas[0][3].setPeca(Dama([0, 3], False))
		self.casas[0][4].setPeca(Rei([0, 4], False))
		self.casas[0][5].setPeca(Bispo([0, 5], False))
		self.casas[0][6].setPeca(Cavalo([0, 6], False))
		self.casas[0][7].setPeca(Torre([0, 7], False))
		
		# Linha dos peões
		i = 0
		while i < 8:
			self.casas[1][i].setPeca(Peao([1, i], False))
			i += 1

		
		# Peças Brancas
		# Linha dos peões
		i = 0
		while i < 8:
			self.casas[6][i].setPeca(Peao([6, i], True))
			i += 1
		
		# Linha do Rei
		self.casas[7][0].setPeca(Torre([7, 0], True))
		self.casas[7][1].setPeca(Cavalo([7, 1], True))
		self.casas[7][2].setPeca(Bispo([7, 2], True))
		self.casas[7][3].setPeca(Dama([7, 3], True))
		self.casas[7][4].setPeca(Rei([7, 4], True))
		self.casas[7][5].setPeca(Bispo([7, 5], True))
		self.casas[7][6].setPeca(Cavalo([7, 6], True))
		self.casas[7][7].setPeca(Torre([7, 7], True))

		
		i = 0
		while i < 8:
			self.attach(self.casas[i][0], 0, i, 1,1)
			j = 0
			while j < 7:
				self.attach_next_to(self.casas[i][j+1], self.casas[i][j], Gtk.PositionType.RIGHT, 1,1)
				j += 1
			i += 1
			

class BarraCapturados(Gtk.Box):
	def __init__(self, alinhamento):
		Gtk.Box.__init__(self, orientation=Gtk.Orientation.HORIZONTAL)
		if alinhamento:
			self.set_halign(Gtk.Align.START)
			self.set_name('CapturadosBrancos')
		else:
			self.set_halign(Gtk.Align.END)
			self.set_name('CapturadosPretos')
		self.__valor = 0
		self.__pecas = [[], []]
		self.__imgPecas = [[], []]
		
		self.__box = [Gtk.Box(orientation=Gtk.Orientation.VERTICAL), Gtk.Box(orientation=Gtk.Orientation.VERTICAL)]
		
		i = 0
		while i < 2:
			j = 0
			while j < 8:
				self.__imgPecas[i].append(Gtk.Image())
				self.__imgPecas[i][j].set_from_file('Img/Tabuleiro/vazio.svg')
				self.__box[i].pack_start(self.__imgPecas[i][j], True, True, 0)
				j += 1
			i += 1
		
		if alinhamento:
			self.pack_start(self.__box[0], True, True, 0)
			self.pack_start(self.__box[1], True, True, 0)
		else:
			self.pack_start(self.__box[1], True, True, 0)
			self.pack_start(self.__box[0], True, True, 0)
		
	def addPeca(self, peca):
		if type(peca) == Peao:
			self.__pecas[1].append(peca)
			aux = len(self.__pecas[1])
			self.__imgPecas[1][aux - 1].set_from_file(peca.getEnderecoImg() + '.svg')
		else:
			self.__pecas[0].append(peca)
			aux = len(self.__pecas[0])
			self.__imgPecas[0][aux - 1].set_from_file(peca.getEnderecoImg() + '.svg')
		self.__valor += peca.getValor()
				

class TelaJogo(Gtk.Window):
	def __init__(self, wid, hei):
		Gtk.Window.__init__(self, title='PyChess')
		self.set_name('geral')
		self.set_position(Gtk.WindowPosition.CENTER)
		self.set_icon_from_file('Img/Icone.svg')
		self.set_size_request(wid, hei)
		self.set_resizable(False)
		self.set_border_width(2)
		
		self.__box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		
		self.capBrancos = BarraCapturados(True)
		self.capPretos = BarraCapturados(False)
		self.tabuleiro = Tabuleiro()
		
		self.__subBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		self.__subBox.pack_start(self.tabuleiro, True, True, 10)
		
		# Exemplos de como inserir nas barras de Capturados
		#self.capPretos.addPeca(Dama([2, 5], False))
		# self.__capPretos.addPeca(Peao([4, 6], False))
		# self.__capBrancos.addPeca(Peao([4, 6], True))

		self.__box.pack_start(self.capBrancos, True, True, 0)
		self.__box.pack_start(self.__subBox, True, True, 100)
		self.__box.pack_start(self.capPretos, True, True, 0)

		self.add(self.__box)
	
	def setValorP(self, valor):
		self.__ValorP = valor
		self.__LValorP.set_text(self.__ValorP)
	
	def getValorP(self):
		return self.__ValorP
	
	def setValorB(self, valor):
		self.__ValorB = valor
		self.__LValorB.set_text(self.__ValorB)
		
	def getValorB(self):
		return self.__ValorB

tela = Gdk.Screen.get_default()
estilo = Gtk.CssProvider()
estilo.load_from_path('estilo.css')	
context = Gtk.StyleContext()
context.add_provider_for_screen(tela, estilo, Gtk.STYLE_PROVIDER_PRIORITY_USER)
		
janela = TelaJogo(750, 600)
janela.connect('destroy', Gtk.main_quit)
janela.show_all()
Gtk.main()
