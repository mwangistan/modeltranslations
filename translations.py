from modeltranslation.translator import translator, TranslationOptions
from app.models import Articles

fallback_values = {}

class ArticlesTranslations(TranslationOptions):
	instances = Articles.objects.all()
	fields = ('title', 'body')

	if len(instances) > 0:
		for instance in instances:
			fallback_values.update({'title':instance.__dict__['title'],
				'body':instance.__dict__['body']})
	else:
		fallback_values = {}
