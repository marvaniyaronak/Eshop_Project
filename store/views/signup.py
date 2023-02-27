from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django. views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        customer = Customer(first_name=first_name, last_name=last_name,
                            phone=phone, email=email, password=password)
    # validation for signupform

        error_message = None
        error_message = self.validateCustomer(customer)
        if not error_message:
            # validation for signupform

            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            return render(request, 'signup.html', {'error': error_message})

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "Frist Name  Required !! "
        elif len(customer.first_name) < 3:
            error_message = 'Frist Name Must Be 3 char '
        elif not customer.last_name:
            error_message = "Last Name  Required !! "
        elif len(customer.last_name) < 5:
            error_message = 'Last Name Must Be 5 char '
        elif not customer.phone:
            error_message = "Phon Number Required !! "
        elif len(customer.phone) < 10:
            error_message = 'Phone Number Must Be 10 char '
        elif not customer.password:
            error_message = "Password  Required !! "
        elif len(customer.password) < 5:
            error_message = 'Password Must Be 5 char '

        elif customer.isExists():
            error_message = 'Email Address Already Registered'

        return error_message
