from django.contrib import auth, messages
from django.shortcuts import get_object_or_404, redirect


from ..utils import send_activation_email, send_suspension_email

User = auth.get_user_model()

# logic for suspending users and redirection based on user type


def suspend_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = not user.is_active
    user.save()

    if(user.role == 'doctor'):
        send_suspension_email(user, request)
        messages.success(request, "Account Suspended")
        return redirect("dashboard:doctors:doctor_details", pk=pk)
    # elif(user.role == 'staff'):
    #     send_suspension_email(user, request)
    #     messages.success(request, "Account Suspended")
    #     return redirect("dashboard:staff:staff_details", pk=pk)
    # elif(user.role == 'patient'):
    #     send_suspension_email(user, request)
    #     messages.success(request, "Account Suspended")
    #     return redirect("dashboard:patients:patient_details", pk=pk)


# logic for activating users and redirection
def activate_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = True
    user.save()

    if(user.role == 'doctor'):
        send_activation_email(user, request)
        messages.success(request, "Account activated")
        return redirect("dashboard:doctors:doctor_details", pk=pk)
    # elif(user.role == 'staff'):
    #     send_activation_email(user, request)
    #     messages.success(request, "Account activated")
    #     return redirect("dashboard:staff:staff_details", pk=pk)
    # elif(user.role == 'staff'):
    #     send_activation_email(user, request)
    #     messages.success(request, "Account activated")
    #     return redirect("dashboard:patients:patient_details", pk=pk)