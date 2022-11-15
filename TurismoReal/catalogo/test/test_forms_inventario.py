from django.test import SimpleTestCase
from catalogo.forms import *

class TestForms(SimpleTestCase):

	# INVENTARIO
	def test_expense_from_no_data(self):
		form = InventarioForm(data={})

		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors), 6)
