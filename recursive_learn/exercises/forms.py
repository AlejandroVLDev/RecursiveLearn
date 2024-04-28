from django import forms


class powerForm(forms.Form):
    base = forms.Field(widget=forms.NumberInput(attrs={
                       'id': 'first', 'min': '1', 'max': '100', 'step': '1', }), required=False, label='base', label_suffix="=")
    exponent = forms.Field(widget=forms.NumberInput(attrs={
                           'id': 'second', 'min': '0', 'max': '10', 'step': '1', }), required=False, label='exponente', label_suffix="=")


class listForm(forms.Form):
    list = forms.Field(widget=forms.TextInput(
        attrs={'id': 'first'}), required=False, label='a', label_suffix="=")


class sameStringForm(forms.Form):
    string1 = forms.Field(widget=forms.TextInput(
        attrs={'id': 'first'}), required=False, label='a', label_suffix="=")
    string2 = forms.Field(widget=forms.TextInput(
        attrs={'id': 'second'}), required=False, label='b', label_suffix="=")


class decimalBinaryForm(forms.Form):
    number = forms.Field(widget=forms.NumberInput(attrs={
                         'id': 'first', 'min': '0', 'max': '100', 'step': '1', }), required=False, label='numero', label_suffix="=")


class digitInNumberForm(forms.Form):
    number = forms.Field(widget=forms.NumberInput(attrs={
                         'id': 'first', 'min': '0', 'max': '9999999999', 'step': '1', }), required=False, label='numero', label_suffix="=")
    digit = forms.Field(widget=forms.NumberInput(attrs={
                        'id': 'second', 'min': '0', 'max': '9', 'step': '1', }), required=False, label='digito', label_suffix="=")


class palindromeForm(forms.Form):
    palabra = forms.Field(widget=forms.TextInput(
        attrs={'id': 'first'}), required=False, label='palabra', label_suffix="=")


class nAryForm(forms.Form):
    number = forms.Field(widget=forms.NumberInput(attrs={
                         'id': 'first', 'min': '0', 'max': '100', 'step': '1', }), required=False, label='numero', label_suffix="=")
    base = forms.Field(widget=forms.NumberInput(attrs={
                       'id': 'second', 'min': '2', 'max': '9', 'step': '1', }), required=False, label='base', label_suffix="=")


class factorialForm(forms.Form):
    number = forms.Field(widget=forms.NumberInput(attrs={
                         'id': 'first', 'min': '0', 'max': '20', 'step': '1', }), required=False, label='numero', label_suffix="=")
