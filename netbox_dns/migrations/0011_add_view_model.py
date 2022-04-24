# Generated by Django 4.0.4 on 2022-04-22 17:18

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0073_journalentry_tags_custom_fields"),
        ("netbox_dns", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="zone",
            options={"ordering": ("view", "name")},
        ),
        migrations.AlterField(
            model_name="zone",
            name="name",
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name="View",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "custom_field_data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=django.core.serializers.json.DjangoJSONEncoder,
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("default", models.BooleanField(default=False)),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        through="extras.TaggedItem", to="extras.Tag"
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.AddField(
            model_name="zone",
            name="view",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="netbox_dns.view",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="zone",
            unique_together={("view", "name")},
        ),
    ]
