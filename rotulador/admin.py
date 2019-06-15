from django.contrib import admin
from .models import Task

admin.site.register(Task)

from .models import Label

admin.site.register(Label)

from .models import Document

admin.site.register(Document)

from .models import Term

admin.site.register(Term)

from .models import OcorrenciaTermo

admin.site.register(OcorrenciaTermo)


