from django.shortcuts import render
from .froms import ReportProblemForm
from server import get_response_from_server

def home(request):   
    response_status = ''
    if request.method == 'POST': #data has arrived - need to handale
        all_fildes = ReportProblemForm(request.POST)
        if all_fildes.is_valid():
            data = all_fildes.cleaned_data #fileds are valid 
            response_status = get_response_from_server(data)

            new_form = all_fildes.save(commit=False) #yet to be saved
            new_form.response_status = response_status
            new_form.save()
    all_fildes = ReportProblemForm()
    return render(request,"home.html",{'response_status': response_status,'report_problem_form' : all_fildes})



