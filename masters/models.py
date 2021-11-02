from django.db import models

# Create your models here.
class core(models.Model):
    co_id = models.TextField(max_length=32);
    co_name = models.TextField()
    co_auther = models.TextField()
    co_created_on = models.TextField()

    def __str__(self) -> str:
            return self.co_id

    def show_all(self):
        json = {
            "co_id" : self.co_id,
            "co_name" : self.co_name,
            "co_auther" : self.co_auther,
            "co_created_on" : self.co_created_on,
        }
        
        return json