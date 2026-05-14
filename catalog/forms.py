from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        exclude = ("created_at", "updated_at",)

    def __init__(self, *args, **kwargs):
        super(ProductForm,self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Введите наименование продукта'
        })
        self.fields['description'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Укажите основные характеристики продукта'
        })
        self.fields['image'].widget.attrs.update({
            'class':'form-control'
        })
        self.fields['category'].widget.attrs.update({
            'class':'form-control'
        })
        self.fields['price'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Введите стоимость продукта'
        })

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for word in self.FORBIDDEN_WORDS:
            if word in name.lower() or word in description.lower():
                self.add_error('name', f'Слово {word} - запрещено!')

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price <= 0:
            raise forms.ValidationError("Цена должна быть больше 0.")
        return price
