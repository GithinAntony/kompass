from django.db import models

# Create your models here.
class Place(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    userid = models.IntegerField(null=False)
    name = models.CharField(max_length=100, null=True)
    overview = models.TextField(null=True)
    type = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    amenities = models.ForeignKey("Amenity",on_delete=models.SET_NULL,null=True)
    besttime = models.CharField(max_length=150, null=True)
    howtoreach = models.CharField(max_length=250, null=True)
    nativelang = models.CharField(max_length=100, null=True)
    place = models.ForeignKey("Locality",on_delete=models.SET_NULL,null=True)
    latitude = models.CharField(max_length=50, null=True)
    longitude = models.CharField(max_length=50, null=True)
    mainphoto = models.CharField(max_length=65, null=True)
    status_choices = [
        ('pending', 'Pending'),
        ('active', 'Active'),
    ]
    status = models.CharField(max_length=15, choices=status_choices, default="pending")
    booking_choices = [
        ('none', 'None'),
        ('day', 'Day'),
        ('seat', 'Seat'),
        ('ticket', 'Ticket'),
    ]
    bookingtype = models.CharField(max_length=15, choices=booking_choices, default="none")
    booking_price = models.FloatField(null=True)

    def __str__(self):
        return self.name

class User(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100,default='', null=False)
    email = models.CharField(max_length=255,default='', null=False)
    username = models.CharField(max_length=100,default='', null=False)
    password = models.CharField(max_length=500,default='', null=False)
    phone = models.CharField(max_length=15,default='', null=False)
    address = models.TextField(default='',null=False)
    place = models.CharField(max_length=255,default='', null=True)
    status_choices = [
        ('active', 'Active'),
        ('suspend', 'Suspend'),
    ]
    status = models.CharField(max_length=7, choices=status_choices, default="Active")
    usertype_choices = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('owner','Owner'),
    ]
    usertype = models.CharField(max_length=7, choices=usertype_choices, default="user")

    def __str__(self):
        return self.name

class Locality(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Amenity(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class User_gallery(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    place = models.ForeignKey("Place",on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey("User",on_delete=models.SET_NULL,null=True)
    image = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.place

class Report(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    place = models.ForeignKey("Place",on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey("User",on_delete=models.SET_NULL,null=True)
    message = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.id

class Review(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    place = models.ForeignKey("Place",on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey("User",on_delete=models.SET_NULL,null=True)
    rating = models.IntegerField(null=False)
    review = models.TextField(null=True)

    def __str__(self):
        return self.review

class Contact_message(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=255, null=True)
    message = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

class Orders(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    place = models.ForeignKey(Place,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    booking_type = models.CharField(max_length=100, null=True)
    booking_title = models.CharField(max_length=100, null=True)
    booking_date_text = models.CharField(max_length=100, null=True)
    booking_no_of_rooms = models.CharField(max_length=100, null=True)
    booking_count = models.CharField(max_length=100, null=True)
    booking_price = models.CharField(max_length=100, null=True)
    total_price = models.CharField(max_length=100, null=True)
    cardholder_name = models.CharField(max_length=100, null=True)
    cardnumber = models.CharField(max_length=100, null=True)
    expdate = models.CharField(max_length=100, null=True)
    expyear = models.CharField(max_length=100, null=True)
    cvv = models.CharField(max_length=100, null=True)
    date_added = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.booking_title

