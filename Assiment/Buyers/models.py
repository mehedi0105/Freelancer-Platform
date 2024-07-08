from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

JOB_TYPE = (
    ("part-tyme","part-time"),
    ("Full-time","Full-time"),
)

Rating = (
    ('☆☆☆☆⭐','☆☆☆☆⭐'),
    ('☆☆☆⭐⭐','☆☆☆⭐⭐'),
    ('☆☆⭐⭐⭐','☆☆⭐⭐⭐'),
    ('☆⭐⭐⭐⭐','☆⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
)

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


class AddJob(models.Model):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100, choices=JOB_TYPE)
    job_category =models.ManyToManyField(Category)
    salary = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    job_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['salary']

    def __str__(self):
        return self.title

class Reveiw(models.Model):
    project = models.ForeignKey(AddJob, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=10,choices=Rating)
    reveiw_text = models.TextField()

    def __str__(self):
        return self.freelancer.username