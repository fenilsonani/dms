from import_export import resources

from .models import Customer, Delivery


class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer


class DeliveryResource(resources.ModelResource):
    class Meta:
        model = Delivery
