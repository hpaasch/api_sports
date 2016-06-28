from rest_framework import serializers

from app.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    # add data you want to calculate
    age = serializers.SerializerMethodField()  #expects a function get_age

    class Meta:
        model = Player
        fields = ('id', 'name', 'weight', 'position', 'birth_year', 'age')

    def get_age(self, object):  # classes take self as first arg. object is the instance
        return 10  # hard code to test... used DateTime ...
