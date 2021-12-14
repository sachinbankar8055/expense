from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from expensetrack.models import Ade
from django.contrib.auth.decorators import login_required

# Create your views here.

def index1(request):

    # ph=destination()
    # ph.price=123456789
    return render(request,'index1.html')





def about(request):

    # ph=destination()
    # ph.price=123456789
    return render(request,'about.html')






def contact(request):

    # ph=destination()
    # ph.price=123456789
    return render(request, 'contact.html')





def register(request):

    if request.method=='POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if username=='' or first_name=='' or last_name=='' or email=='' or password1=='' or password2=='':
            messages.info(request,'Please enter all required information')
            return redirect('register')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                # print('user name already taken ')
                messages.info(request,'user name already exist')
                return redirect('register')
            #elif User.objects.filter(email=email).exists():
                # print('email already taken ')
               # messages.info(request,'email already exist')
               # return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save();
                print('user created')
                messages.info(request,'user created')
                return redirect('login')

            

        else:
            print('password not matching')
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')





def login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid registration')
            print('login')
            return redirect('login')

    else:
        return render(request,'login.html')





@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect('/')





@login_required(login_url='/login') 
def expense(request):
    return render(request,'expense.html')





@login_required(login_url='/login') 
def expens(request):


    alltask=Ade.objects.filter(username=request.user.username)

    context={'tasks':alltask}

    return render(request,'expens.html',context)





@login_required(login_url='/login')
def edit(request,pid):
    e=Ade.objects.get(id=pid)
    
    print(e.date)
    if request.method=="POST":
        username = request.user.username
        date = e.date
        food = int(request.POST['food'])
        petrol = 0 #int(request.POST['petrol'])
        travel = int(request.POST['travel'])
        movie = int(request.POST['movie'])
        rent = 0 # int(request.POST['rent'])
        other = int(request.POST['other'])
       
        sum=food+travel+petrol+movie+rent+other
        print(sum)
       
        if sum>0:

                    e.food=food
                    e.travel=travel
                    e.movie=movie
                    e.other=other
                    e.save()
                    # messages.info(request, 'expense edited succesfully')
                    return redirect('expens')


        else:
                    messages.error(request, 'you did not filled any amount !!')
                    return redirect('edit')
    else:
        context={'a':e}
        return render(request,'edit.html',context)
           
               




@login_required(login_url='/login')
def adexp(request):
    if request.method=="POST":
        username = request.user.username
        date = request.POST['date']
        food = int(request.POST['food'])
        petrol = 0 #int(request.POST['petrol'])
        travel = int(request.POST['travel'])
        movie = int(request.POST['movie'])
        rent = 0 # int(request.POST['rent'])
        other = int(request.POST['other'])
        print("date"+date)
        sum=food+travel+petrol+movie+rent+other
        print(sum)
        if date!="":
            if sum>0:
                if Ade.objects.filter(date=date, username=username).exists():
                    data = Ade.objects.get(date=date, username=username)
                    data.food = int(data.food)+int(food)
                    data.travel =  int(data.travel) +int(travel)
                    data.petrol =  int(data.petrol) +int(petrol)
                    data.movie =int(data.movie) + int(movie)
                    data.rent =int(data.rent) + int(rent)
                    data.other =int(data.other) + int(other)
                    data.save()
                    messages.info(request, 'expense added succesfully')
                    return redirect('adexp')
                else:
                    data = Ade(date=date,food=food,travel=travel,petrol=petrol,movie=movie,rent=rent,other=other,username=username)
                    data.save();
                    messages.info(request, 'expense added succesfully')
                    return redirect('adexp')


            else:
                messages.error(request, 'you did not filled any amount !!')
                return redirect('adexp')
        else:
            messages.error(request, 'Unfortunately!! you missed the date ')
            return redirect('adexp')


    else:
        return render(request, "adexp.html")





def delete_it(request,data_id):
    data = Ade.objects.get( id=data_id)
    data.delete()
    messages.info(request, 'expense deleted succesfully')
    return redirect('/expens')




@login_required(login_url='/login')
def home(request):
    if request.method=='POST' and request.POST['date'] is not '':

        date=request.POST['date']
        print("po0st")
        if Ade.objects.filter(username=request.user.username,date=date).exists():
            data = Ade.objects.get(username=request.user.username, date=date)
            food = int(data.food)
            movie = int(data.movie)
            travel = int(data.travel)
            other = int(data.other)

            total = food + movie + travel + other
            # total=max(total,0.01)
            if total is not 0:
                fpr = round((food / total) * 100)
                spr = round((movie / total) * 100)
                tpr = round((travel / total) * 100)
                opr = round((other / total) * 100)
            else:
                fpr = 0
                spr = 0
                tpr = 0
                opr = 0

            context = {'date': date, 'total': total, 'food': food, 'shopping': movie, 'travel': travel,
                       'other': other, 'fpr': fpr,
                       'spr': spr, 'tpr': tpr, 'opr': opr}

            return render(request, "home.html", context)


        else:
            food = 0
            movie = 0
            travel = 0
            other = 0

            total = food + movie + travel + other
            # total=max(total,0.01)
            if total is not 0:
                fpr = round((food / total) * 100)
                spr = round((movie / total) * 100)
                tpr = round((travel / total) * 100)
                opr = round((other / total) * 100)
            else:
                fpr = 0
                spr = 0
                tpr = 0
                opr = 0

            context = {'date': date, 'total': total, 'food': food, 'shopping': movie, 'travel': travel,
                       'other': other, 'fpr': fpr,
                       'spr': spr, 'tpr': tpr, 'opr': opr}

            return render(request, "home.html", context)

    else:
        print("else po0st")
        data = Ade.objects.filter(username=request.user)
        total = 0
        food = 0
        movie = 0
        travel = 0
        other = 0

        for da in data:
            food +=int(da.food)
            movie +=int(da.movie)
            travel +=int(da.travel)
            other +=int(da.other)


        total = food + movie + travel + other
        # total=max(total,0.01)
        if total is not 0:
            fpr = round((food / total) * 100)
            spr = round((movie / total) * 100)
            tpr = round((travel / total) * 100)
            opr = round((other / total) * 100)
        else:
            fpr = 0
            spr = 0
            tpr = 0
            opr = 0

        context = {'total': total, 'food': food, 'shopping': movie, 'travel': travel, 'other': other, 'fpr': fpr,
                   'spr': spr, 'tpr': tpr, 'opr': opr}
        return render(request, "home.html", context)


        

