# keygen views.py
# Django modules
from django.shortcuts import render, redirect
from django.contrib import messages
from django_rq import job
import time

# My modules
from .models import Secret

@job
def generate_bg():
    time.sleep(2) # Simulate expensive operation
    Secret.objects.create()


def index(request):
    context = {'secrets': Secret.objects.all()}
    return render(request, 'keygen/index.html', context)


def generate(request):
    """
    Generate keys
    """
    if request.GET.get('bg'):
        generate_bg.delay()
        messages.success(request, 'Generating new key in backgroun. Refresh after two seconds to se generated key.')
    else:
        Secret.objects.create()
        messages.success(request, 'Generated new key.')
    return redirect('home')


def delete(request):
    """
    Detele keys
    """
    Secret.objects.all().delete()
    messages.success(request, 'Deleted all keys.')
    return redirect('home')