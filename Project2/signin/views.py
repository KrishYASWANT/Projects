from django.shortcuts import render
import mysql.connector as sql
# Create your views here.
em=''
pwd=''
add1=''
add2=''
city=''
state=''
zip=''
def signaction(request):
    global em,pwd,add1,add2,city,state,zip
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Krish@321",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
            if key=="add1":
                add1=value
            if key=="add2":
                add2=value
            if key=="city":
                city=value
            if key=="state":
                state=value
            if key=="zip":
                zip=value
        
        c="insert into users Values('{}','{}','{}','{}','{}','{}','{}')".format(em,pwd,add1,add2,city,state,zip)
        cursor.execute(c)
        m.commit()
    
    return render(request,'intro.html')

