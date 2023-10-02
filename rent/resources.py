from import_export import resources

from .models import RentalPerson, RentPayment, House


class RentalPersonResource(resources.ModelResource):
    class Meta:
        model = RentalPerson


class RentPaymentResource(resources.ModelResource):
    class Meta:
        model = RentPayment


class HouseResource(resources.ModelResource):
    class Meta:
        model = House