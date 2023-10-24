from django.db import models


class TitleTextAbstractModel(models.Model):
    title = models.CharField(max_length=250,
                             verbose_name='Title')
    text = models.TextField(max_length=10000,
                            verbose_name='Text')

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f'Faq: {self.title}'


class MainFaq(TitleTextAbstractModel):

    class Meta:
        db_table = 'main_faqs'
        verbose_name = 'faq'
        verbose_name_plural = 'Main FAQs'


class PricingFaq(TitleTextAbstractModel):

    class Meta:
        db_table = 'pricing_faqs'
        verbose_name = 'faq'
        verbose_name_plural = 'Pricing FAQs'


HELP_REQUEST_TYPES = ['Functionality', 'Account', 'Pricing', 'Other']


class HelpRequest(models.Model):
    REQUEST_STATUSES = (
        ('ACTIVE', 'ACTIVE'),
        ('IN PROCESSING', 'IN PROCESSING'),
        ('COMPLETED', 'COMPLETED')
    )
    REQUEST_TYPES = (
        (req_type, req_type) for req_type in HELP_REQUEST_TYPES
    )

    status = models.CharField(choices=REQUEST_STATUSES,
                              max_length=150,
                              verbose_name='Request status',
                              default='ACTIVE')
    request_type = models.CharField(choices=REQUEST_TYPES,
                                    max_length=150,
                                    verbose_name='Request type',
                                    default='Functionality')
    email = models.EmailField(verbose_name='Email')
    text = models.TextField(verbose_name='Request text')

    class Meta:
        db_table = 'help_requests'
        verbose_name = 'help request'
        verbose_name_plural = 'Help requests'

    def __str__(self):
        return f'Request #{self.id}. Email: {self.email}'
