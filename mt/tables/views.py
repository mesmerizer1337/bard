from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Table

def table_list(request):
    """Get a list of all tables."""
    tables = Table.objects.all()
    return render(request, "tables/list.html", {"tables": tables})

@csrf_exempt
def create_table(request):
    """Create a new table."""
    if request.method == "POST":
        number = request.POST.get("number")
        seats = request.POST.get("seats")
        table = Table.objects.create(number=number, seats=seats, is_available=True)
        return JsonResponse({"message": "Table created", "table_id": table.id}, status=201)
    
    return JsonResponse({"error": "Invalid request"}, status=400)

def available_tables(request):
    """Get a list of available tables."""
    tables = Table.objects.filter(is_available=True)
    return render(request, "tables/available.html", {"tables": tables})
