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
