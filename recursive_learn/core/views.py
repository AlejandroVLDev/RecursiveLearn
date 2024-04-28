from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

from .forms import SignUpForm, EmailChangeForm, EmailSubmitPasswordChange, VerificationCodePasswordChange, ChangePasswordForm
from .models import Profile

import secrets
import smtplib
from email.message import EmailMessage
import ssl
import os


# Create your views here.


def index(request):
    return render(request, 'core/index.html')


@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            profile = Profile()
            profile.user = user
            profile.save()
            return redirect('core:login')
    else:
        form = SignUpForm()

    content = {
        'form': form,
    }
    return render(request, 'user/signup.html', content)


@csrf_protect
@login_required
def update_email(request):
    if request.method == 'POST':
        form = EmailChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('core:change_email_done')
    else:
        form = EmailChangeForm(request.user)

    content = {
        'form': form,
    }
    return render(request, 'user/update_email.html', content)


@login_required
def change_email_done(request):
    content = {
        'title': 'correo',
    }
    return render(request, 'user/change_done.html', content)


@login_required
def change_password_done(request):
    content = {
        'title': 'contraseña',
    }
    return render(request, 'user/change_done.html', content)


@login_required
def details_user(request):
    user = request.user
    mail = str(user.email)
    extension_index = mail.rfind('.')
    at_sign_index = mail.index('@')
    if at_sign_index >= 5:
        if extension_index - at_sign_index >= 3:
            mail = mail[:2] + '*****' + mail[at_sign_index-2:at_sign_index] + '@' + \
                mail[at_sign_index+1:at_sign_index+3] + \
                '*****.' + mail[extension_index+1:]
        else:
            mail = mail[:2] + '*****' + mail[at_sign_index-2:at_sign_index] + '@' + \
                mail[at_sign_index+1:at_sign_index+2] + \
                '*****.' + mail[extension_index+1:]
    else:
        if extension_index - at_sign_index >= 3:
            mail = mail[:1] + '*****' + mail[at_sign_index-1:at_sign_index] + '@' + \
                mail[at_sign_index+1:at_sign_index+3] + \
                '*****.' + mail[extension_index+1:]
        else:
            mail = mail[:1] + '*****' + mail[at_sign_index-1:at_sign_index] + '@' + \
                mail[at_sign_index+1:at_sign_index+2] + \
                '*****.' + mail[extension_index+1:]
    content = {
        'mail': mail,
    }
    return render(request, 'user/details_user.html', content)


@login_required
def logout_view(request):
    logout(request)
    return redirect('core:login')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


@csrf_protect
def restore_password_mail(request):
    if request.method == 'POST':
        form = EmailSubmitPasswordChange(request.POST)

        if form.is_valid():
            user_mail = form.cleaned_data['email']
            user = User.objects.filter(email__exact=user_mail).first()
            if user:
                token = secrets.randbelow(899999) + 100000
                profile = get_object_or_404(Profile, user=user)
                profile.code_change = token
                profile.save()
                _send_mail(user_mail, token)
                request.session['token'] = 'yes'
                request.session['my_user_mail'] = user_mail
            
            return redirect('core:verification_step')
    else:
        form = EmailSubmitPasswordChange()

    content = {
        'form': form,
    }
    return render(request, 'user/restore_password_mail.html', content)


@csrf_protect
def verification_step(request):
    if 'token' in request.session:
        if request.session['token'] != 'yes':
            return PermissionDenied()
    else:
        return PermissionDenied()
    
    if request.method == 'POST':
        form = VerificationCodePasswordChange(request.POST)

        if form.is_valid():
            token = form.cleaned_data['code']
            user_mail = request.session['my_user_mail']
            user = User.objects.get(email__exact=user_mail)
            profile = get_object_or_404(Profile, user=user)
            request.session['token'] = 'no'
            request.session['password_change'] = 'yes'
            if profile.code_change == token:
                return redirect('core:restore_password')
            else:
                return redirect('core:error_verification')
    else:
        form = VerificationCodePasswordChange()

    content = {
        'form': form,
    }
    return render(request, 'user/verification_step.html', content)


def error_verification(request):
    return render(request, 'user/error_verification.html')


@csrf_protect
def restore_password(request):
    if 'password_change' in request.session:
        if request.session['password_change'] != 'yes':
            return PermissionDenied()
    else:
        return PermissionDenied()
    
    user_mail = request.session['my_user_mail']
    user = User.objects.get(email__exact=user_mail)

    if request.method == 'POST':
        form = ChangePasswordForm(user, request.POST)

        if form.is_valid():
            password = form.cleaned_data['new_password1']
            user.set_password(password)
            user.save()
            request.session['my_user_mail'] = ''
            request.session['password_change'] = 'no'
            return render(request, 'user/restore_password_done.html')
    else:
        form = ChangePasswordForm(user)

    content = {
        'form': form,
    }
    return render(request, 'user/restore_password.html', content)


def restore_password_done(request):
    return render(request, 'user/restore_password_done.html')


def _send_mail(mail, code):
    body = 'Tu código para cambiar la contraseña es:\n {}'.format(code)
    subject = 'Código de recuperación contraseña LeapOfFaith'

    user = 'no.responder.leap.of.faith@gmail.com'
    # TODO: os.environ.get('EMAIL_PASSWORD')
    password = 'dhkazjmwqkwbuarm'

    em = EmailMessage()
    em['From'] = user
    em['To'] = mail
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(user, password)
        smtp.sendmail(user, mail, em.as_string())


def my_custom_page_not_found_view(request, exception):
    context = {
        'error': exception,
        'title': 'ERROR 404',
        'title_extra': 'PAGE NOT FOUND',
    }
    return render(request, 'error/40X.html', status=404, context=context)


def my_custom_error_view(request):
    return render(request, 'error/500.html', status=500)


def my_custom_permission_denied_view(request, exception):
    context = {
        'error': exception,
        'title': 'ERROR 403',
        'title_extra': 'FORBIDDEN',
    }
    return render(request, 'error/40X.html', status=403, context=context)


def my_custom_bad_request_view(request, exception):
    context = {
        'error': exception,
        'title': 'ERROR 400',
        'title_extra': 'BAD REQUEST',
    }
    return render(request, 'error/40X.html', status=400, context=context)
