from django.urls import path
from django.contrib import admin

import environ
env = environ.Env()
environ.Env.read_env()

def env_admin(request):
    return path(env('admin'), admin.site.urls)
    









