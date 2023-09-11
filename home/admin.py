from django.contrib import admin
from .models import SolvedCase, SolvedCaseFile
# Register your models here.


class SolvedCaseFileInLine(admin.StackedInline):
    model = SolvedCaseFile
    extra = 1

class SolvedCaseAdmin(admin.ModelAdmin):
    model = SolvedCase
    inlines = [SolvedCaseFileInLine]


admin.site.register(SolvedCase, SolvedCaseAdmin)
