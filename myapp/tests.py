from django.test import TestCase

from catalog.models import AuthorModel as Author

class YourTestClass(TestCase):

	@classmethod
	def setUpTestData(cls):
		Author.objects.create(first_name="Ivan", last_name="Ivanov")
		print("Author was created.")

	def setUp(self):
		print("setUp: Running")
		pass

	def tearDown(self):
		print("tearDown: Running")
		pass

	def test_max_length_first_name(self):
		author = Author.objects.get(id=1)
		field_length = author._meta.get_field('first_name').max_length 
		return self.assertEquals(field_length, 100)

	def test_field_label_first_name(self):
		author = Author.objects.get(id=1)
		field_label = author._meta.get_field('first_name').verbose_name 
		return self.assertEquals(field_label, 'first name')
