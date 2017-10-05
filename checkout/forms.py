from django import forms

class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i,) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i,) for i in range(2015, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
class AddressForm(forms.Form):

    # COUNTRY_CHOICES = ["Ireland", "England"]

    full_name = forms.CharField(label='Full Name')
    phone_number = forms.CharField(label='Phone Number')
    country = forms.CharField(label='Country')
    postcode = forms.CharField(label='Postcode')
    town_or_city = forms.CharField(label='Town or City')
    street_address_1 = forms.CharField(label='Street Address 1')
    street_address_2 = forms.CharField(label='Street Address 2')
    county = forms.CharField(label='County')

