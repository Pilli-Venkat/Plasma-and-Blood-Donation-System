from django_filters import FilterSet
from . models import Donate
class ReceiveFilter(FilterSet):

    class Meta:
        model = Donate
        fields =['state','choose']
       