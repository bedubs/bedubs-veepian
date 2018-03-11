from django.http import HttpResponse
from django.conf import settings
import os
from django.shortcuts import render


def index(request):
    return HttpResponse("Welcome to Veepian!")


def make_cert(request):
    ovpn_dir = settings.OPENVPN_DIRECTORY
    dir_ls = os.system(f'sudo ls {ovpn_dir}')
    return HttpResponse(f'OpenVPN directory is at {ovpn_dir}. ls is {dir_ls}')
