from django.shortcuts import render

# Create your views here.

# I want 2 views to do the oob circle.  
# The 2 htmx request are responding with 2 different partial page. 
# the msg to the context,
# just to know what I did and where I m
# in the DOM , to understand the mechanism.

def Home1(request):
    
    context={}
    
    msg="I call the  def Home1 with htmx, response homepartial1.html"
    context ={
                'msg':msg,
             }
    
    if request.htmx:
        return render(request,'homepartial1.html',context)        
    else:
        msg="The initial home page def home1 ,without htmx, response home.html"
        context ={
                'msg':msg,
             }
    return render(request,'home.html',context)

def Home2(request):
    
    context={}
    
    msg="I call the  def Home2 with htmx, response homepartial2.html"
    context ={
                'msg':msg,
             }

    if request.htmx:
        return render(request,'homepartial2.html',context)        
    return render(request,'home.html',context)