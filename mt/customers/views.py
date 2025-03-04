from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Customer

def customer_list(request):
    """Get a list of all customers."""
    customers = Customer.objects.all()
    return render(request, "customers/list.html", {"customers": customers})

def customer_detail(request, id):
    """Get details of a specific customer."""
    customer = get_object_or_404(Customer, id=id)
    return render(request, "customers/detail.html", {"customer": customer})

@csrf_exempt
def create_customer(request):
    """Create a new customer."""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        customer = Customer.objects.create(name=name, phone=phone)
        return JsonResponse({"message": "Customer created", "customer_id": customer.id}, status=201)
    
    return JsonResponse({"error": "Invalid request"}, status=400)
