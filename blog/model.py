# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_post'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EggmorningHotel(models.Model):
    hotel_no = models.IntegerField()
    addr = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'eggmorning_hotel'


class EggmorningHotelscore(models.Model):
    score = models.FloatField()
    category = models.ForeignKey('EggmorningRankcategory', models.DO_NOTHING)
    hotel = models.ForeignKey(EggmorningHotel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'eggmorning_hotelscore'


class EggmorningMainslide(models.Model):
    title = models.CharField(max_length=128)
    image = models.CharField(max_length=1024)
    username = models.CharField(max_length=64)
    desc = models.CharField(max_length=256, blank=True, null=True)
    priority = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    mod_date = models.DateTimeField()
    reg_date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'eggmorning_mainslide'


class EggmorningRankcategory(models.Model):
    cat_no = models.IntegerField()
    cat_type = models.CharField(max_length=8)
    cat_name = models.CharField(max_length=32)
    cat_code = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'eggmorning_rankcategory'


class EggmorningUser(models.Model):
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)
    birth = models.DateField()
    gender = models.CharField(max_length=1)
    date_joined = models.DateTimeField()
    email = models.CharField(unique=True, max_length=255)
    is_active = models.IntegerField()
    is_admin = models.IntegerField()
    is_staff = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    nickname = models.CharField(unique=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'eggmorning_user'


class EggmorningUserGroups(models.Model):
    user = models.ForeignKey(EggmorningUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'eggmorning_user_groups'
        unique_together = (('user', 'group'),)


class EggmorningUserUserPermissions(models.Model):
    user = models.ForeignKey(EggmorningUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'eggmorning_user_user_permissions'
        unique_together = (('user', 'permission'),)
