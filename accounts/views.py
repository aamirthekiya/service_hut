from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout

def signup(request):
	if request.method == 'POST':

		if request.POST['username'] != "" and request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				context = {
					'error': 'Username has already taken.'
				}
				return render(request, 'signup.html', context)
			except User.DoesNotExist:
				user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
				auth.login(request,user)
				return redirect('login')
		else:
			context = {
				'error': 'Username should not be empty and Passwords must match.'
			}
			return render(request, 'signup.html', context)
	else:
		return render(request, 'signup.html')


def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('create')
		else:
			context = {
				'error': 'Username or password is incorrect'
			}
			return render(request, 'login.html', context)
	else:
		return render(request, 'login.html')


def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('login')
