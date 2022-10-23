from django.test import SimpleTestCase
from catalogo.forms import *

class TestForms(SimpleTestCase):

	# TRANSPORTE
	def test_expense_from_no_data(self):
		form = TransporteForm(data={})

		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors), 7)
