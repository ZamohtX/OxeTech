from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class BaseRepository:
    def __init__(self, model: models.Model):
        self.model = model

    def get_all(self):
        return self.model.objects.all()
    
    def get_by_id(self, pk):
        try:
            return self.model.objects.get(id=pk)
        except ObjectDoesNotExist:
            return None
        
    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)
    
    def update(self, pk, **kwargs):
        obj = self.get_by_id(pk)
        if obj:
            for key, value in kwargs.items():
                setattr(obj, key, value)

            obj.save()
            return obj
        return None
    
    def delete(self, pk):
        obj = self.get_by_id(pk)
        if obj:
            obj.delete()
            return True
        return False
    
    def delete_all(self):
        return self.model.objects.all().delete()
