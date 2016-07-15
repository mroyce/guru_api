from django.db import models


class BaseGuruModel(models.Model):
	"""
	Base Model class
	"""
	created_at = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True
