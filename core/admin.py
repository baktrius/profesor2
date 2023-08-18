from django.contrib import admin

from .models import Lesson
from .models import FlashCard
from .models import Hint

admin.site.register(Lesson)
admin.site.register(FlashCard)
admin.site.register(Hint)
