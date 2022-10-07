from django.contrib.sessions.models import Session
from django.db import connection
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm

def index(request):
    return render(request, 'Homepage.html')
def auth(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("pass")
        request.session['username'] = username
        sql = "select * from auth_table where fName = %s and password = %s"
        data = [username,password]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        # print(result)
        columnName = ("id", "fName", "lName", "email", "password", "mNumber")
        res = {
            "data": []
        }
        count = 0
        for w in result:
            # print({columnName[i]:  w[i]for i, _ in enumerate(w)})
            res["data"].append({columnName[i]: w[i] for i, _ in enumerate(w)})

        return render(request, "Auth.html", {"list": res['data'], "logedin": True})
    return render(request, "Auth.html", {"normalUser": True})


def reg(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Registration.html", {'flag':True})
        else:
            return render(request, "Registration.html", {'flag1': True})


    return render(request, "Registration.html", {'flag0': True})

def logout(request):
    # session destroy
    return redirect("/auth/")

def checkdata(request):
    sql = "select * from auth_table"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print(result)
    columnName = ("id", "fName", "lName", "email", "password", "mNumber")
    res = {
        "data": []
    }
    count = 0
    for w in result:
        # print({columnName[i]:  w[i]for i, _ in enumerate(w)})
        res["data"].append({columnName[i]: w[i] for i, _ in enumerate(w)})
        # print(res)

    return render(request, "AllData.html", {"list": res['data'], "logedin": True})

def delete(request, id):
    sql = "delete from auth_table where id = %s"
    print("SQL lin",sql)
    data = [id]
    cursor = connection.cursor()
    cursor.execute(sql, data)
    connection.commit()
    # checkdata()
    return render(request, "AllData.html", {"logedin": True})

def update(request, id):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            id = request.POST.get("id")
            fName = request.POST.get("fName")
            lName = request.POST.get("lName")
            email = request.POST.get("email")
            password = request.POST.get("password")
            mNumber = request.POST.get("mNumber")

            sql = "update auth_table set fName = %s, lName = %s, email = %s, password = %s, mNumber = %s where id = %s"
            data = [fName,lName,email,password,mNumber, id]
            cursor = connection.cursor()
            t1 = cursor.execute(sql, data)
            t2 = connection.commit()
            print(t1, t2)
            return render(request, "Update.html", {'update':True})
        else:
            return render(request, "Update.html", {'notupdate': True})
    else:
        sql = "select * from auth_table where id = %s"
        cursor = connection.cursor()
        print(sql)
        id = [id]
        cursor.execute(sql, id)
        temp = cursor.fetchall()
        columnName = ("id", "fName", "lName", "email", "password", "mNumber")
        res = {
            "data":[]
        }
        for w in temp:
            res["data"].append({columnName[i]: w[i] for i, _ in enumerate(w)})
        return render(request, "Update.html", {"list":res ['data'], "updated": True})

def Create_Session(request):
    request.session['name'] = 'Hello User'
    response = "<h1> Welcome to Sessions</h1><br>"
    response += "ID : {0} <br>".format(request.session.session_key)
    return HttpResponse(response)

def Access_Session(request):
    response = "Name : {0} <br>".format(request.session.get('username'))
    return HttpResponse(response)
def Distroy_Session(request):
    Session.objects.all().delete()
    return render(request, "Auth.html")