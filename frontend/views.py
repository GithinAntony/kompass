from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    localitys = Locality.objects.all()
    context = {'localitys': localitys}
    if request.method == 'POST':
       return redirect('/search-category/'+str(request.POST['search_places']))
    return render(request, 'home.html', context)


def site_admin_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            if User.objects.filter(username=data_record['username'],password=data_record['password'],usertype='admin'):
                user_details = User.objects.get(username=data_record['username'],password=data_record['password'],usertype='admin')
                request.session['is_logged_in'] = True
                request.session['email'] = user_details.email
                request.session['full_name'] = user_details.name
                request.session['user_id'] = user_details.id
                request.session['username'] = user_details.username
                request.session['usertype'] = user_details.usertype
                return redirect('/admin-dashboard')
            else:
                messages.error(request, 'Invalid Credentials!')
                return redirect('/admin-login')
    context = {'form': form}
    return render(request, 'admin-login.html', context)

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            if User.objects.filter(username=data_record['username'],password=data_record['password'],usertype='user'):
                user_details = User.objects.get(username=data_record['username'],password=data_record['password'],usertype='user')
                if user_details.status == 'active':
                        request.session['is_logged_in'] = True
                        request.session['email'] = user_details.email
                        request.session['full_name'] = user_details.name
                        request.session['user_id'] = user_details.id
                        request.session['username'] = user_details.username
                        request.session['usertype'] = user_details.usertype
                        return redirect('/user-dashboard')
                else:
                        messages.error(request, 'User is suspended. Contact the admin!')
                        return redirect('/login')
            else:
                messages.error(request, 'Invalid Credentials!')
                return redirect('/login')
    context = {'form': form}
    return render(request, 'login.html', context)


def register(request):
    form = RegisterForm()
    localitys = Locality.objects.all()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            user = User(
            name=data_record['name'],
            email=data_record['email'],
            username=data_record['username'],
            password=data_record['password'],
            phone=data_record['phone'],
            address=data_record['address'],
            place=data_record['place'],
            status='pending',
            usertype='user',
            )
            user.save()
            messages.success(request, 'User registered successfully!')
            return redirect('/login')
    context = {'localitys': localitys, 'form': form}
    return render(request, 'register.html', context)

def owner_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            if User.objects.filter(username=data_record['username'], password=data_record['password'],usertype='owner'):
                user_details = User.objects.get(username=data_record['username'], password=data_record['password'],usertype='owner')

                if user_details.status == 'active':
                        request.session['is_logged_in'] = True
                        request.session['email'] = user_details.email
                        request.session['full_name'] = user_details.name
                        request.session['user_id'] = user_details.id
                        request.session['username'] = user_details.username
                        request.session['usertype'] = user_details.usertype
                        return redirect('/user-dashboard')
                else:
                        messages.error(request, 'Owner is suspended. Contact the admin!')
                        return redirect('/owner-login')
            else:
                messages.error(request, 'Invalid Credentials!')
                return redirect('/owner-login')
    context = {'form': form}
    return render(request, 'owner-login.html', context)


def owner_register(request):
    form = OwnerRegisterForm()
    localitys = Locality.objects.all()
    if request.method == 'POST':
        form = OwnerRegisterForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            user = User(
            name=data_record['name'],
            email=data_record['email'],
            username=data_record['username'],
            password=data_record['password'],
            phone=data_record['phone'],
            address=data_record['address'],
            place=data_record['place'],
            status='pending',
            usertype='owner',
            )
            user.save()
            messages.success(request, 'Owner registered successfully!')
            return redirect('/owner-login')
    context = {'localitys': localitys, 'form': form}
    return render(request, 'owner-register.html', context)


def user_dashboard(request):
    return render(request, 'user-dashboard.html' )

def owner_dashboard(request):
    return render(request, 'user-dashboard.html' )

#admin processing
def admin_contact_us(request):
    contact_us_messages = Contact_message.objects.filter()
    context = {'contact_us_messages': contact_us_messages}
    return render(request, 'admin-contact-us.html', context)

def admin_dashboard(request):
    return render(request, 'admin-dashboard.html' )

def admin_users(request):
    user_details = User.objects.exclude(usertype='admin').all()
    context = {'user_details': user_details }
    return render(request, 'admin-users.html', context )

def admin_users_delete(request, user_id):
    User.objects.filter(id=user_id).delete()
    messages.error(request, 'User deleted!')
    return redirect('/admin-users')

def admin_users_status(request, user_id, slug):
    user = User.objects.get(id=user_id)
    user.status = slug
    user.save()
    messages.error(request, 'User status updated!')
    return redirect('/admin-users')

