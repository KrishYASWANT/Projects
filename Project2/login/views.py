# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_protect
# from django.shortcuts import render, redirect
# from .models import User
# # Create your views here.
# # def login(request):
# #     return render(request, 'login.html')
# @csrf_protect
# def login(request):
#     if request.method == 'POST':
#         csrf_token = request.POST['csrfmiddlewaretoken']
#         email = request.POST['email']
#         password = request.POST['password']

#         try:
#             user = User.objects.get(email=email)

#             if user.password == password:
#                 # Password matches, perform login logic
#                 # Redirect to a success page or perform other actions
#                 #print("sucess")
#                 return redirect('success')
#             else:
#                 # Password doesn't match
#                 return render(request, 'login.html', {'error': 'Invalid email or password.'})

#         except User.DoesNotExist:
#             # User with the provided email doesn't exist
#             return render(request, 'login.html', {'error': 'Invalid email or password.'})

#     return render(request, 'login.html')




# @csrf_protect
# def login(request):
#     if request.method == 'POST':
#         csrf_token = request.POST['csrfmiddlewaretoken']
#         # Rest of your form handling logic

#     return render(request, 'login.html')


from django.shortcuts import render, redirect
#from .models import User
import mysql.connector as sql

def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Krish@321",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,'welcome.html')
      
    
    return render(request,'login.html')





# def login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

#         try:
#             user = User.objects.get(email=email)

#             if user.password == password:
#                 # Password matches, perform login logic
#                 # Redirect to a success page or perform other actions
#                 return redirect('success')
#             else:
#                 # Password doesn't match
#                 return render(request, 'login.html', {'error': 'Invalid email or password.'})

#         except User.DoesNotExist:
#             # User with the provided email doesn't exist
#             return render(request, 'login.html', {'error': 'Invalid email or password.'})

#     return render(request, 'login.html')

