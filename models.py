from typing import Text
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class NewModel(models.Model):
	ch = [
		('pr', 'primary'),
		('sch', 'school'),
		('js', 'javascript'),
		('hw', 'homework'),
		('res', 'result')
	]
	id = models.IntegerField(primary_key=True)
	number1 = models.IntegerField(default=0, validators=[MinValueValidator(10), MaxValueValidator(200)], blank=False)
	number2 = models.IntegerField(default=0, validators=[MinValueValidator(10), MaxValueValidator(200)], blank=False)
	number3 = models.IntegerField(default=0, validators=[MinValueValidator(10), MaxValueValidator(200)], blank=False)
	number4 = models.IntegerField(default=0, validators=[MinValueValidator(10), MaxValueValidator(200)], blank=False)
	number5 = models.IntegerField(default=0, validators=[MinValueValidator(10), MaxValueValidator(200)], blank=False)
	text1 = models.CharField(max_length=100, help_text='')
	text2 = models.CharField(max_length=100, help_text='')
	text3 = models.CharField(max_length=100, help_text='')
	text4 = models.CharField(max_length=100, help_text='')
	text5 = models.CharField(max_length=100, help_text='')
	Text6 = models.TextField(choices=ch)
