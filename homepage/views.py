from django.shortcuts import render
from django.views.generic import View, TemplateView
from inventory.models import Stock
from transactions.models import SaleBill, PurchaseBill
from django.db.models import Sum
from transactions.models import SaleItem  # Add this import at the top


class HomeView(View):
    template_name = "home.html"

    def get(self, request):        
        # Fetch sales data for chart
        sales_data = SaleItem.objects.values('stock__name')\
            .annotate(total_sold=Sum('quantity'))\
            .order_by('stock__name')

        # Prepare the labels and data for the sales chart
        sales_labels = [item['stock__name'] for item in sales_data]
        sales_data_values = [item['total_sold'] for item in sales_data]

        # Fetch recent sales and purchases
        sales = SaleBill.objects.order_by('-time')[:3]
        purchases = PurchaseBill.objects.order_by('-time')[:3]

        # Prepare context for the home page
        context = {
            'sales_labels': sales_labels,
            'sales_data': sales_data_values,
            'sales': sales,
            'purchases': purchases
        }

        # Render the home page with sales chart data
        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = "about.html"


