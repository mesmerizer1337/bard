from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
from .models import Reservation
from customers.models import Customer
from tables.models import Table
from forums.models import ForumThread, ForumPost  # Import forum models

def reservation_list(request):
    """Retrieve a list of all reservations."""
    reservations = Reservation.objects.select_related('customer', 'table').all()
    return render(request, "reservations/list.html", {"reservations": reservations})

def reservation_detail(request, id):
    """Retrieve details of a specific reservation, including the discussion forum."""
    reservation = get_object_or_404(Reservation, id=id)
    forum_thread, created = ForumThread.objects.get_or_create(title=f"Discussion for Reservation {reservation.id}")
    forum_posts = forum_thread.posts.all() if forum_thread else []
    
    return render(
        request, 
        "reservations/detail.html", 
        {"reservation": reservation, "forum_thread": forum_thread, "forum_posts": forum_posts}
    )

def user_reservations(request, user_id):
    """Retrieve all reservations for a specific user."""
    customer = get_object_or_404(Customer, id=user_id)
    reservations = Reservation.objects.filter(customer=customer).select_related('table')
    return render(request, "reservations/user_reservations.html", {"reservations": reservations})

@csrf_exempt
def create_reservation(request):
    """Create a new reservation and an associated forum thread."""
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        table_id = request.POST.get("table_id")
        date_str = request.POST.get("date")
        status = request.POST.get("status", "pending")

        if not (user_id and table_id and date_str):
            return JsonResponse({"error": "Missing required fields"}, status=400)

        customer = get_object_or_404(Customer, id=user_id)
        table = get_object_or_404(Table, id=table_id)
        date = parse_date(date_str)

        if not date:
            return JsonResponse({"error": "Invalid date format"}, status=400)

        if Reservation.objects.filter(customer=customer, date=date).exists():
            return JsonResponse({"error": "User already has a reservation on this date"}, status=400)

        if Reservation.objects.filter(table=table, date=date).exists():
            return JsonResponse({"error": "Table is already reserved on this date"}, status=400)

        reservation = Reservation.objects.create(customer=customer, table=table, date=date, status=status)

        # Create a forum thread for discussion
        forum_thread = ForumThread.objects.create(title=f"Discussion for Reservation {reservation.id}")

        return JsonResponse({
            "message": "Reservation created successfully",
            "reservation_id": reservation.id,
            "forum_thread_id": forum_thread.id
        }, status=201)

    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def update_reservation(request, id):
    """Update the status of a reservation."""
    reservation = get_object_or_404(Reservation, id=id)
    
    if request.method == "POST":
        new_status = request.POST.get("status")
        valid_statuses = ["pending", "confirmed", "canceled"]

        if new_status not in valid_statuses:
            return JsonResponse({"error": "Invalid status"}, status=400)

        reservation.status = new_status
        reservation.save()
        return JsonResponse({"message": "Reservation updated successfully", "new_status": reservation.status})

    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def delete_reservation(request, id):
    """Delete a reservation and its associated forum thread."""
    reservation = get_object_or_404(Reservation, id=id)

    # Delete the associated forum thread if it exists
    forum_thread = ForumThread.objects.filter(title=f"Discussion for Reservation {reservation.id}").first()
    if forum_thread:
        forum_thread.delete()

    reservation.delete()
    return JsonResponse({"message": "Reservation and associated forum thread deleted successfully"}, status=200)
