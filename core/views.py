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