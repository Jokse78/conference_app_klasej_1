from django.contrib.auth.models import User
from django.db import models
from conferences.models import Conference


# Create your models here.
from django.db import models
from conferences.models import Conference

# Create your models here.
class Event( models.Model ):
    date = models.DateTimeField( null = True )
    title = models.CharField( max_length = 100 )
    # TODO:Istrinti ateityje
    visitors = models.IntegerField( default = 0 )

    conference = models.ForeignKey( Conference, on_delete = models.CASCADE )

    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now = True )




class EventRegistration (models.Model):
    event = models.ForeignKey(Event, on_delete = models.CASCADE, )
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
