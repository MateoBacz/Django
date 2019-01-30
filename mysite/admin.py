#ctl alt l układa tekst
#ctrl / komenty
from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    site_header = 'Moja aplikacja ankietowa z kursu Reaktor PWN'
    site_title = 'Moja aplikacja'
