from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.views.generic import ListView, DetailView, TemplateView
from xhtml2pdf import pisa

from profiles.models import Profile
from reports.utils import get_report_image
from .models import Report


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


def csv_upload_view():
    pass


def render_pdf_view(request, pk):
    template_path = "reports/pdf.html"
    obj = get_object_or_404(Report, pk=pk)
    context = {"obj": obj}

    response = HttpResponse(content_type="application/pdf")

    response["Content-Disposition"] = 'filename="report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse(f"We had some errors <pre>{html}</pre>")
    return response
