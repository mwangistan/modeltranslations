from django.db import models

class Articles(models.Model):
	class Meta:
		db_table = 'articles'

	title = models.CharField(max_length=50)
	body = models.TextField()
	author = models.CharField(max_length=50, default='unknown')
	date = models.DateTimeField(auto_now_add=True)
