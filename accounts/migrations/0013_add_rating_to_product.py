from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_productdetailimage_productid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
