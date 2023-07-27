from rest_framework import serializers
from .models import Project, Unit


class ProjectSerializer(serializers.ModelSerializer):
    # units = UnitSerializer(many=True)
    class Meta:
        model = Project
        fields = ['area', 'projectName', 'projectType', 'developerName', 'landParcel', 'landmark', 'areaIn',
                  'waterSupply', 'floors', 'flatsPerFloors', 'totalUnit', 'availableUnit', 'amenities', 'parking',
                  'longitude', 'latitude', 'transport', 'readyToMove', 'power', 'goods', 'rera',
                  'possession', 'contactPerson', 'contactNumber', 'marketValue', 'lifts', 'brokerage', 'incentive',
                  ]


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['project_id', 'unit', 'CarpetArea', 'price']


class ProjectSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['projectName', 'area', 'rera']


class UnitSerializer1(serializers.ModelSerializer):
    project_name = serializers.SerializerMethodField()
    area = serializers.SerializerMethodField()
    rera = serializers.SerializerMethodField()

    class Meta:
        model = Unit
        fields = ['project_id', 'project_name', 'area', 'rera', 'unit', 'CarpetArea', 'price']

    def get_project_name(self, obj):
        return obj.project_id.projectName

    def get_area(self, obj):
        return obj.project_id.area

    def get_rera(self, obj):
        return obj.project_id.rera
