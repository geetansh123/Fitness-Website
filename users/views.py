from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from users.forms import RegistrationForm,LoginForm
from django.contrib import messages
from users.models import NewUser

def home(request):
    return render(request, 'users/home.html')
    

def about(request):
    return render(request, 'users/about.html')

def accounts(request):
    userna = request.user
    workout = []
    workout_number=[]
    cardio = ["Cardio","Running/Skipping: 60 secs", "Mountain Climbers: 45 secs", "Burpees: 45 secs", "Lunges: 45 secs","Butt Kicks: 45 secs","Jumping Jacks: 45 secs"]
    total_body = ["Total Body","Pushups", "Plank", "Squat", "Close Grip Pushups", "Lunges", "Leg Raises"]
    endurance = ["Endurance","Running/Skipping", "Boat Hold", "Mountain climbers", "Wall Sit","Burpees", "Plank Hold"]
    yoga = ["Yoga", "Standing Forward Bend", "Tree", "Triangle", "Seated Forward Bend", "Garland", "Happy Baby"]
    reps=""
    workout1 = ""
    workout2 = ""
    workout3 = ""
    age=userna.age
    height=userna.height
    weight=userna.weight
    gender=userna.gender
    goal=userna.goal
    fit_weight=(height/30)*12
    bmi = str(weight / ((height / 100)** 2))
    bmi = float(bmi[:5])
    goal = goal.lower()
    if goal == "improve endurance":
        goal = "endurance"
        reps="Till Failure"
    elif goal == "basic fitness":
        goal = "basic"
        reps="12-15"
    if gender=="female":
        rang=26
    else:
        rang=24
    if age<40:
        if goal == "lean" or goal == "strength":
            reps="4-7"
            if bmi>rang:
                cardio_number = 3
                total_number = 3
                endurance_number = 0
                yoga_number=0
            else:
                cardio_number = 2
                total_number = 4
                endurance_number = 0
                yoga_number=0
        elif goal=="bulky" and bmi>rang:
            cardio_number = 2
            total_number = 4
            endurance_number = 0
            yoga_number=0
        elif goal=="bulky" and bmi<rang:
            cardio_number = 0
            total_number = 5
            endurance_number = 0
            yoga_number=0
        elif goal=="endurance" or goal=="stamina":
            cardio_number = 0
            total_number = 2
            endurance_number = 3
            yoga_number=0
        elif goal=="basic":
            if bmi>24:
                cardio_number = 4
                total_number = 2
                endurance_number = 0
                yoga_number=0
            else:
                cardio_number = 3
                total_number = 3
                endurance_number = 0
                yoga_number=0
    elif age>=40 and age<=50:
        if goal=="lean":
            if bmi>rang:
                cardio_number = 3
                total_number = 2
                endurance_number = 0
                yoga_number=0
            else:
                cardio_number = 2
                total_number = 3
                endurance_number = 0
                yoga_number=0
        elif goal=="bulky" and bmi>rang:
            cardio_number = 1
            total_number = 3
            endurance_number = 0
            yoga_number=0
        elif goal=="bulky" and bmi<rang:
            cardio_number = 0
            total_number = 4
            endurance_number = 0
            yoga_number=0
        elif goal=="basic":
            if bmi>rang:
                cardio_number = 2
                total_number = 1
                yoga_number=1
                endurance_number = 0
            else:
                cardio_number = 1
                total_number = 1
                yoga_number=2
                endurance_number = 0
    else:
        cardio_number = 1
        total_number = 1
        yoga_number=3
        endurance_number = 0
    if weight>fit_weight:
        time=int((weight-fit_weight)/1.3)+1
    else:
        time = 0
    l=[]

    cardio_number=0
    if cardio_number != 0:
        workout1 = "Cardio"
        workout1_main = cardio
        l.append(workout1_main)
        if yoga_number != 0:
            workout3 = "Yoga"
            workout3_main = yoga
            l.append(workout3_main)
        else:
            workout3 = workout1
            workout3_main=workout1_main
        #workout.append("cardio")
        #workout_number.append(cardio_number)
    workout2 = "Total Body"
    workout2_main = total_body
    l.append(workout2_main)
        #workout.append("total")
        #workout_number.append(total_number)
    if endurance_number != 0:
        l.append(workout1_main)
        workout1 = "Endurance"
        workout1_main = endurance
        if yoga_number != 0:
            l.append(workout3_main)
            workout3 = "Yoga"
            workout3_main = yoga
        else:
            workout3 = workout1
            workout3_main=workout1_main

    return render(request,'users/account.html',context = {"reps":reps,"l":l,"time":time,"bmi":bmi,"workout1":workout1,"workout2":workout2,"workout3":workout3,"workout3_main":workout3_main,"workout1_main":workout1_main,"workout2_main":workout2_main})

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f"New Account Created: {email}")
            messages.info(request,f"You are now logged in as {email}")
            email = form.cleaned_data.get('email')
            raw_password=form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'users/register.html', context)
    
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")


def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                messages.info(request, f"You are now logged in as {email}")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = LoginForm()
    return render(request = request,
                    template_name = "users/login.html",
                    context={"form": form})
        
