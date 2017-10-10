# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from  .models import user
from  .models import question
from  .models import test
# Register your models here.

admin.site.register(user)
admin.site.register(question)
admin.site.register(test)