from django.db import models

# Create your models here.
book_choices = (
    ('general', 'General'),
    ('sports', 'Sports'),
    ('science', 'Science'),
    ('political', 'Political'),
    ('story', 'Story'),
    ('bio', 'Auto Biography'),
    ('other', 'Other')
)

class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    # fields  field type       field option
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=book_choices, default='other')

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.title
