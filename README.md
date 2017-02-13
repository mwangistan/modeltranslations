# modeltranslations
If you are adding translations to an already existing project you may need to access the original columns marked for translations
which otherwise become "inaccessible" once you run 
```
python manage.py update_translation_fields
```

#Translations.py
To get this original values you'll need to add fallback_values dict to the translations.py and populate the dict
Check out translations.py for the implemenation

