# Generated by Django 3.1.2 on 2020-10-25 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('address', models.TextField(null=True)),
                ('Zipcode', models.IntegerField(null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'Address',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('contact_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('email_id', models.EmailField(max_length=254, null=True)),
                ('contact_no', models.BigIntegerField(null=True)),
                ('message', models.TextField(null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'Contact_us',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('coupon_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('coupon_code', models.CharField(max_length=20, null=True)),
                ('activation_date', models.DateField(null=True)),
                ('expiry_date', models.DateField(null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'Coupon',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('email_id', models.EmailField(max_length=254, null=True)),
                ('password', models.CharField(default='', max_length=200, null=True)),
                ('contact_no', models.BigIntegerField(null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
                ('address_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.address')),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Customer_Order',
            fields=[
                ('customer_order_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('contact_no', models.BigIntegerField(null=True)),
                ('order_date', models.DateField(null=True)),
                ('order_amount', models.FloatField(null=True)),
                ('productinfo', models.CharField(default='', max_length=255)),
                ('is_successful', models.IntegerField(null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
                ('status', models.CharField(max_length=255, null=True)),
                ('address_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.address')),
                ('customer_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.customer')),
            ],
            options={
                'db_table': 'Customer_Order',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('newsletter_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email_id', models.EmailField(max_length=254, null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'Newsletter',
            },
        ),
        migrations.CreateModel(
            name='Payment_Type',
            fields=[
                ('payment_type_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'Payment_Type',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('total_stock', models.IntegerField(null=True)),
                ('current_stock', models.IntegerField(null=True)),
                ('price', models.FloatField(null=True)),
                ('rating', models.FloatField(null=True)),
                ('product_size', models.CharField(max_length=100, null=True)),
                ('product_image', models.ImageField(null=True, upload_to='Products')),
                ('is_wrinkle_product', models.IntegerField(default=0)),
                ('is_pimple_product', models.IntegerField(default=0)),
                ('skintone', models.CharField(max_length=100, null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='Product_Brand',
            fields=[
                ('product_brand_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'Product_Brand',
            },
        ),
        migrations.CreateModel(
            name='Product_Color',
            fields=[
                ('product_color_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('shade_name', models.CharField(max_length=20, null=True)),
                ('color_code', models.CharField(max_length=20, null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'Product_Color',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('role_type', models.CharField(max_length=20, null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'Role',
            },
        ),
        migrations.CreateModel(
            name='Skin_Survey',
            fields=[
                ('skin_survey_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('picture', models.ImageField(null=True, upload_to='survey_images')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'State',
            },
        ),
        migrations.CreateModel(
            name='Sub_Category1',
            fields=[
                ('sub_category1_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
                ('category_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.category')),
            ],
            options={
                'db_table': 'Sub_Category1',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=20, null=True)),
                ('contact_no', models.BigIntegerField(null=True)),
                ('email_id', models.EmailField(max_length=254, null=True)),
                ('password', models.CharField(default='', max_length=20, null=True)),
                ('partnership_date', models.DateField(null=True)),
                ('latest_supply_date', models.DateField(null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
                ('address_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.address')),
                ('payment_type_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Client.payment_type')),
                ('role_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.role')),
            ],
            options={
                'db_table': 'Supplier',
            },
        ),
        migrations.CreateModel(
            name='Sub_Category2',
            fields=[
                ('sub_category2_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
                ('sub_category1_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.sub_category1')),
            ],
            options={
                'db_table': 'Sub_Category2',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('review_message', models.TextField(null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
                ('customer_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.customer')),
                ('product_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.product')),
            ],
            options={
                'db_table': 'Review',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.product_brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='color_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.product_color'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category2_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.sub_category2'),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.supplier'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('is_successful', models.IntegerField(null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
                ('customer_order_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.customer_order')),
            ],
            options={
                'db_table': 'Payment',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='role_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.role'),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
                ('state_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.state')),
            ],
            options={
                'db_table': 'City',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('email_id', models.EmailField(max_length=254, null=True)),
                ('password', models.CharField(default='', max_length=20, null=True)),
                ('contact_no', models.BigIntegerField(null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
                ('role_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.role')),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='city_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.city'),
        ),
    ]