def admin_locality(request):
    form = LocalityForm()
    locality = Locality.objects.all()
    if request.method == 'POST':
        form = LocalityForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            locality = Locality(
            name=data_record['name']
            )
            locality.save()
            messages.success(request, 'Locality added successfully!')
            return redirect('/admin-locality')
    context = {'locality': locality, 'form':form  }
    return render(request, 'admin-locality.html', context )

def admin_locality_delete(request, id):
    Locality.objects.filter(id=id).delete()
    messages.error(request, 'Locality deleted!')
    return redirect('/admin-locality')

def admin_amenity(request):
    form = AmenityForm()
    amenity = Amenity.objects.all()
    if request.method == 'POST':
        form = AmenityForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            amenity = Amenity(
            name=data_record['name']
            )
            amenity.save()
            messages.success(request, 'Amenity added successfully!')
            return redirect('/admin-amenity')
    context = {'amenity': amenity, 'form':form  }
    return render(request, 'admin-amenity.html', context )

def admin_amenity_delete(request, id):
    Amenity.objects.filter(id=id).delete()
    messages.error(request, 'Amenity deleted!')
    return redirect('/admin-amenity')

def admin_places(request):
    place = Place.objects.all()
    context = {'places': place }
    return render(request, 'admin-places.html', context )

def admin_places_delete(request, id):
    Place.objects.filter(id=id).delete()
    messages.error(request, 'Place deleted!')
    return redirect('/admin-places')

def admin_places_status(request, id, slug):
    place = Place.objects.get(id=id)
    place.status = slug
    place.save()
    messages.error(request, 'Place updated!')
    return redirect('/admin-places')

