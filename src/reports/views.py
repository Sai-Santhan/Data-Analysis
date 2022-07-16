from django.shortcuts import render
from profiles.models import Profile
from django.http import JsonResponse
from .models import Report
from reports.utils import get_report_image
from django.views.generic import ListView, DetailView, TemplateView


class ReportListView(ListView):
    model = Report
    template_name = "reports/main.html"


class ReportDetailView(DetailView):
    model = Report
    template_name = "reports/detail.html"


class UploadTemplateView(TemplateView):
    pass


def create_report_view(request):
    if request.is_ajax():
        name = request.POST.get("name")
        remarks = request.POST.get('remarks')
        image = request.POST.get("image")

        img = get_report_image(image)

        author = Profile.objects.get(user=request.user)
        Report.objects.create(name=name, remarks=remarks, image=img, author=author)
        return JsonResponse({'msg': 'send'})
    return JsonResponse({})


def render_pdf_view():
    pass


def csv_upload_view():
    pass
