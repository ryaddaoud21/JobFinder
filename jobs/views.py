from django.shortcuts import render, redirect ,get_object_or_404
from .models import Job ,Application
from .forms import AddJobForm , ApplicationForm
from django.contrib.auth.decorators import login_required



def jobdetails(request,job_id):
    job = Job.objects.get(pk=job_id)
    context = {'job': job}
    return render(request,'jobs/job_details.html', context)


@login_required
def apply_for_job(request,job_id):
    job = Job.objects.get(pk=job_id)
    if request.method=='POST':
        form = ApplicationForm(request.POST,request.FILES )

        if form.is_valid():
            Application = form.save(commit=False)
            Application.job = job
            Application.created_by =request.user
            Application.save()


            return redirect('dashboard')
    else:
        form = ApplicationForm()
    context = {'form': form , 'job':job }
    return  render(request , 'jobs/apply_for_job.html', context )

@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return redirect('dashboard')
    else:
        form = AddJobForm()
    context = {'form': form  }
    return render(request, 'jobs/add_job.html', context)



@login_required
def edit_job (request, job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == 'POST':
        form = AddJobForm(request.POST, instance=job)

        if form.is_valid():
            job = form.save(commit=False)
            job.status = request.POST.get('status')
            job.save()

            return redirect('dashboard')
    else:
        form = AddJobForm(instance=job)

    context = {'form': form ,'job': job}
    return render(request, 'jobs/edit_job.html',context)


def delete_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == 'POST':
        job.delete()
        return redirect('/')
    context= {'job': job}
    return render(request, 'jobs/delete_job.html',context)

