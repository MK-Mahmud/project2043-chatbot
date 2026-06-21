from django.db import models


class AuditLog(models.Model):
    admin_name = models.CharField(max_length=100)
    action = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.admin_name