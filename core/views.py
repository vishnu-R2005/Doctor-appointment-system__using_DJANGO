from django.shortcuts import render,redirect
from .models import Doctor,Patient,Appointment
from django.contrib.auth.models import User
# from django.contrib.auth import login
from django.contrib.auth import authenticate, login,logout


# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
    doctors=Doctor.objects.all()
    appointments=Appointment.objects.all()
    
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        doctor_id=request.POST.get('doctor')
        date=request.POST.get('date')
        time=request.POST.get('time')



        patient=Patient.objects.create(
            name=name,
            age=age,
            phone=phone
        )


        doctor=Doctor.objects.get(id=doctor_id)

        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            date=date,
            time=time
        )

        return redirect('/home/')
    
    return render(request,'home.html',{
                  'doctors':doctors,
                  'appointments':appointments
                  })

def landing(request):
    return render(request, 'landing.html')

def del_appointments(request,id):
    appointment = Appointment.objects.get(id=id)
    appointment.delete()
    return redirect("/home")


def edit_appointment(request,id):
    appointment=Appointment.objects.get(id=id)
    doctors=Doctor.objects.all()


    if request.method =="POST":
        appointment.patient.name=request.POST.get('name')
        appointment.patient.age=request.POST.get('age')
        appointment.patient.phone=request.POST.get('phone')


        doctor_id=request.POST.get('doctor')
        appointment.doctor=Doctor.objects.get(id=doctor_id)


        appointment.date=request.POST.get('date')
        appointment.time=request.POST.get('time')

        appointment.patient.save()
        appointment.save()

        return redirect('/home')
    return render(request,'edit.html',{
        'appointment': appointment,
        'doctors':doctors
    })

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect('/home/')   # ✅ better than render

    return render(request, 'register.html')   # ✅ handles GET


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('/home/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    # 👉 THIS PART FIXES YOUR ERROR
    return render(request, 'login.html')
    

def user_logout(request):
    logout(request)

    return redirect('/login/')