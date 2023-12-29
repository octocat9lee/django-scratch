from django.shortcuts import render, redirect
from .models import File
from .forms import FileUploadModelForm


# Show file list
def file_list(request):
    files = File.objects.all().order_by("-id")
    return render(request, 'file_upload/file_list.html', {'files': files})


# Upload File with ModelForm
def model_form_upload(request):
    if request.method == "POST":
        form = FileUploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("File Uploaded Successfully")
            return redirect("/file/")
    else:
        form = FileUploadModelForm()

    return render(request, 'file_upload/index.html')
