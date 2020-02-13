class Peca:
	def __init__(self, cor, posicao, valor, enderecoImg):
		self.__cor = cor
		self.__posicao = posicao
		self.__valor = valor
		self.__enderecoImg = enderecoImg

	def getCor(self):
		return self.__cor

	def getPosicao(self):
		return self.__posicao

	def getValor(self):
		return self.__valor

	def getEnderecoImg(self):
		return self.__enderecoImg

	def setPosicao(self, posicao):
		self.__posicao = posicao

	def setValor(self, valor):
		self.__valor = valor

	def setEnderecoImg(self, enderecoImg):
		self.__enderecoImg = enderecoImg

class Peao(Peca):
	def __init__(self, posicao, cor=True):
		cor = 'Brancas' if cor else 'Pretas'
		enderecoImg = 'Img/Pecas' + cor + '/Peao/peao'
		Peca.__init__(self, cor, posicao, 1, enderecoImg)

	def verificaMovimento(self, casa, tabuleiro):
		posicao = casa.getPosicao()
		if Peca.getCor(self) == 'Brancas':
			if casa.getPeca() == None:
				if posicao[0] + 1 != Peca.getPosicao(self)[0]:
					return False
				if posicao[1] != Peca.getPosicao(self)[1]:
					return False
			else:
				if posicao[0] + 1 != Peca.getPosicao(self)[0]:
					return False
				if posicao[1] - 1 != Peca.getPosicao(self)[1] and posicao[1] + 1 != Peca.getPosicao(self)[1]:
					return False
				if  casa.getPeca().getCor() == Peca.getCor(self):
					return False
			return True
		if Peca.getCor(self) == 'Pretas':
			if casa.getPeca() == None:
				if posicao[0] - 1 != Peca.getPosicao(self)[0]:
					return False
				if posicao[1] != Peca.getPosicao(self)[1]:
					return False
			else:
				if posicao[0] - 1 != Peca.getPosicao(self)[0]:
					return False
				if posicao[1] - 1 != Peca.getPosicao(self)[1] and posicao[1] + 1 != Peca.getPosicao(self)[1]:
					return False
				if  casa.getPeca().getCor() == Peca.getCor(self):
					return False
			return True


class Cavalo(Peca):
	def __init__(self, posicao, cor=True):
		cor = 'Brancas' if cor else 'Pretas'
		enderecoImg = 'Img/Pecas' + cor + '/Cavalo/cavalo'
		Peca.__init__(self, cor, posicao, 3, enderecoImg)

	def verificaMovimento(self, casa, tabuleiro):
		posicao = casa.getPosicao()
		
		if ((posicao[0] - 2 == Peca.getPosicao(self)[0] or posicao[0] + 2 == Peca.getPosicao(self)[0]) and
		(posicao[1] - 1 == Peca.getPosicao(self)[1] or posicao[1] + 1 == Peca.getPosicao(self)[1])):
			if casa.getPeca() == None:
				return True
			if casa.getPeca().getCor() != Peca.getCor(self):
				return True
		elif ((posicao[1] - 2 == Peca.getPosicao(self)[1] or posicao[1] + 2 == Peca.getPosicao(self)[1]) and
		(posicao[0] - 1 == Peca.getPosicao(self)[0] or posicao[0] + 1 == Peca.getPosicao(self)[0])):
			if casa.getPeca() == None:
				return True
			if casa.getPeca().getCor() != Peca.getCor(self):
				return True
			
		return False


class Bispo(Peca):
	def __init__(self, posicao, cor=True):
		cor = 'Brancas' if cor else 'Pretas'
		enderecoImg = 'Img/Pecas' + cor + '/Bispo/bispo'
		Peca.__init__(self, cor, posicao, 3, enderecoImg)

	def verificaMovimento(self, casa, tabuleiro):
		posicao = casa.getPosicao()
		diferencaX = posicao[0] - self.getPosicao()[0]
		diferencaY = posicao[1] - self.getPosicao()[1]

		if abs(diferencaX) != abs(diferencaY):
			return False
		
		if casa.getPeca() != None and casa.getPeca().getCor() == self.getCor():
			return False
		
		incrementoJ = 1 if diferencaX == diferencaY else -1
		
		if (diferencaX > 0):

			j = self.getPosicao()[1]
			for i in range(self.getPosicao()[0] + 1, posicao[0]):
				j += incrementoJ
				if tabuleiro[i][j].getPeca() != None:
					return False
		
		else:

			j = posicao[1]
			for i in range(posicao[0] + 1, self.getPosicao()[0]):
				j += incrementoJ
				if tabuleiro[i][j].getPeca() != None:
					return False
		
		return True

class Torre(Peca):
	def __init__(self, posicao, cor=True):
		cor = 'Brancas' if cor else 'Pretas'
		enderecoImg = 'Img/Pecas' + cor + '/Torre/torre'
		Peca.__init__(self, cor, posicao, 5, enderecoImg)

	def verificaMovimento(self, casa, tabuleiro):
		posicao = casa.getPosicao()

		if posicao[0] != self.getPosicao()[0] and posicao[1] != self.getPosicao()[1]:
			return False

		if posicao[0] != self.getPosicao()[0]:

			maior = posicao[0]
			menor = self.getPosicao()[0]

			if self.getPosicao()[0] > posicao[0]:
				
				maior = menor
				menor = posicao[0]
			
			for x in range(menor + 1, maior):
				if tabuleiro[x][posicao[1]].getPeca() != None:
					return False
		
		else:

			maior = posicao[1]
			menor = self.getPosicao()[1]

			if self.getPosicao()[1] > posicao[1]:
				
				maior = menor
				menor = posicao[1]
			
			for x in range(menor + 1, maior):
				if tabuleiro[posicao[0]][x].getPeca() != None:
					return False
		
		if casa.getPeca() != None and casa.getPeca().getCor() == self.getCor():
			return False
		
		return True

		


class Dama(Peca):
	def __init__(self, posicao, cor=True):
		cor = 'Brancas' if cor else 'Pretas'
		enderecoImg = 'Img/Pecas' + cor + '/Dama/dama'
		Peca.__init__(self, cor, posicao, 9, enderecoImg)
		
	def verificaMovimento(self, casa, tabuleiro):
		return Bispo.verificaMovimento(self, casa, tabuleiro) or Torre.verificaMovimento(self, casa, tabuleiro)


class Rei(Peca):  # O rei tem valor absoluto infinito, mas pra facilitar nossa vida definimos com 0
	def __init__(self, posicao, cor=True):
		cor = 'Brancas' if cor else 'Pretas'
		enderecoImg = 'Img/Pecas' + cor + '/Rei/rei'
		Peca.__init__(self, cor, posicao, 0, enderecoImg)

	def verificaMovimento(self, casa, tabuleiro):
		
		posicao = casa.getPosicao()

		if abs(posicao[0] - self.getPosicao()[0]) > 1 or abs(posicao[1] - self.getPosicao()[1]) > 1:
			return False

		if casa.getPeca() != None and casa.getPeca().getCor() == self.getCor():
			return False
		
		return True
