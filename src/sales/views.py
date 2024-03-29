import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from reports.forms import ReportForm
from sales.forms import SalesSearchForm
from sales.models import Sale
from sales.utils import get_customer_from_id, get_salesman_from_id, get_chart


@login_required()
def home_view(request):
    sales_df = positions_df = merged_df = df = chart = no_data = None

    search_form = SalesSearchForm(request.POST or None)
    report_form = ReportForm()

    if request.method == "POST":
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")
        chart_type = request.POST.get("chart_type")
        results_by = request.POST.get("results_by")

        sale_qs = Sale.objects.filter(
            created__date__gte=date_from, created__date__lte=date_to
        )
        if len(sale_qs) > 0:
            sales_df = pd.DataFrame(sale_qs.values())
            sales_df["customer_id"] = sales_df["customer_id"].apply(get_customer_from_id)
            sales_df["salesman_id"] = sales_df["salesman_id"].apply(get_salesman_from_id)
            sales_df["created"] = sales_df["created"].apply(lambda x: x.strftime("%Y-%m-%d %H:%M"))
            sales_df["updated"] = sales_df["updated"].apply(lambda x: x.strftime("%Y-%m-%d %H:%M"))
            sales_df.rename({
                "customer_id": "customer",
                "salesman_id": "salesman",
                "id": "sales_id",
            },
                axis=1,
                inplace=True
            )
            positions_data = []
            for sale in sale_qs:
                for position in sale.get_positions():
                    obj = {
                        "position_id": position.id,
                        "product": position.product.name,
                        "quantity": position.quantity,
                        "price": position.price,
                        "sales_id": position.get_sales_id(),
                    }
                    positions_data.append(obj)

            positions_df = pd.DataFrame(positions_data)
            merged_df = pd.merge(sales_df, positions_df, on='sales_id')
            df = merged_df.groupby('transaction_id', as_index=False)['price'].agg("sum")

            chart = get_chart(chart_type, sales_df, results_by)

            sales_df = sales_df.to_html(justify='left', index=False,
                                        classes='table table-bordered table-hover table-sm')
            positions_df = positions_df.to_html(justify='left', index=False,
                                                classes='table table-bordered table-hover table-sm')
            merged_df = merged_df.to_html(justify='left', index=False,
                                          classes='table table-bordered table-hover table-sm')
            df = df.to_html(justify='left', index=False,
                            classes='table table-bordered table-hover table-sm')

        else:
            no_data = "No data is available between the provided dates."
    context = {
        'search_form': search_form,
        'report_form': report_form,
        'sales_df': sales_df,
        'positions_df': positions_df,
        'merged_df': merged_df,
        'df': df,
        'chart': chart,
        'no_data': no_data
    }
    return render(request, 'sales/home.html', context)


class SaleListView(LoginRequiredMixin, ListView):
    model = Sale
    template_name = 'sales/main.html'


class SaleDetailView(LoginRequiredMixin, DetailView):
    model = Sale
    template_name = 'sales/detail.html'
