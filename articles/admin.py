from django.contrib import admin

from .models import Article, Topic, Scope


from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

#
# class ScopeInlineFormset(BaseInlineFormSet):
#     def clean(self):
#         for form in self.forms:
#             form.cleaned_data
#             raise ValidationError('Тут всегда ошибка')
#         return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    pass


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
