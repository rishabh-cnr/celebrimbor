from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import uploadPageForm
from .funtions import page_manager


def uploadPage(request):
    print('inside views')
    if request.method == 'POST':
        form = uploadPageForm(request.POST)
        print('inside POST')
        if form.is_valid():
            path = form.cleaned_data.get('path')
            print(path)  # prints the value of path
            return HttpResponse('PAGE UPLOADED')


        # page = uploadPageForm(request.POST, request.FILES)
        # if page.is_valid():  
        #     # check_upload = page_manager.handle_uploaded_file(request.FILES['file'])
        #     check_upload = page_manager.clone_project(request.)
        #     if check_upload == True:
        #         return HttpResponse('PAGE UPLOADED')
        #         #link site to display uploaded html page
        #         # return redirect(displayResume)
        #     elif check_upload == False:
        #         return HttpResponse('UPLOAD UNSUCCESSFUL')
        #         #redirect to upload file
        #     elif check_upload == 'TYPE':
        #         return HttpResponse('UPLOAD .html file')
        #         #display error and redirect to upload file

    else:
        print('inside else')
        page = uploadPageForm() 
        print(page)
        print('type : ',type(page))
        return render(request,"upload_page.html",{'form':page})