from django.test import SimpleTestCase
from catalogo.forms import *

class TestForms(SimpleTestCase):

	# TOUR
	def test_expense_from_no_data(self):
		form = TourForm(data={})

		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors), 4)
