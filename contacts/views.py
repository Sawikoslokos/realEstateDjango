from django.shortcuts import render

# Create your views here.
def contact(request):
    if request.method == 'POST':
        print('HELLO')
        listing_id = request.POST['listing_id']
        