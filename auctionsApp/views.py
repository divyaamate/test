from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import AdminDetailsModel, RegisterUserModel, AuctionModel,userBidModel
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def dashbord(req):
    if (req.session.has_key('user_id')):
        ab=req.session['user_id']
        user=RegisterUserModel.objects.filter(id=ab) 
        product=AuctionModel.objects.all()
        obj={'user':user,'product':product}   
        return render(req,'home_page.html',obj)
    else:
        return redirect('login_user/')
def admin_login(req):
    return render(req,'admin_login.html')
def admin_control_page(req):
    if (req.session.has_key('admin_id')):
        ab=req.session['admin_id']
        admin=AdminDetailsModel.objects.filter(id=ab)
        user_data=RegisterUserModel.objects.all(); 
        obj={'admin':admin,
             "user_data":user_data
             }   
        return render(req,'admin_control_page.html',obj)
    else:
        return redirect('/admin_login')
def do_admin_login(req):
    user_data=AdminDetailsModel.objects.filter(
        admin_mobile=req.POST['almobile'],
        admin_password=req.POST['alpassword']
    )
    if(len(user_data)>0):
        req.session['admin_id']=user_data[0].id
        return redirect('/admin_control_page')
    else:
        return HttpResponse("<script> alert('Login Faild'); history.back();</script>")
def admin_log_out(req):
    del req.session['admin_id']
    return redirect('/')



def register_user(req):
    return render(req,'register_user.html')
def save_new_user(req):
    new_user=RegisterUserModel(
        user_name=req.POST['uname'],
        user_mobile=req.POST['umobile'],
        user_email=req.POST['uemail'],
        user_password=req.POST['upassword'],
        user_image=req.FILES['uimage']
    )
    new_user.save()
    return redirect('/login_user')

def login_user(req):
    return render(req,'login_user.html')

def do_login(req):
    user_data=RegisterUserModel.objects.filter(
        user_name=req.POST['lname'],
        user_password=req.POST['lpassword']
    )
    if(len(user_data)>0):
        req.session['user_id']=user_data[0].id
        return redirect('/')
    else:
        return HttpResponse("<script> alert('Login Faild'); history.back();</script>")

def log_out(req):
    del req.session['user_id']
    return redirect('/login_user')


def edit_user(req):
    obj={
        "user_det" : RegisterUserModel.objects.get(id=req.GET['id'])
    }
    return render(req,"edit_user.html",obj)


def update_user(req):
    print(req.POST)
    old = RegisterUserModel.objects.get(id=req.POST['id'])
    old.user_name = req.POST['user_name']
    old.user_mobile = req.POST['user_mobile']
    old.user_email = req.POST['user_email']
    old.user_password = req.POST['user_password']
    old.save()
    return redirect("/")

def delete_user(req):
    RegisterUserModel.objects.get(id=req.GET['id']).delete()
    return redirect("/")

def user_list(req):
    ab=req.session['admin_id']
    admin=AdminDetailsModel.objects.filter(id=ab);
    user_data=RegisterUserModel.objects.all(); 
    obj={'admin':admin,
             "user_data":user_data
             }   
        
    return render(req,"user_list.html",obj)


def auction(req):
    return render(req,"auction.html")

def save_product(req):
    product=AuctionModel(
    title = req.POST['title'],
    description = req.POST['description'],
    initial_price = req.POST['initial_price'],
    start_date = req.POST['start_date'],
    end_date = req.POST['end_date'],
    created_at = req.POST['created_at'],
    image1 = req.FILES['image1'],
    
    current_price = req.POST['current_price']
    )
    product.save()
    return HttpResponse("<script>alert('Successfully stored your product! <br> keep selling products thank you!');location.href='/'</script>")


def biditem(req):
    product = AuctionModel.objects.get(id=req.GET['id'])
    obj = {'product':product}
    return render(req,'biditem.html',obj)

def validate(req):
    amount=userBidModel(
        user_amount = req.POST['user_amount'],
        
    )
    amount.save()
    return HttpResponse("<script>alert('Successfull <br> keep selling products thank you!');location.href='/'</script>")


    # return redirect("/")
    
    
    