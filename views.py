

# Create your views here.
# views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from django.db import connection

# Vulnerable Login View
def vulnerable_login(request):
    print("Check")
    print(request.method)
    if request.method == 'POST':
        print("Check 2")
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("Check 2")
        # Vulnerable SQL query prone to SQL injection
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM User WHERE username='%s' AND password='%s'" % (username, password))
        row = cursor.fetchone()
        cursor.close()

        if row:
            return render('shop.html')  # Replace 'success_page' with your actual URL name 

            
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

# Mitigated Login View
'''def mitigated_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Using parameterized queries to prevent SQL injection
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        row = cursor.fetchone()
        cursor.close()

        if row:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})

    return render(request, 'login.html')
'''