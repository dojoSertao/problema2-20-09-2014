import unittest
from JKP import joga

class Teste_JKP(unittest.TestCase):
	
	def test_se_for_pedra_e_papel(self):
		self.assertEqual(joga('pedra','papel'),'papel')

	def test_se_for_papel_e_pedra(self):
		self.assertEqual(joga('papel','pedra'),'papel')

	def test_se_for_tesoura_e_pedra(self):
		self.assertEqual(joga('tesoura','pedra'),'pedra')

	def test_se_for_pedra_e_tesoura(self):
		self.assertEqual(joga('pedra','tesoura'),'pedra')

	def test_se_for_tesoura_e_papel(self):
		self.assertEqual(joga('tesoura','papel'),'tesoura')

	def test_se_for_papel_e_tesoura(self):
		self.assertEqual(joga('papel','tesoura'),'tesoura')

unittest.main()