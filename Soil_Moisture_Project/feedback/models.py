from django.db import models

# Create your models here.

FEEDBACK_TYPES = (
    ('Bug', 'Bug'),
    ('Feature Request', 'Feature Request'),
    ('General Feedback', 'General Feedback'),
)


class Feedback(models.Model):
    feedbackType = models.CharField(max_length=100, choices=FEEDBACK_TYPES)
    feedback = models.TextField(blank=True, null=True)
    feedbackDate = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.feedbackType + ' - ' + self.feedback

    def mark_read(self):
        self.is_read = True
        self.save()
