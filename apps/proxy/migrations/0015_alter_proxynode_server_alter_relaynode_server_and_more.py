# Generated by Django 4.1.3 on 2022-11-19 08:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("proxy", "0014_alter_trojanconfig_fallback_addr"),
    ]

    operations = [
        migrations.AlterField(
            model_name="proxynode",
            name="server",
            field=models.CharField(
                help_text="服务器地址", max_length=256, verbose_name="服务器地址"
            ),
        ),
        migrations.AlterField(
            model_name="relaynode",
            name="server",
            field=models.CharField(
                help_text="服务器地址", max_length=256, verbose_name="服务器地址"
            ),
        ),
        migrations.AlterField(
            model_name="usertrafficlog",
            name="proxy_node",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="proxy.proxynode",
                verbose_name="代理节点",
            ),
        ),
        migrations.AlterField(
            model_name="usertrafficlog",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
                verbose_name="用户",
            ),
        ),
    ]