from django.test import SimpleTestCase
from catalogo.forms import *

class TestForms(SimpleTestCase):

	# USUARIO
	def test_expense_from_no_data(self):
		form = UsuarioForm(data={})

		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors), 11)
