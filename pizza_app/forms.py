from django import forms 
from .models import Pizza, Size

# class PizzaForm(forms.Form):
    # widget examples
    # topping1 = forms.CharField(label="Topping 1", max_length=100, required=False, widget=forms.Textarea)
    # topping2 = forms.CharField(label="Topping 2", max_length=100, required=False, widget=forms.PasswordInput)
    # toppings = forms.MultipleChoiceField(choices=[('pop', 'Pepperorin'),
    #                                               ('cheese', 'Cheese'),
    #                                               ('olives', 'Olives'),],widget=forms.CheckboxSelectMultiple)
    # topping1 = forms.CharField(label="Topping 1", max_length=100, required=False)
    # topping2 = forms.CharField(label="Topping 2", max_length=100, required=False)
    # size = forms.ChoiceField(label="Size", choices=[('Small','Small'), ('Medium', 'Medium'), ('Large', 'Large')],)

class PizzaForm(forms.ModelForm):

    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.CheckboxSelectMultiple)
    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)

    # image = forms.ImageField()

    class Meta:
        model = Pizza
        fields = ['topping1','topping2','size']
        labels = {'topping1': 'Topping 1',
                  'topping1': 'Topping 2',
                  'size': 'Pizza Size',}
        # widgets = {'topping1':forms.Textarea}
        # widgets = {'size':forms.CheckboxSelectMultiple}

class MultiplePizzasForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)