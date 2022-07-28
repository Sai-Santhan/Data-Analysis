import csv

from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.utils.dateparse import parse_date
from django.views.generic import ListView, DetailView, TemplateView
from xhtml2pdf import pisa

from customers.models import Customer
from products.models import Product
from profiles.models import Profile
from reports.utils import get_report_image
from sales.models import CSV, Position, Sale
from .models import Report
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = "reports/main.html"


class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    template_name = "reports/detail.html"


class UploadTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'reports/from_file.html'


@login_required()
def csv_upload_view(request):
    if request.method == "POST":
        csv_file_name = request.FILES.get('file').name
        csv_file = request.FILES.get('file')
        obj, created = CSV.objects.get_or_create(file_name=csv_file_name)

        if not created:
            return JsonResponse({"ex": True})

        obj.csv_file = csv_file
        obj.save()
        with open(obj.csv_file.path, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                transaction_id = row[1]
                product = row[2]
                quantity = int(row[3])
                customer = row[4]
                date = parse_date(row[5])

                try:
                    product_obj = Product.objects.get(name__iexact=product)
                except Product.DoesNotExist:
                    product_obj = None

                if product_obj is not None:
                    customer_obj, _ = Customer.objects.get_or_create(
                        name=customer)
                    salesman_obj = Profile.objects.get(user=request.user)
                    position_obj = Position.objects.create(product=product_obj,
                                                           quantity=quantity,
                                                           created=date)

                    sale_obj, _ = Sale.objects.get_or_create(
                        transaction_id=transaction_id,
                        customer=customer_obj,
                        salesman=salesman_obj,
                        created=date,
                    )
                    sale_obj.positions.add(position_obj)
                    sale_obj.save()
            return JsonResponse({"ex": False})
    return HttpResponse()


@login_required()
def create_report_view(request):
    # The below line got deprecated in Django 3.1
    # if request.is_ajax():
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        name = request.POST.get("name")
        remarks = request.POST.get('remarks')
        image = request.POST.get("image")

        img = get_report_image(image)

        author = Profile.objects.get(user=request.user)
        Report.objects.create(name=name, remarks=remarks, image=img, author=author)
        return JsonResponse({'msg': 'send'})
    return JsonResponse({})


@login_required()
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
