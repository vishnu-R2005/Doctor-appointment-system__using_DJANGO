from django.shortcuts import render,redirect
from .models import Doctor,Patient,Appointment

# Create your views here.


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

        return redirect('/')
    
    return render(request,'home.html',{
                  'doctors':doctors,
                  'appointments':appointments
                  })

def del_appointments(request,id):
    appointment = Appointment.objects.get(id=id)
    appointment.delete()
    return redirect("/")


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

        return redirect('/')
    return render(request,'edit.html',{
        'appointment': appointment,
        'doctors':doctors
    })