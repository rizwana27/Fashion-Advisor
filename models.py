from django.db import models



#custom model added by pavanY



import uuid
#primary key assignment

class EnteredText(models.Model):
    custom_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

