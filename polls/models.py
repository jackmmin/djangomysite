import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Etc_data(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    etc_text = models.CharField(max_length=200)

    def __str__(self):
        return self.etc_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Feedback_Question(models.Model):
    feedback_q = models.CharField(max_length=200)

    def __str__(self):
        return self.feedback_q

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Feedback_Choice(models.Model):
    feedback_q = models.ForeignKey(Feedback_Question, on_delete=models.CASCADE)
    feedback_c = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.feedback_c

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Fb_Choice_Data(models.Model):
    feedback_c = models.ForeignKey(Feedback_Choice, on_delete=models.CASCADE, default="", editable=False)
    fb_etc_text = models.CharField(max_length=200)

    def __str__(self):
        return self.etc_bad_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
