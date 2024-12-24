from django.db import models
from core.abstract.models import AbstractModel, AbstractManager


# Create your models here.
class PostManager(AbstractManager):
    def get_object_by_public_id(self, public_id):
        try:
            return self.get(public_id=public_id)
        except self.model.DoesNotExist:
            raise ValueError(f"Post with public_id '{public_id}' does not exist.")
    pass

class Post(AbstractModel):
    author = models.ForeignKey(to='core_user.User', on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=True)
    
    objects = PostManager()
    
    def __str__(self):
        return f"{self.author.name}"
    
    class Meta:
        db_table = "core.post"
        
        