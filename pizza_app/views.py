from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzasForm
from django.forms import formset_factory 
from .models import Pizza

# Create your views here.
def home(request):

    return render(request, "pizza/home.html")

def order(request):

    multiple_form = MultiplePizzasForm()
    if request.method == "POST":
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            note = "Thanks for Ordering!  Your %s %s and %s Pizza is on its way....."%(filled_form.cleaned_data['size'],
                   filled_form.cleaned_data['topping1'],
                   filled_form.cleaned_data['topping2'],)   
            filled_form = PizzaForm()
            context = {
                'created_pizza_pk': created_pizza_pk,
                'pizzaform': filled_form,
                'note': note,
                'multiple_form': multiple_form,
            }
        else:
            created_pizza_pk = None
            note = "Pizza order has failed - please try again"
            # newform = PizzaForm()
        context = {
            'created_pizza_pk': created_pizza_pk,
            'pizzaform': filled_form,
            'note': note,
            'multiple_form': multiple_form,
        }
        return render(request, "pizza/order.html", context)
              
    else:
        context = {
            'pizzaform': PizzaForm,
            'multiple_form': multiple_form,
        }
        return render(request, "pizza/order.html", context)

def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzasForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']

    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == "POST":
        filled_formset = PizzaFormSet(request.POST)
        if (filled_formset.is_valid()):
            for form in filled_formset:
                # print(form.cleaned_data['topping1'])
                print(form.cleaned_data['topping1'])
            note = 'Pizzas have been ordered'
        else:
            note = 'Order was not created, please try again!!!'

        context = {
            'note': note, 
            'formset': formset,
        }

        return render(request, 'pizza/pizzas.html', context )

    else:

        context = {
            'formset': formset,
        }

        return render(request, 'pizza/pizzas.html',context,)

def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = "Order has been updated"

            context = {
                'pizzaform': form,
                'pizza': pizza,
                'note': note,
            }

            return render(request, 'pizza/edit_order.html',context,)

    context = {
    'pizzaform': form,
    'pizza': pizza,
    }
    
    return render(request, 'pizza/edit_order.html',context,)