def addnewplace(request):
    place = Place.objects.all()
    amenity = Amenity.objects.all()
    form = AddNewPlaceForm()
    if request.method == 'POST':
        form = AddNewPlaceForm(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['main_photo']
            fs = FileSystemStorage()
            file_name = fs.save(uploaded_file.name, uploaded_file)
            place = Place(
                userid=request.session['user_id'],
                name=request.POST['name'],
                overview=request.POST['overview'],
                mainphoto = fs.url(file_name),
                type=request.POST['type'],
                place=Locality.objects.get(id=request.POST['place']),
                amenities=Amenity.objects.get(id=request.POST['amenities']),
                description=request.POST['description'],
                besttime=request.POST['besttime'],
                howtoreach=request.POST['howtoreach'],
                nativelang=request.POST['nativelanguage'],
                latitude=request.POST['latitude'],
                longitude=request.POST['longitude'],
                status = 'pending',
                bookingtype = request.POST['bookingtype'],
                booking_price = request.POST['bookingprice']
            )
            place.save()
            messages.success(request, 'Establishments sent for approval! Once approved establishments will be published online.')
            return redirect('/addnewplace')
    context = {'place': place, 'amenity': amenity, 'form': form}
    return render(request, 'addnewplace.html', context)

def admin_contactus(request):
    context = { 'contactus' : Contact_message.objects.filter() }
    return render(request, 'admin-contactus.html', context )

def user_gallery(request, place_id):
    user_gallery = User_gallery.objects.filter(place=Place.objects.get(id=place_id),user=User.objects.get(id=request.session['user_id']))
    form = UserGallery()
    if request.method == 'POST':
        form = UserGallery(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['main_photo']
            fs = FileSystemStorage()
            file_name = fs.save(uploaded_file.name, uploaded_file)
            user_gallery = User_gallery(
                user=User.objects.get(id=request.session['user_id']),
                place=Place.objects.get(id=place_id),
                image=fs.url(file_name),
            )
            user_gallery.save()
            messages.success(request, 'Image added successfully')
            return redirect('/user-gallery/'+str(place_id))
    context = {'user_gallery': user_gallery, 'form':form }
    return render(request, 'user-gallery.html', context)

def user_gallery_delete(request,place_id,id):
    User_gallery.objects.filter(id=id).delete()
    messages.error(request, 'Image deleted!')
    return redirect('/user-gallery/'+str(place_id))

def myprofile(request):
    localitys = Locality.objects.all()
    user=User.objects.get(id=request.session['user_id'])
    form = MyProfileForm(initial={'user': user})
    context = {'localitys': localitys, 'form': form}
    return render(request, 'myprofile.html', context)

def myplaces(request):
    place = Place.objects.all()
    context = {'places': place}
    return render(request, 'myplaces.html', context)

def pendingplaces(request):
    place = Place.objects.filter(userid=request.session['user_id'], status='pending')
    context = {'places': place}
    return render(request, 'pendingplaces.html', context)

def search_category(request,id):
    try:
        place = Place.objects.filter(place=Locality.objects.get(id=id))
    except Place.DoesNotExist:
        place = 'none'
    category = [
        'Clubs',
        'Resorts',
        'Restaurant',
        'Bar',
        'Hotels',
        'Nightclub',
        'Monuments',
        'Homestay',
        'Tourism',
        'Theatre',
        'Other',
    ]
    locality = Locality.objects.get(id=id)
    context = {'place': place,'category':category,'locality':locality,'place_id':id}
    return render(request, 'search-category.html', context)

def search_places(request,id,str_type):
    try:
        place = Place.objects.get(place=Locality.objects.get(id=id),type=str(str_type))
    except Place.DoesNotExist:
        place = 'none'
    locality = Locality.objects.get(id=id)
    context = {'place': place,'str_type':str_type,'locality':locality}
    return render(request, 'search-places.html', context)

def place_details(request,id):
    form = UserPlacesRating()
    if request.method == 'POST':
        form = UserPlacesRating(request.POST)
        if form.is_valid():
            review = Review(
                user=User.objects.get(id=request.session['user_id']),
                place=Place.objects.get(id=id),
                rating=request.POST['rating'],
                review=request.POST['review'],
            )
            review.save()
            messages.success(request,'Review added')
            return redirect('/place-details/'+str(id))
    try:
        place = Place.objects.filter(id=id)
        user_gallery = User_gallery.objects.filter(place=Place.objects.get(id=id))
        review = Review.objects.filter(place=Place.objects.get(id=id))
    except Place.DoesNotExist:
        place = 'none'
        user_gallery ='none'
        review='none'
    context = {'form':form,'place': place,'user_gallery':user_gallery,'review':review}
    return render(request, 'places-details.html', context)

def user_place_report(request, place_id):
    place = Place.objects.filter(id=place_id)
    form = UserPlacesReport()
    if request.method == 'POST':
        form = UserPlacesReport(request.POST)
        if form.is_valid():
            report = Report(
                user=User.objects.get(id=request.session['user_id']),
                place=Place.objects.get(id=place_id),
                message=request.POST['message'],
            )
            report.save()
            messages.success(request,'Report Filed successfully')
            return redirect('/place-details/'+str(place_id))
    context = {'place': place,'form':form}
    return render(request, 'places-report.html', context)

def places_delete(request, id):
    Place.objects.filter(id=id).delete()
    messages.error(request, 'Place deleted!')
    return redirect('/myplaces')

def logout(request):
    del request.session['is_logged_in']
    del request.session['username']
    return redirect('/login')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            contact = Contact_message(
            name=data_record['name'],
            email=data_record['email'],
            message=data_record['message'],
            )
            contact.save()
            messages.success(request, 'Message registered successfully!')
            return redirect('/contact')
    context = {'form': form}
    return render(request, 'contact.html', context)

def about(request):
    return render(request, 'about.html')

def user_place_booking_day(request, place_id):
    form = PlaceBookingDayForm()
    place = Place.objects.get(id=place_id)
    if request.method == 'POST':
        form = PlaceBookingDayForm(request.POST)
        if form.is_valid():
           data_record = form.cleaned_data
           request.session['booking_type'] = 'day'
           request.session['day_booking_place_id'] = place_id
           request.session['day_date_text'] = data_record['date']
           request.session['day_no_of_rooms'] = data_record['no_of_rooms']
           request.session['day_no_of_days_hidden'] = data_record['no_of_days_hidden']
           return redirect('/user-booking-payment/'+str(place_id))
    context = {'form': form, 'place':place}
    return render(request, 'places-booking-day.html', context)

def user_place_booking_seat(request, place_id):
    form = PlaceBookingSeatForm()
    place = Place.objects.get(id=place_id)
    if request.method == 'POST':
        form = PlaceBookingSeatForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            request.session['booking_type'] = 'seat'
            request.session['seat_booking_place_id'] = place.id
            request.session['seat_booking_count'] = data_record['no_of_seat']
            return redirect('/user-booking-payment/'+str(place_id))
    context = {'form': form, 'place':place}
    return render(request, 'places-booking-seat.html', context)

def user_place_booking_ticket(request, place_id):
    form = PlaceBookingTicketForm()
    place = Place.objects.get(id=place_id)
    if request.method == 'POST':
        form = PlaceBookingTicketForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            request.session['booking_type'] = 'ticket'
            request.session['ticket_booking_place_id'] = place.id
            request.session['ticket_booking_count'] = data_record['no_of_tickets']
            return redirect('/user-booking-payment/'+str(place_id))
    context = {'form': form, 'place':place}
    return render(request, 'places-booking-ticket.html', context)

def user_booking_payment(request,place_id):
    form = UserBookingPayment()
    place = Place.objects.get(id=place_id)
    total_amount_pay = 0;
    if request.session['booking_type']=='day':
        total_amount_pay =  int(request.session['day_no_of_rooms']) * int(request.session['day_no_of_days_hidden']) * place.booking_price;
    elif request.session['booking_type']=='seat':
        total_amount_pay = int(request.session['seat_booking_count']) * place.booking_price;
    elif request.session['booking_type']=='ticket':
        total_amount_pay = int(request.session['ticket_booking_count']) * place.booking_price;
    else:
        return redirect('/user-booking-payment/')
    if request.method == 'POST':
        form = UserBookingPayment(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            if request.session['booking_type'] == 'day':
              orders = Orders(
                user=User.objects.get(id=request.session['user_id']),
                place=Place.objects.get(id=place_id),
                booking_type = request.session['booking_type'],
                booking_title=place.name,
                booking_date_text = request.session['day_date_text'],
                booking_no_of_rooms = request.session['day_no_of_rooms'],
                booking_count = request.session['day_no_of_days_hidden'],
                booking_price = place.booking_price,
                total_price = total_amount_pay,
                cardholder_name = data_record['name'],
                cardnumber = data_record['card'],
                expdate = data_record['expdate'],
                expyear = data_record['expyear'],
                cvv = data_record['cvv'],
                date_added = 'null'
              )
              orders.save()
            elif request.session['booking_type'] == 'seat':
                orders = Orders(
                user=User.objects.get(id=request.session['user_id']),
                place=Place.objects.get(id=place_id),
                booking_type = request.session['booking_type'],
                booking_title=place.name,
                booking_date_text = 'null',
                booking_no_of_rooms = 'null',
                booking_count = request.session['seat_booking_count'],
                booking_price = place.booking_price,
                total_price = total_amount_pay,
                cardholder_name = data_record['name'],
                cardnumber = data_record['card'],
                expdate = data_record['expdate'],
                expyear = data_record['expyear'],
                cvv = data_record['cvv'],
                date_added = 'null'
                )
                orders.save()
            elif request.session['booking_type'] == 'ticket':
                orders = Orders(
                user=User.objects.get(id=request.session['user_id']),
                place=Place.objects.get(id=place_id),
                booking_type = request.session['booking_type'],
                booking_title=place.name,
                booking_date_text = 'null',
                booking_no_of_rooms = 'null',
                booking_count = request.session['ticket_booking_count'],
                booking_price = place.booking_price,
                total_price = total_amount_pay,
                cardholder_name = data_record['name'],
                cardnumber = data_record['card'],
                expdate = data_record['expdate'],
                expyear = data_record['expyear'],
                cvv = data_record['cvv'],
                date_added = 'null'
                )
                orders.save()
            else:
               return redirect('/user-booking-payment/'+str(place_id))

            if request.session['booking_type'] == 'day':
               del request.session['day_booking_place_id']
               del request.session['day_date_text']
               del request.session['day_no_of_rooms']
               del request.session['day_no_of_days_hidden']
            elif request.session['booking_type'] == 'seat':
                del request.session['seat_booking_place_id']
                del request.session['seat_booking_count']
            elif request.session['booking_type'] == 'ticket':
                del request.session['ticket_booking_place_id']
                del request.session['ticket_booking_count']
            del request.session['booking_type']
            messages.success(request, 'Payment made successfully!')
            return redirect('/user-booking-orders')
    context = {'form': form, 'place':place, 'total_amount_pay':total_amount_pay }
    return render(request, 'user-booking-payment.html', context)

def user_booking_payment_success(request,place_id):
    place = Place.objects.get(id=place_id)
    context = { 'place':place }
    return render(request, 'user-booking-payment-success.html', context)

def user_booking_orders(request):
    orders = Orders.objects.filter(user=User.objects.get(id=request.session['user_id']))
    context = {'orders': orders}
    return render(request, 'user-booking-orders.html', context)

def place_booking_orders(request,place_id):
    orders = Orders.objects.filter(place=Place.objects.get(id=place_id))
    context = {'orders': orders}
    return render(request, 'place-booking-orders.html', context)

def forgot_password(request, usertype):
    form = ForgotPassword()
    if request.method == 'POST':
        form = ForgotPassword(request.POST)
        if form.is_valid():
           data_record = form.cleaned_data
           if usertype == 'user':
             email_details = User.objects.filter(email=data_record['email'],usertype='user')
           else:
            email_details = User.objects.filter(email=data_record['email'],usertype='owner')

           if email_details:
             messages.success(request, 'Instructions are sent to your email!')
           else:
             messages.success(request, 'No accounts associated with this email!')
           return redirect('/forgot-password/' + str(usertype))
    context = {'usertype': usertype, 'form':form}
    return render(request, 'forgot-password.html', context)

def user_change_password(request):
    form = UserChangePasswordForm()
    if request.method == 'POST':
        form = UserChangePasswordForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            userdata = User.objects.get(id=request.session['user_id'],usertype='user')
            if data_record['oldpassword'] == userdata.password:
                record = User.objects.get(id=request.session['user_id'],usertype='user')
                record.password = data_record['password']
                record.save()
                messages.success(request, 'Password updated successfully!')
            else:
                messages.success(request, 'Please enter your correct password!')
            return redirect('/user-change-password')
    context = {'form': form}
    return render(request, 'user-change-password.html', context)

def owner_change_password(request):
    form = ShopChangePasswordForm()
    if request.method == 'POST':
        form = ShopChangePasswordForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            userdata = User.objects.get(id=request.session['user_id'],usertype='owner')
            if data_record['oldpassword'] == userdata.password:
                record = User.objects.get(id=request.session['user_id'],usertype='owner')
                record.password = data_record['password']
                record.save()
                messages.success(request, 'Password updated successfully!')
            else:
                messages.success(request, 'Please enter your correct password!')
            return redirect('/owner-change-password')
    context = {'form': form}
    return render(request, 'owner-change-password.html', context)

def user_edit_profile(request):
    form = UserEditProfile()
    userdata = User.objects.get(id=request.session['user_id'],usertype='user')
    form = UserEditProfile(initial={'name': userdata.name, 'email': userdata.email, 'username': userdata.username, 'phone': userdata.phone, 'address': userdata.address, 'place':userdata.place })
    if request.method == 'POST':
        form = UserEditProfile(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            flag = 0
            mess = ''
            if userdata.email != data_record['email']:
                t = User.objects.filter(email=data_record['email'],usertype='user').exclude(email=userdata.email)
                if t:
                    flag = 1
                    mess = 'Email already exists'
            elif userdata.username != data_record['username']:
                t = User.objects.filter(username=data_record['username'],usertype='user').exclude(username=userdata.username)
                if t:
                    flag = 1
                    mess = 'Username already exists'
            if flag == 0:
                record = User.objects.get(id=request.session['user_id'])
                record.name = data_record['name']
                record.email = data_record['email']
                record.username = data_record['username']
                record.phone = data_record['phone']
                record.address = data_record['address']
                record.place = data_record['place']
                record.save()
                messages.success(request, 'User Profile updated successfully!')
                return redirect('/user-edit-profile')
            else:
                messages.success(request, mess)
    context = {'form': form}
    return render(request, 'user-edit-profile.html',context)

def owner_edit_profile(request):
    form = ShopEditProfile()
    userdata = User.objects.get(id=request.session['user_id'],usertype='owner')
    form = ShopEditProfile(initial={'name': userdata.name, 'email': userdata.email, 'username': userdata.username, 'phone': userdata.phone, 'address': userdata.address, 'place':userdata.place})
    if request.method == 'POST':
        form = ShopEditProfile(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            flag = 0
            mess = ''
            if userdata.email != data_record['email']:
                t = User.objects.filter(email=data_record['email'],usertype='owner').exclude(email=userdata.email)
                if t:
                    flag = 1
                    mess = 'Email already exists'
            elif userdata.username != data_record['username']:
                t = User.objects.filter(username=data_record['username'],usertype='owner').exclude(username=userdata.username)
                if t:
                    flag = 1
                    mess = 'Username already exists'
            if flag == 0:
                record = User.objects.get(id=request.session['user_id'])
                record.name = data_record['name']
                record.email = data_record['email']
                record.username = data_record['username']
                record.phone = data_record['phone']
                record.address = data_record['address']
                record.place = data_record['place']
                record.save()
                messages.success(request, 'Owner Profile updated successfully!')
                return redirect('/owner-edit-profile')
            else:
                messages.success(request, mess)
    context = {'form': form}
    return render(request, 'owner-edit-profile.html',context)
