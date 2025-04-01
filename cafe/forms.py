from django import forms
from .models import Reservation, Contact, Subscriber

from django import forms
from django.core.exceptions import ValidationError
import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Reservation
import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Reservation
import datetime

import datetime
from django import forms
from django.core.exceptions import ValidationError
from .models import Reservation

import datetime
from django.core.exceptions import ValidationError

from django import forms
from django.core.exceptions import ValidationError
from .models import Reservation
import datetime

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'date', 'time', 'people', 'special_request']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_time(self):
        time = self.cleaned_data.get('time')
        if time:
            hour = time.hour
            minute = time.minute
            
            # Validate business hours
            if hour < 8 or hour >= 22:
                raise ValidationError("We're only open from 8:00 AM to 10:00 PM")
            
            # Validate 30-minute increments
            if minute not in [0, 30]:
                raise ValidationError("Please select time in 30-minute intervals (e.g., 2:00 or 2:30 PM)")
        
        return time

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        
        # Validate for today's date
        if date and time and date == datetime.date.today():
            now = datetime.datetime.now().time()
            if time < now:
                raise ValidationError("You cannot book a time in the past for today")
        
        return cleaned_data
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']