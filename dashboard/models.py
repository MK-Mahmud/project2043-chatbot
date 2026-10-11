from django.db import models


class AuditLog(models.Model):
    """
    Records administrator actions (e.g. knowledge base edits) for
    accountability purposes.

    NOTE: this model is registered in the Django admin but nothing in
    the application currently writes to it. It is kept as scaffolding
    for a future audit-logging feature rather than removed, since the
    schema and admin registration are already in place.
    """

    admin_name = models.CharField(max_length=100)
    action = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.admin_name