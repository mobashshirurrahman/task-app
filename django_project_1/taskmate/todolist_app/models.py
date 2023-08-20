from django.db import models

# Create your models here.
class TaskList(models.Model):

    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    

    # class Meta:
    #     verbose_name = _("TaskList")
    #     verbose_name_plural = _("TaskLists")

    def __str__(self):
        return self.task + "-" +str(self.done)

    # def get_absolute_url(self):
    #     return reverse("TaskList_detail", kwargs={"pk": self.pk})
