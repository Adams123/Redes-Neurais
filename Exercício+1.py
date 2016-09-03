import random
aprendizados = [[[+1,-1,-1,-1,+1],[+1,-1,-1,-1,+1],[-1,+1,-1,+1,-1],[-1,+1,-1,+1,-1],[-1,-1,+1,-1,-1]],[[+1,+1,-1,-1,+1],[+1,-1,-1,-1,+1],[-1,+1,-1,+1,-1],[-1,+1,-1,+1,-1],[-1,-1,+1,-1,-1]],[[-1, -1, +1, -1, -1],[-1, +1, -1, +1, -1],[-1, +1, -1, +1, -1],[+1, -1, -1, -1, +1],[+1, -1, -1, -1, +1]],[[-1, -1, +1, -1, -1],[-1, +1, -1, +1, -1],[-1, +1, +1, +1, -1],[+1, -1, -1, -1, +1],[+1, -1, -1, -1, +1]],[[+1,+1,-1,-1,+1],[+1,-1,-1,-1,+1],[-1,+1,+1,+1,-1],[-1,+1,-1,+1,-1],[-1,-1,+1,-1,-1]],[[-1, -1, +1, -1, -1],[-1, +1, -1, +1, -1],[-1, +1, -1, +1, -1],[+1, +1, -1, -1, +1],[+1, -1,+1, -1, +1]],[[+1,-1,+1,-1,+1],[+1,-1,+1,-1,+1],[-1,+1,+1,+1,-1],[-1,+1,-1,+1,-1],[-1,-1,+1,-1,-1]],[[+1, -1, +1, -1, -1],[-1, +1, -1, +1, -1],[-1, +1, -1, +1, -1],[+1, -1, +1, -1, +1],[+1, -1, -1, +1, +1]],[[-1, -1, +1, -1, +1],[-1, +1, +1, +1, -1],[-1, +1, -1, +1, -1],[+1, -1, -1, +1, +1],[+1, -1, +1, -1, +1]],[[+1,-1,+1,-1,+1],[+1,-1,-1,+1,+1],[-1,+1,-1,+1,-1],[+1,+1,-1,+1,+1],[-1,-1,+1,-1,-1]],[[+1,-1,+1,-1,+1],[+1,+1,-1,-1,+1],[-1,+1,+1,+1,-1],[-1,+1,-1,+1,-1],[+1,-1,+1,-1,+1]],[[+1, -1, +1, -1, +1],[-1, +1, -1, +1, -1],[-1, +1, +1, +1, -1],[+1, -1, -1, +1, +1],[+1, -1, +1, -1, +1]]]
saidaEsperada = [-1,-1,1,1,-1,1,-1,1,1,-1,-1,1]

class adaline(object):
	def __init__(self, taxaAprendizado,input,saidaEsperada, temPeso, maxIteracoes, bias):
		self.w=[]
		self.taxaAprendizado=taxaAprendizado
		self.input = input
		self.numeroInputs = len(input)
		self.saidaEsperada = saidaEsperada
		self.maxIteracoes = maxIteracoes
		self.temPeso = temPeso
		self.initW()
		self.saida = []
		self.bias = bias

	def initW(self):
		if(self.temPeso==0):					#seta pesos aleatorios
			for i in range(0,self.numeroInputs):
				self.w.append([])
				for j in range(0,len(self.input[i])):
					self.w[i].append([])
					for k in range(0,len(self.input[i][j])):
						self.w[i][j].append(random.uniform(-1,1))
		else:							#seta pesos nulos
			for i in range(0,self.numeroInputs):
				self.w.append([])
				for j in range(0,len(self.input[i])):
					self.w[i].append([])
					for k in range(0,len(self.input[i][j])):
						self.w[i][j].append(0)

	def calcOutput(self, testeCase):
		output = 0
		for j in range (0,len(self.input[testeCase])): #matriz do caso de teste
			for k in range(0,len(self.input[testeCase][j])): #elemento de cada linha de cada caso de teste
				output += self.input[testeCase][j][k] * self.w[testeCase][j][k] + self.bias#calcula output
		return output

	def calcAll(self):
		output = 0
		for i in range(0,len(self.input)): #casos de teste
			for iter in range(0,self.maxIteracoes):
				output = 0
				output = self.calcOutput(i)
				for j in range(0,len(self.input[i])): #linhas do caso i
					for k in range(0,len(self.input[i][j])): #elemento do caso i da linha j
						self.w[i][j][k]=self.w[i][j][k]+self.taxaAprendizado*(self.saidaEsperada[i]-output)*self.input[i][j][k]
	#peso do elemento k da linha j do teste i = peso do elemento k da linha j do teste i + taxa de aprendizado * (saida esperada do teste i - saida da ultima iteracao do teste i)*elemento k da linha j do teste i
			self.saida.append(output)


ada = adaline(0.025,aprendizados,saidaEsperada,1,1000,0)
ada.calcAll()
print ada.saida