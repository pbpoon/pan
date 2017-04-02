from django.db import models


class Account(models.Model):
    name = models.CharField('户名号码', unique=True, db_index=True, max_length=12)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新日期', auto_now=True)

    class Meta:
        verbose_name = '户口号码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}:{1}".format(self.name, self.people.get(is_main=True))


class People(models.Model):
    SEX_CHOICES = (
        ('male', '男'),
        ('female', '女'),
    )
    first_name = models.CharField('姓氏', max_length=8)
    last_name = models.CharField('名字', max_length=12)
    sex = models.CharField('性别', choices=SEX_CHOICES, max_length=6)
    id_card_num = models.CharField('身份证号码', db_index=True, max_length=18, null=True, blank=True)
    is_main = models.BooleanField('是否为户主', default=False)
    account = models.ForeignKey('Account', related_name='people',null=True, blank=True, verbose_name='所属户口')
    birthday = models.DateField('出生日期', null=True, blank=True)
    is_marry = models.BooleanField('是否已婚', default=False)
    is_getmoney = models.BooleanField('分钱资格', default=False)
    joind =models.DateField('入户日期', null=True, blank=True)
    nationality = models.CharField('民族', null=True, blank=True, max_length=26)
    education = models.CharField('教育程度', null=True, blank=True, max_length=20)
    account_type =models.CharField('户口类型', null=True, blank=True, max_length=20)
    phone_num = models.CharField('电话号码', null=True, blank=True, max_length=11)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新日期', auto_now=True)
    is_del = models.BooleanField('是否注销', default=False)

    class Meta:
        verbose_name = '村民信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_age(self):
        pass

