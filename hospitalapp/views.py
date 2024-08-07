from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Contact
from .models import Booking
from datetime import datetime
from django.utils import timezone
# Create your views here.
def about(request):
    return render(request,"about.html")
def doctors(request):
    return render(request,"doctors.html")
#login chatgpt


# def login_page(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Debug print to check email value
#         print(f"Email: {email}")

#         # Check if the email address is registered
#         if not User.objects.filter(email=email).exists():
#             messages.error(request, "Email address not found!")
#             return redirect('/login/')
        
#         # Get the user object by email
#         user = User.objects.get(email=email)
        
#         # Authenticate using the username
#         user = authenticate(request, username=user.username, password=password)
        
#         if user is None:
#             messages.error(request, "Invalid password")
#             return redirect('/login/')
#         else:
#             login(request, user)
#             return redirect('/appointment/')
    
#     return render(request, "login.html")

def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not User.objects.filter(email=email).exists():
            messages.error(request, "Email address not found!")
            return redirect('/login/')
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is None:
                messages.error(request, "Invalid Password")
                return redirect('/login/')
            else:
                login(request, user)
                return redirect('/meetup/')
        except:
            messages.error(request, "Email not found")
            return redirect('/login/')
    return render(request, "login.html")

##login


def index(request):
    return render(request,"index.html")
def privacy(request):
    return render(request,"privacy.html")
#chatgpt register


# def registration(request):
#     if request.method == "POST":
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         # confirmpassword = request.POST.get('confirmpassword')

#         # Debug prints
#         print(f"First Name: {first_name}")
#         print(f"Last Name: {last_name}")
#         print(f"Username: {username}")
#         print(f"Email: {email}")
#         print(f"Password: {password}")

#         # Check if the username already exists
#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists")
#             return redirect('/registration/')
        
#         # Check if the email already exists
#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email already exists")
#             return redirect('/registration/')
        
#         # Create the user
#         user = User.objects.create_user(
#             first_name=first_name,
#             last_name=last_name,
#             username=username,
#             email=email,
#             password=password
#         )
        
#         # Inform the user of the successful registration
#         messages.info(request, "Registration successful!")
#         return redirect('/login/')
    
#     return render(request, "registration.html")


#register
def registration(request):
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
       # confirmpassword=request.POST.get('confirmpassword'),
        #for checking that email address is not same
        if User.objects.filter(username=username).exists():
            messages.error(request,"username is already exist")
            return redirect('/registration/')
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email is already exist")
            return redirect('/registration/')
        if password and confirmpassword and password != confirmpassword: 
           messages.error(request,"Password couldnot match") 
           return redirect('/registration/')
        user=User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
            )
        user.save()
        messages.info(request,"REGISTRATION SUCCESSFULLY!!!!!!!!!!!")
        return redirect('/login/')
    return render(request,"registration.html")


def gallary(request):
    return render(request,"gallary.html")


def terms(request):
    return render(request,"terms.html")


def blog(request):
    return render(request,"blog.html")

def contact(request):
    if request.method == "POST":
        data=request.POST
        Name=data.get('Name')
        Email=data.get('Email')
        Subject=data.get('Subject')
        Phone=data.get('Phone')
        Message=data.get('Message')
        
        Contact.objects.create(
            Name=Name,
            Email=Email,
            Subject=Subject,
            Phone=Phone,
            Message=Message,
        )
        
        redirect('/contact/')
    return render(request,"contact.html")

@login_required(login_url='login')
def appointment(request):
    user_email=request.user.email if request.user.is_authenticated else None
    if request.method == "POST":
        data = request.POST
        Name = data.get('Name')
        Email = data.get('Email',user_email)
        Purpose = data.get('Purpose')
        Phone = data.get('Phone')
        Surgury = data.get('Surgury')
        Date = data.get('Date')
        Time = data.get('Time')
        today = timezone.localdate()
        appointment_date = datetime.strptime(Date, '%Y-%m-%d').date()
        
        if Booking.objects.filter(Email=Email).exists():
            messages.error(request, "Email address already used for a booking!")
            return redirect('/appointment/')
        if appointment_date < today:
            messages.error(request, "You cannot book an appointment for past days!")
            return redirect('/appointment/')
        if not Name or not Email or not Purpose or not Phone or not Surgury or not Date or not Time:
            messages.error(request, "All fields are required!")
            return redirect('/appointment/')
        
        if Booking.objects.filter(Surgury=Surgury, Date=Date, Time=Time).exists():
            messages.error(request, "Sorry, this slot is already booked. Please select another.")
            return redirect('/appointment/')
        
        # Associate the booking with the logged-in user
        Booking.objects.create(
            user=request.user,
            Name=Name,
            Email=Email,
            Purpose=Purpose,
            Phone=Phone,
            Surgury=Surgury,
            Date=Date,
            Time=Time,
        )
        
        messages.success(request, "Appointment booked successfully!")
        return redirect('/meetup/')
    
    return render(request, "appointment.html")


        # Associate the booking with the logged-in use

def log_out(request):
    logout(request)
    return redirect("/login/")

def meetup(request):
    bookings = Booking.objects.filter(user=request.user)
    
    if not bookings.exists():
        context = {'message': "You don't have an appointment. Please book an appointment."}
    else:
        context = {'bookings': bookings}
    
    return render(request, "meetup.html", context)

