from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'title', 'timestamp', 'datapoints')
<<<<<<< HEAD


=======
>>>>>>> 7f99ef66c1d8e03a64c96c83d3eb364fbdc71e4e
