from django.db import models

class AdminAuthToken(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'admin_auth_tokens'
