# Generated by Django 4.2.8 on 2024-03-05 16:49

from django.db import migrations, models
import django.db.models.deletion
import globlocks.blocks.block_fields.rangeslider.rangeslider
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alerts', wagtail.fields.StreamField([('alert', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('ALERT', 'Alert'), ('TOAST', 'Toast')], classname=None, help_text='The template to use for rendering.', label='Template', translatable=False)), ('duration', globlocks.blocks.block_fields.rangeslider.rangeslider.RangeSliderBlock(default=0, help_text='The alert will display for this many milliseconds.<br>1000ms = 1s<br>0ms = infinite.', label='Duration', max_value=25000, min_value=0, stepping=500, unit='ms')), ('dismissible', wagtail.blocks.BooleanBlock(default=True, help_text='Can the alert be dismissed by the user?', label='Dismissible', required=False)), ('alert_theme', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('success', 'Success'), ('danger', 'Danger'), ('warning', 'Warning'), ('info', 'Info'), ('light', 'Light'), ('dark', 'Dark')], help_text='The type/theme of alert to display.', label='Type')), ('once_per_session', wagtail.blocks.BooleanBlock(default=False, help_text='Whether to only show the alert once per session, it will not show after a page refresh for up to a day.', label='Once Per Session', required=False)), ('permanent_dismiss', wagtail.blocks.BooleanBlock(default=True, help_text='If this is true the alert will not be displayed for a day if the user dismisses it.', label='Permanent Dismiss', required=False)), ('dates', wagtail.blocks.StructBlock([('active_from', wagtail.blocks.DateTimeBlock(help_text='The date and time the alert should start being displayed.', label='Active From', required=False)), ('active_to', wagtail.blocks.DateTimeBlock(help_text='The date and time the alert should stop being displayed.', label='Active To', required=False)), ('active', wagtail.blocks.BooleanBlock(default=True, help_text='Whether the alert is active. If not active, the alert will not be displayed.', label='Active', required=False))], label='Active Settings', required=False))])), ('title', wagtail.blocks.CharBlock(label='Title', required=False)), ('body', wagtail.blocks.RichTextBlock(label='Body', required=True))]))], blank=True, null=True, use_json_field=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Alert Settings',
                'verbose_name_plural': 'Alert Settings',
            },
        ),
    ]
