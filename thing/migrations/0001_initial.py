# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alliance',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('short_name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='APIKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyid', models.IntegerField(verbose_name=b'Key ID', db_index=True)),
                ('vcode', models.CharField(max_length=64, verbose_name=b'Verification code')),
                ('access_mask', models.BigIntegerField(default=0)),
                ('override_mask', models.BigIntegerField(default=0)),
                ('key_type', models.CharField(default=b'', max_length=16)),
                ('expires', models.DateTimeField(null=True, blank=True)),
                ('paid_until', models.DateTimeField(null=True, blank=True)),
                ('name', models.CharField(default=b'', max_length=64)),
                ('group_name', models.CharField(default=b'', max_length=32)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('valid', models.BooleanField(default=True)),
                ('needs_apikeyinfo', models.BooleanField(default=False)),
                ('apikeyinfo_errors', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('keyid',),
            },
        ),
        migrations.CreateModel(
            name='APIKeyFailure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyid', models.IntegerField()),
                ('fail_time', models.DateTimeField(db_index=True)),
                ('fail_reason', models.CharField(max_length=255)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asset_id', models.BigIntegerField(db_index=True)),
                ('parent', models.BigIntegerField(default=0)),
                ('corporation_id', models.IntegerField(default=0, db_index=True)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('quantity', models.IntegerField()),
                ('raw_quantity', models.IntegerField()),
                ('singleton', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AssetSummary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('corporation_id', models.IntegerField(default=0)),
                ('total_items', models.BigIntegerField()),
                ('total_volume', models.DecimalField(max_digits=12, decimal_places=2)),
                ('total_value', models.DecimalField(max_digits=18, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Blueprint',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('productionLimit', models.IntegerField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='BlueprintComponent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity', models.IntegerField(choices=[(0, b'None'), (1, b'Manufacturing'), (2, b'Researching Technology'), (3, b'TE Research'), (4, b'ME Research'), (5, b'Copying'), (6, b'Duplicating'), (7, b'Reverse Engineering'), (8, b'Invention')])),
                ('count', models.IntegerField()),
                ('consumed', models.BooleanField(default=False)),
                ('blueprint', models.ForeignKey(to='thing.Blueprint')),
            ],
        ),
        migrations.CreateModel(
            name='BlueprintInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('original', models.BooleanField(default=False)),
                ('material_level', models.IntegerField(default=0)),
                ('productivity_level', models.IntegerField(default=0)),
                ('blueprint', models.ForeignKey(to='thing.Blueprint')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('blueprint',),
            },
        ),
        migrations.CreateModel(
            name='BlueprintProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity', models.IntegerField(choices=[(0, b'None'), (1, b'Manufacturing'), (2, b'Researching Technology'), (3, b'TE Research'), (4, b'ME Research'), (5, b'Copying'), (6, b'Duplicating'), (7, b'Reverse Engineering'), (8, b'Invention')])),
                ('count', models.IntegerField()),
                ('blueprint', models.ForeignKey(to='thing.Blueprint')),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32)),
                ('slug', models.SlugField(max_length=32)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CharacterSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.SmallIntegerField()),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Clone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CloneImplant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clone', models.ForeignKey(related_name='implants', to='thing.Clone')),
            ],
        ),
        migrations.CreateModel(
            name='Colony',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('planet_id', models.IntegerField()),
                ('planet', models.CharField(max_length=128)),
                ('planet_type', models.CharField(max_length=32)),
                ('last_update', models.DateTimeField()),
                ('level', models.IntegerField()),
                ('pins', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Constellation',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contract_id', models.IntegerField(db_index=True)),
                ('assignee_id', models.IntegerField(default=0)),
                ('acceptor_id', models.IntegerField(default=0)),
                ('type', models.CharField(max_length=16)),
                ('status', models.CharField(max_length=24)),
                ('title', models.CharField(max_length=64)),
                ('for_corp', models.BooleanField(default=False)),
                ('public', models.BooleanField(default=False)),
                ('date_issued', models.DateTimeField()),
                ('date_expired', models.DateTimeField()),
                ('date_accepted', models.DateTimeField(null=True, blank=True)),
                ('date_completed', models.DateTimeField(null=True, blank=True)),
                ('num_days', models.IntegerField()),
                ('price', models.DecimalField(max_digits=15, decimal_places=2)),
                ('reward', models.DecimalField(max_digits=15, decimal_places=2)),
                ('collateral', models.DecimalField(max_digits=15, decimal_places=2)),
                ('buyout', models.DecimalField(max_digits=15, decimal_places=2)),
                ('volume', models.DecimalField(max_digits=16, decimal_places=4)),
                ('retrieved_items', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date_issued',),
            },
        ),
        migrations.CreateModel(
            name='ContractItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contract_id', models.IntegerField(db_index=True)),
                ('quantity', models.IntegerField()),
                ('raw_quantity', models.IntegerField()),
                ('singleton', models.BooleanField(default=False)),
                ('included', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('ticker', models.CharField(default=b'', max_length=5)),
                ('division1', models.CharField(default=b'', max_length=64)),
                ('division2', models.CharField(default=b'', max_length=64)),
                ('division3', models.CharField(default=b'', max_length=64)),
                ('division4', models.CharField(default=b'', max_length=64)),
                ('division5', models.CharField(default=b'', max_length=64)),
                ('division6', models.CharField(default=b'', max_length=64)),
                ('division7', models.CharField(default=b'', max_length=64)),
                ('alliance', models.ForeignKey(blank=True, to='thing.Alliance', null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CorporationStanding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('standing', models.DecimalField(max_digits=4, decimal_places=2)),
            ],
            options={
                'ordering': ('-standing',),
            },
        ),
        migrations.CreateModel(
            name='CorpWallet',
            fields=[
                ('account_id', models.IntegerField(serialize=False, primary_key=True)),
                ('account_key', models.IntegerField()),
                ('description', models.CharField(max_length=64)),
                ('balance', models.DecimalField(max_digits=18, decimal_places=2)),
                ('corporation', models.ForeignKey(to='thing.Corporation')),
            ],
            options={
                'ordering': ('corporation', 'account_id'),
            },
        ),
        migrations.CreateModel(
            name='ESIToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_token', models.CharField(max_length=128)),
                ('refresh_token', models.CharField(max_length=320)),
                ('status', models.BooleanField(default=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('token_type', models.CharField(max_length=32)),
                ('characterID', models.IntegerField(default=None, null=True)),
                ('corporationID', models.IntegerField(default=None, null=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issued', models.DateTimeField()),
                ('text', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-issued', '-id'),
            },
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='FactionStanding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('standing', models.DecimalField(max_digits=4, decimal_places=2)),
            ],
            options={
                'ordering': ('-standing',),
            },
        ),
        migrations.CreateModel(
            name='IndustryJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_id', models.IntegerField()),
                ('installer_id', models.IntegerField()),
                ('activity', models.IntegerField(choices=[(0, b'None'), (1, b'Manufacturing'), (2, b'Researching Technology'), (3, b'TE Research'), (4, b'ME Research'), (5, b'Copying'), (6, b'Duplicating'), (7, b'Reverse Engineering'), (8, b'Invention')])),
                ('output_location_id', models.BigIntegerField()),
                ('runs', models.IntegerField()),
                ('team_id', models.BigIntegerField()),
                ('licensed_runs', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, b'Active'), (2, b'Paused (Facility Offline)'), (3, b'Ready'), (102, b'Cancelled'), (104, b'Delivered'), (105, b'Failed'), (999, b'Unknown')])),
                ('duration', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('pause_date', models.DateTimeField()),
                ('completed_date', models.DateTimeField()),
                ('blueprint', models.ForeignKey(related_name='job_installed_blueprints', to='thing.Blueprint')),
            ],
            options={
                'ordering': ('-end_date',),
            },
        ),
        migrations.CreateModel(
            name='InventoryFlag',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('text', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('portion_size', models.IntegerField()),
                ('volume', models.DecimalField(default=0, max_digits=16, decimal_places=4)),
                ('base_price', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('sell_price', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('buy_price', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ItemGroup',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('category', models.ForeignKey(to='thing.ItemCategory')),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(db_index=True)),
                ('ref_id', models.BigIntegerField(db_index=True)),
                ('owner1_id', models.IntegerField()),
                ('owner2_id', models.IntegerField()),
                ('arg_name', models.CharField(max_length=128)),
                ('arg_id', models.BigIntegerField()),
                ('amount', models.DecimalField(max_digits=14, decimal_places=2)),
                ('balance', models.DecimalField(max_digits=17, decimal_places=2)),
                ('reason', models.CharField(max_length=255)),
                ('tax_amount', models.DecimalField(max_digits=14, decimal_places=2)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MailMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_id', models.BigIntegerField()),
                ('sender_id', models.IntegerField()),
                ('sent_date', models.DateTimeField()),
                ('title', models.CharField(max_length=255)),
                ('to_corp_or_alliance_id', models.IntegerField()),
                ('to_list_id', models.IntegerField()),
                ('body', models.TextField(null=True, blank=True)),
                ('read', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-sent_date',),
            },
        ),
        migrations.CreateModel(
            name='MarketGroup',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='thing.MarketGroup', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MarketOrder',
            fields=[
                ('order_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('creator_character_id', models.IntegerField(db_index=True)),
                ('escrow', models.DecimalField(max_digits=14, decimal_places=2)),
                ('price', models.DecimalField(max_digits=14, decimal_places=2)),
                ('total_price', models.DecimalField(max_digits=17, decimal_places=2)),
                ('buy_order', models.BooleanField(default=False)),
                ('volume_entered', models.IntegerField()),
                ('volume_remaining', models.IntegerField()),
                ('minimum_volume', models.IntegerField()),
                ('issued', models.DateTimeField(db_index=True)),
                ('expires', models.DateTimeField(db_index=True)),
            ],
            options={
                'ordering': ('buy_order', 'item__name'),
            },
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pin_id', models.BigIntegerField(db_index=True)),
                ('schematic', models.IntegerField()),
                ('cycle_time', models.IntegerField()),
                ('quantity_per_cycle', models.IntegerField()),
                ('installed', models.DateTimeField()),
                ('expires', models.DateTimeField()),
                ('last_launched', models.DateTimeField()),
                ('content_size', models.DecimalField(default=0, max_digits=16, decimal_places=4)),
                ('colony', models.ForeignKey(to='thing.Colony')),
            ],
        ),
        migrations.CreateModel(
            name='PinContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('minimum', models.DecimalField(max_digits=18, decimal_places=2)),
                ('maximum', models.DecimalField(max_digits=18, decimal_places=2)),
                ('average', models.DecimalField(max_digits=18, decimal_places=2)),
                ('movement', models.BigIntegerField()),
                ('orders', models.IntegerField()),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='RefType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SkillPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('visibility', models.IntegerField(default=1, choices=[(1, b'Private'), (2, b'Public'), (3, b'Global')])),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SkillQueue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('start_sp', models.IntegerField()),
                ('end_sp', models.IntegerField()),
                ('to_level', models.SmallIntegerField()),
            ],
            options={
                'ordering': ('start_time',),
            },
        ),
        migrations.CreateModel(
            name='SPEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField()),
                ('skill_plan', models.ForeignKey(related_name='entries', to='thing.SkillPlan')),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='SPRemap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('int_stat', models.IntegerField()),
                ('mem_stat', models.IntegerField()),
                ('per_stat', models.IntegerField()),
                ('wil_stat', models.IntegerField()),
                ('cha_stat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SPSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('short_name', models.CharField(default=b'', max_length=64)),
                ('structure', models.BooleanField(default=False)),
                ('lastupdated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('constellation', models.ForeignKey(to='thing.Constellation')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TaskState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyid', models.IntegerField(db_index=True)),
                ('url', models.CharField(max_length=64, db_index=True)),
                ('parameter', models.IntegerField(db_index=True)),
                ('state', models.IntegerField(db_index=True)),
                ('mod_time', models.DateTimeField(db_index=True)),
                ('next_time', models.DateTimeField(db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transaction_id', models.BigIntegerField(db_index=True)),
                ('date', models.DateTimeField(db_index=True)),
                ('buy_transaction', models.BooleanField(default=False)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(max_digits=14, decimal_places=2)),
                ('total_price', models.DecimalField(max_digits=17, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_seen', models.DateTimeField(default=datetime.datetime.now)),
                ('can_add_keys', models.BooleanField(default=True)),
                ('theme', models.CharField(default=b'default', max_length=32)),
                ('show_clock', models.BooleanField(default=True)),
                ('show_assets', models.BooleanField(default=True)),
                ('show_blueprints', models.BooleanField(default=True)),
                ('show_contracts', models.BooleanField(default=True)),
                ('show_industry', models.BooleanField(default=True)),
                ('show_orders', models.BooleanField(default=True)),
                ('show_trade', models.BooleanField(default=True)),
                ('show_transactions', models.BooleanField(default=True)),
                ('show_wallet_journal', models.BooleanField(default=True)),
                ('show_pi', models.BooleanField(default=True)),
                ('show_item_icons', models.BooleanField(default=False)),
                ('entries_per_page', models.IntegerField(default=100)),
                ('home_chars_per_row', models.IntegerField(default=4)),
                ('home_sort_order', models.CharField(default=b'apiname', max_length=12, choices=[(b'apiname', b'APIKey name'), (b'charname', b'Character name'), (b'corpname', b'Corporation name'), (b'totalsp', b'Total SP'), (b'wallet', b'Wallet balance')])),
                ('home_sort_descending', models.BooleanField(default=False)),
                ('home_hide_characters', models.TextField(default=b'', blank=True)),
                ('home_show_locations', models.BooleanField(default=True)),
                ('home_highlight_backgrounds', models.BooleanField(default=True)),
                ('home_highlight_borders', models.BooleanField(default=True)),
                ('home_show_separators', models.BooleanField(default=True)),
                ('home_show_security', models.BooleanField(default=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterConfig',
            fields=[
                ('character', models.OneToOneField(related_name='config', primary_key=True, serialize=False, to='thing.Character')),
                ('is_public', models.BooleanField(default=False)),
                ('show_implants', models.BooleanField(default=False)),
                ('show_skill_queue', models.BooleanField(default=False)),
                ('show_standings', models.BooleanField(default=False)),
                ('show_wallet', models.BooleanField(default=False)),
                ('anon_key', models.CharField(default=b'', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterDetails',
            fields=[
                ('character', models.OneToOneField(related_name='details', primary_key=True, serialize=False, to='thing.Character')),
                ('wallet_balance', models.DecimalField(default=0, max_digits=18, decimal_places=2)),
                ('cha_attribute', models.SmallIntegerField(default=20)),
                ('int_attribute', models.SmallIntegerField(default=20)),
                ('mem_attribute', models.SmallIntegerField(default=20)),
                ('per_attribute', models.SmallIntegerField(default=20)),
                ('wil_attribute', models.SmallIntegerField(default=19)),
                ('security_status', models.DecimalField(default=0, max_digits=6, decimal_places=4)),
                ('last_known_location', models.CharField(default=b'', max_length=255)),
                ('ship_name', models.CharField(default=b'', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Implant',
            fields=[
                ('item', models.OneToOneField(primary_key=True, serialize=False, to='thing.Item')),
                ('description', models.TextField()),
                ('charisma_modifier', models.SmallIntegerField()),
                ('intelligence_modifier', models.SmallIntegerField()),
                ('memory_modifier', models.SmallIntegerField()),
                ('perception_modifier', models.SmallIntegerField()),
                ('willpower_modifier', models.SmallIntegerField()),
                ('implant_slot', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('item', models.OneToOneField(primary_key=True, serialize=False, to='thing.Item')),
                ('rank', models.SmallIntegerField()),
                ('description', models.TextField()),
                ('primary_attribute', models.SmallIntegerField(choices=[(164, b'Cha'), (165, b'Int'), (166, b'Mem'), (167, b'Per'), (168, b'Wil')])),
                ('secondary_attribute', models.SmallIntegerField(choices=[(164, b'Cha'), (165, b'Int'), (166, b'Mem'), (167, b'Per'), (168, b'Wil')])),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='character',
            field=models.ForeignKey(to='thing.Character'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='corp_wallet',
            field=models.ForeignKey(blank=True, to='thing.CorpWallet', null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='item',
            field=models.ForeignKey(to='thing.Item'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='other_char',
            field=models.ForeignKey(related_name='transaction_others', blank=True, to='thing.Character', null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='other_corp',
            field=models.ForeignKey(blank=True, to='thing.Corporation', null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='station',
            field=models.ForeignKey(to='thing.Station'),
        ),
        migrations.AddField(
            model_name='station',
            name='system',
            field=models.ForeignKey(to='thing.System'),
        ),
        migrations.AddField(
            model_name='spentry',
            name='sp_remap',
            field=models.ForeignKey(blank=True, to='thing.SPRemap', null=True),
        ),
        migrations.AddField(
            model_name='spentry',
            name='sp_skill',
            field=models.ForeignKey(blank=True, to='thing.SPSkill', null=True),
        ),
        migrations.AddField(
            model_name='skillqueue',
            name='character',
            field=models.ForeignKey(to='thing.Character'),
        ),
        migrations.AddField(
            model_name='pricehistory',
            name='item',
            field=models.ForeignKey(to='thing.Item'),
        ),
        migrations.AddField(
            model_name='pricehistory',
            name='region',
            field=models.ForeignKey(to='thing.Region'),
        ),
        migrations.AddField(
            model_name='pincontent',
            name='item',
            field=models.ForeignKey(related_name='+', to='thing.Item'),
        ),
        migrations.AddField(
            model_name='pincontent',
            name='pin',
            field=models.ForeignKey(to='thing.Pin'),
        ),
        migrations.AddField(
            model_name='pin',
            name='type',
            field=models.ForeignKey(related_name='+', to='thing.Item'),
        ),
        migrations.AddField(
            model_name='marketorder',
            name='character',
            field=models.ForeignKey(to='thing.Character'),
        ),
        migrations.AddField(
            model_name='marketorder',
            name='corp_wallet',
            field=models.ForeignKey(blank=True, to='thing.CorpWallet', null=True),
        ),
        migrations.AddField(
            model_name='marketorder',
            name='item',
            field=models.ForeignKey(to='thing.Item'),
        ),
        migrations.AddField(
            model_name='marketorder',
            name='station',
            field=models.ForeignKey(to='thing.Station'),
        ),
        migrations.AddField(
            model_name='mailmessage',
            name='character',
            field=models.ForeignKey(to='thing.Character'),
        ),
        migrations.AddField(
            model_name='mailmessage',
            name='to_characters',
            field=models.ManyToManyField(related_name='_mailmessage_to_characters_+', to='thing.Character'),
        ),
        migrations.AddField(
            model_name='journalentry',
            name='character',
            field=models.ForeignKey(to='thing.Character'),
        ),
        migrations.AddField(
            model_name='journalentry',
            name='corp_wallet',
            field=models.ForeignKey(blank=True, to='thing.CorpWallet', null=True),
        ),
        migrations.AddField(
            model_name='journalentry',
            name='ref_type',
            field=models.ForeignKey(to='thing.RefType'),
        ),
        migrations.AddField(
            model_name='journalentry',
            name='tax_corp',
            field=models.ForeignKey(blank=True, to='thing.Corporation', null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='item_group',
            field=models.ForeignKey(to='thing.ItemGroup'),
        ),
        migrations.AddField(
            model_name='item',
            name='market_group',
            field=models.ForeignKey(blank=True, to='thing.MarketGroup', null=True),
        ),
        migrations.AddField(
            model_name='industryjob',
            name='character',
            field=models.ForeignKey(to='thing.Character'),
        ),
        migrations.AddField(
            model_name='industryjob',
            name='corporation',
            field=models.ForeignKey(blank=True, to='thing.Corporation', null=True),
        ),
        migrations.AddField(
            model_name='industryjob',
            name='product',
            field=models.ForeignKey(related_name='job_products', blank=True, to='thing.Item', null=True),
        ),
        migrations.AddField(
            model_name='industryjob',
            name='system',
            field=models.ForeignKey(to='thing.System'),
        ),
        migrations.AddField(
            model_name='factionstanding',
            name='character',
            field=models.ForeignKey(to='thing.Character'),
        ),
        migrations.AddField(
            model_name='factionstanding',
            name='faction',
            field=models.ForeignKey(to='thing.Faction'),
        ),
        migrations.AddField(
            model_name='esitoken',
            name='character',
            field=models.OneToOneField(related_name='esitoken', null=True, to='thing.Character'),
        ),
        migrations.AddField(
            model_name='esitoken',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='corporationstanding',
            name='character',
            field=models.ForeignKey(to='thing.Character'),
        ),
        migrations.AddField(
            model_name='corporationstanding',
            name='corporation',
            field=models.ForeignKey(to='thing.Corporation'),
        ),
        migrations.AddField(
            model_name='contractitem',
            name='item',
            field=models.ForeignKey(related_name='contract_items', to='thing.Item'),
        ),
        migrations.AddField(
            model_name='contract',
            name='character',
            field=models.ForeignKey(to='thing.Character'),
        ),
        migrations.AddField(
            model_name='contract',
            name='corporation',
            field=models.ForeignKey(blank=True, to='thing.Corporation', null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='end_station',
            field=models.ForeignKey(related_name='+', blank=True, to='thing.Station', null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='issuer_char',
            field=models.ForeignKey(related_name='+', blank=True, to='thing.Character', null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='issuer_corp',
            field=models.ForeignKey(related_name='+', to='thing.Corporation'),
        ),
        migrations.AddField(
            model_name='contract',
            name='start_station',
            field=models.ForeignKey(related_name='+', blank=True, to='thing.Station', null=True),
        ),
        migrations.AddField(
            model_name='constellation',
            name='region',
            field=models.ForeignKey(to='thing.Region'),
        ),
        migrations.AddField(
            model_name='colony',
            name='character',
            field=models.ForeignKey(to='thing.Character'),
        ),
        migrations.AddField(
            model_name='colony',
            name='system',
            field=models.ForeignKey(to='thing.System'),
        ),
        migrations.AddField(
            model_name='clone',
            name='character',
            field=models.ForeignKey(related_name='clones', to='thing.Character'),
        ),
        migrations.AddField(
            model_name='clone',
            name='location',
            field=models.ForeignKey(to='thing.Station', null=True),
        ),
        migrations.AddField(
            model_name='characterskill',
            name='character',
            field=models.ForeignKey(related_name='skills', to='thing.Character'),
        ),
        migrations.AddField(
            model_name='character',
            name='corporation',
            field=models.ForeignKey(blank=True, to='thing.Corporation', null=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='characters',
            field=models.ManyToManyField(to='thing.Character', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='corp_wallets',
            field=models.ManyToManyField(to='thing.CorpWallet', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blueprintproduct',
            name='item',
            field=models.ForeignKey(to='thing.Item'),
        ),
        migrations.AddField(
            model_name='blueprintcomponent',
            name='item',
            field=models.ForeignKey(to='thing.Item'),
        ),
        migrations.AddField(
            model_name='assetsummary',
            name='character',
            field=models.ForeignKey(to='thing.Character'),
        ),
        migrations.AddField(
            model_name='assetsummary',
            name='station',
            field=models.ForeignKey(blank=True, to='thing.Station', null=True),
        ),
        migrations.AddField(
            model_name='assetsummary',
            name='system',
            field=models.ForeignKey(to='thing.System'),
        ),
        migrations.AddField(
            model_name='asset',
            name='character',
            field=models.ForeignKey(to='thing.Character'),
        ),
        migrations.AddField(
            model_name='asset',
            name='inv_flag',
            field=models.ForeignKey(to='thing.InventoryFlag'),
        ),
        migrations.AddField(
            model_name='asset',
            name='item',
            field=models.ForeignKey(to='thing.Item'),
        ),
        migrations.AddField(
            model_name='asset',
            name='station',
            field=models.ForeignKey(blank=True, to='thing.Station', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='system',
            field=models.ForeignKey(blank=True, to='thing.System', null=True),
        ),
        migrations.AddField(
            model_name='apikey',
            name='characters',
            field=models.ManyToManyField(related_name='apikeys', to='thing.Character'),
        ),
        migrations.AddField(
            model_name='apikey',
            name='corp_character',
            field=models.ForeignKey(related_name='corporate_apikey', blank=True, to='thing.Character', null=True),
        ),
        migrations.AddField(
            model_name='apikey',
            name='corporation',
            field=models.ForeignKey(blank=True, to='thing.Corporation', null=True),
        ),
        migrations.AddField(
            model_name='apikey',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='spskill',
            name='skill',
            field=models.ForeignKey(to='thing.Skill'),
        ),
        migrations.AddField(
            model_name='skillqueue',
            name='skill',
            field=models.ForeignKey(to='thing.Skill'),
        ),
        migrations.AlterUniqueTogether(
            name='pricehistory',
            unique_together=set([('region', 'item', 'date')]),
        ),
        migrations.AlterUniqueTogether(
            name='colony',
            unique_together=set([('character', 'planet_id')]),
        ),
        migrations.AddField(
            model_name='cloneimplant',
            name='implant',
            field=models.ForeignKey(to='thing.Implant'),
        ),
        migrations.AddField(
            model_name='characterskill',
            name='skill',
            field=models.ForeignKey(to='thing.Skill'),
        ),
        migrations.AddField(
            model_name='characterdetails',
            name='implants',
            field=models.ManyToManyField(to='thing.Implant'),
        ),
        migrations.AddField(
            model_name='characterdetails',
            name='ship_item',
            field=models.ForeignKey(blank=True, to='thing.Item', null=True),
        ),
    ]
