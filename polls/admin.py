from django.contrib import admin # pyright: ignore[reportMissingModuleSource]

from .models import Question

admin.site.register(Question)
# Register your models here.
