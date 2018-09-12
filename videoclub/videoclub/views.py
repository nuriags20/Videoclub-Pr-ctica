from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('pagVideoclub:videoclub')
		else:
			print ("Login error " + username + " " + password)
			return render(request,'index.html')
	else:
		return render(request,'index.html')