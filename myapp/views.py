from django.http import HttpResponse
from django.shortcuts import render
import joblib


def home_page(request):
    return render(request,'home_page.html')

def index(request):
    return render(request ,'index.html') 

def result(request):

    model = joblib.load(" ")
    info_list = []
    lis = []
    info_list.append(request.POST['name'])
    info_list.append(request.POST['surname'])
    
    #####
    lis.append(int(request.POST['age']))
    lis.append(int(request.POST['anaemia']))
    lis.append(int(request.POST['creatine_pho']))
    lis.append(int(request.POST['diabetes']))
    lis.append(int(request.POST['ejec_fra']))
    lis.append(int(request.POST['high_blood']))
    lis.append(int(request.POST['platelets']))
    lis.append(float(request.POST['serum_cre']))
    lis.append(int(request.POST['serum_sod']))
    lis.append(int(request.POST['sex']))
    lis.append(int(request.POST['smoking']))
    lis.append(int(request.POST['time']))
    
    ans = model.predict([lis])
    prob_pred = model.predict_proba([lis])

    print(info_list)
    print(lis)
    print(ans)
    print(prob_pred)
      

    return render(request,'result.html',{'info_list':info_list,'ans':ans,'prob_pred':prob_pred,'lis':lis})

