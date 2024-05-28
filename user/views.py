from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm

from .models import User

# Create your views here.

# Index View
def index(request):

    if request.user.is_authenticated: # If the user is already logged in redirect to home page
        return redirect("dashboard")
    return render(request, "index.html", {})

# Logout handler
def logout_request(request):

    logout(request)
    messages.success(request, ("Successfully logged out!"))
    # return redirect("main:homepage") # Could be useful to use this syntax
    return redirect('login')

# Login View
def new_login(request):

    if request.user.is_authenticated: # If the user is already logged in redirect to home page
        return redirect("dashboard")

    if request.method == "POST": # If the user clicked the login button

        # Get data from forms
        username = request.POST['floatingInput']
        password = request.POST['floatingPassword']

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None: # If user was authenticated
            login(request, user)

            if not request.POST.get('rememberMe', None): # If user did not check 'rememer me', set session to expire once user has left page
                request.session.set_expiry(0)

            return redirect('dashboard')

        else: # Error while authenticating

            messages.success(request, ("There was an error while logging in, please try again!"))
            return redirect('login')
    return render(request, "login.html", {})

# New Login View
def new_new_login(request):

    context = {}

    if request.user.is_authenticated: # If the user is already logged in redirect to home page
        return redirect("dashboard")

    if request.method == "POST": # If the user clicked the login button

        if request.POST['form'] == 'login':

            # Get data from forms
            username = request.POST['loginEmailAddress']
            password = request.POST['loginPassword']

            # Authenticate user
            user = authenticate(request, username=username, password=password)
            
            if user is not None: # If user was authenticated
                login(request, user)

                if not request.POST.get('rememberMe', None): # If user did not check 'rememer me', set session to expire once user has left page
                    request.session.set_expiry(0)

                return redirect('dashboard')

            else: # Error while authenticating
                messages.success(request, ("There was an error while logging in, please try again!"))
                return redirect('login')
            
        elif request.POST['form'] == 'signup':

            # Access Code

            if request.POST.get('signupOrganization') == "Stillwater":
                if request.POST.get('signupAccessCode') != "48JKwsR8":
                    messages.success(request, ("Incorrect acccess code!"))
                    return redirect(reverse('login') + '?form=signup')
            elif request.POST.get('signupOrganization') == "City B":
                if request.POST.get('signupAccessCode') != "newAccessCode":
                    messages.success(request, ("Incorrect acccess code!"))
                    return redirect(reverse('login') + '?form=signup')

            # Get data from forms
            first_name = request.POST.get('signupFirstName')
            last_name = request.POST.get('signupLastName')
            email = request.POST.get('signupEmail')
            password1 = request.POST.get('signupPassword')
            password2 = request.POST.get('signupConfirmPassword')
            oraganization = request.POST.get('signupOrganization')
            title = request.POST.get('signupTitle')
            phone_number = request.POST.get('signupPhone')

            # Error handling
            if first_name == '':
                messages.success(request, ("Please enter a valid first name!"))
                return redirect(reverse('login') + '?form=signup')
            elif last_name  == '':
                messages.success(request, ("Please enter a valid last name!"))
                return redirect(reverse('login') + '?form=signup')
            elif email  == '':
                messages.success(request, ("Please enter a valid email address!"))
                return redirect(reverse('login') + '?form=signup')
            elif password1  == '':
                messages.success(request, ("Please enter a valid password!"))
                return redirect(reverse('login') + '?form=signup')
            elif oraganization == '':
                messages.success(request, ("Please enter a valid organization!"))
                return redirect(reverse('login') + '?form=signup')
            elif title == '':
                messages.success(request, ("Please enter a valid title!"))
                return redirect(reverse('login') + '?form=signup')
            elif phone_number  == '':
                messages.success(request, ("Please enter a valid phone number!"))
                return redirect(reverse('login') + '?form=signup')
            elif phone_number.isdigit() is not True:
                messages.success(request, ("Please only enter numerical values for phone number!"))
                return redirect(reverse('login') + '?form=signup')
            elif password1 != password2:
                messages.success(request, ("Passwords do not match!"))
                return redirect(reverse('login') + '?form=signup')
            else:
                # All fields are valid, create user, login, and redirect
                account = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password1, organization=oraganization, title=title, phone_number=phone_number)
                login(request, account)
                return redirect("dashboard")
    
    return render(request, "new_login.html", context)



# Signup view and registration handler
def signup(request):

    if request.user.is_authenticated: # If the user is already logged in redirect to home page
        return redirect("dashboard")

    context = {} # Init context dict
    if request.POST: # If the user clicked 'sign up' button
        form = RegistrationForm(request.POST)

        # Get data from forms
        first_name = request.POST.get('floatingFirstName')
        last_name = request.POST.get('floatingLastName')
        email = request.POST.get('floatingInput')
        password1 = request.POST.get('floatingPassword')
        password2 = request.POST.get('floatingConfirmPassword')
        oraganization = request.POST.get('floatingOrganization')
        title = request.POST.get('floatingTitle')
        phone_number = request.POST.get('floatingPhoneNumber')

        # Error handling
        if first_name == '':
            messages.success(request, ("Please enter a valid first name!"))
            return redirect('signup')
        elif last_name  == '':
            messages.success(request, ("Please enter a valid last name!"))
            return redirect('signup')
        elif email  == '':
            messages.success(request, ("Please enter a valid email address!"))
            return redirect('signup')
        elif password1  == '':
            messages.success(request, ("Please enter a valid password!"))
            return redirect('signup')
        elif oraganization == '':
            messages.success(request, ("Please enter a valid organization!"))
            return redirect('signup')
        elif title == '':
            messages.success(request, ("Please enter a valid title!"))
            return redirect('signup')
        elif phone_number  == '':
            messages.success(request, ("Please enter a valid phone number!"))
            return redirect('signup')
        elif phone_number.isdigit() is not True:
            messages.success(request, ("Please only enter numerical values for phone number!"))
            return redirect('signup')
        elif password1 != password2:
            messages.success(request, ("Passwords do not match!"))
            return redirect('signup')
        else:
            # All fields are valid, create user, login, and redirect
            account = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password1, organization=oraganization, title=title, phone_number=phone_number)
            login(request, account)
            return redirect("home")

    # If the user is just requesting the signup page
    form = RegistrationForm()
    context['form'] = form
    return render(request, "signup.html", context)