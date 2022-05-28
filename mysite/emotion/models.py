import os

from django.db import models

# Create your models here.
from django.db.models.signals import pre_save

from emotion.kobert import KoBERT
from django.db import models
from django.dispatch import receiver
import pandas as pd
from datetime import datetime


class Document(models.Model):
    txt_file = models.FileField('첨부 파일', upload_to='uploads/')

    def predict(self, file_name):
        kobert = KoBERT()
        print(file_name[-3:])
        if file_name[-3:] == 'txt':
            print("txt")
            predict_sentence = self.txt_file.read().decode('utf-8')
            result_figure = kobert.predict(predict_sentence)
            self.figure_object(result_figure, datetime.now())

            return result_figure

        elif file_name[-3:] == 'csv':
            result_list = []
            fine_data = pd.read_csv(self.txt_file, encoding='UTF-8')
            print("csv")
            for sentence, date in zip(fine_data['본문'], fine_data['작성일']):
                result_figure = kobert.predict(sentence)
                self.figure_object(result_figure, date)
                result_list.append(result_figure)

            return result_list

    def figure_object(self, result_figure, date):
        for i in range(11):
            if i == 0:
                fear = result_figure[i]
            elif i == 1:
                surprise = result_figure[i]
            elif i == 2:
                anger = result_figure[i]
            elif i == 3:
                sadness = result_figure[i]
            elif i == 4:
                neutrality = result_figure[i]
            elif i == 5:
                happiness = result_figure[i]
            elif i == 6:
                anxiety = result_figure[i]
            elif i == 7:
                embarrassed = result_figure[i]
            elif i == 8:
                hurt = result_figure[i]
            elif i == 9:
                interest = result_figure[i]
            elif i == 10:
                boredom = result_figure[i]

        EmotionResult.objects.create(user_id=1,
                                     fear=fear,
                                     surprise=surprise,
                                     anger=anger,
                                     sadness=sadness,
                                     neutrality=neutrality,
                                     happiness=happiness,
                                     anxiety=anxiety,
                                     embarrassed=embarrassed,
                                     hurt=hurt,
                                     interest=interest,
                                     boredom=boredom,
                                     date=date)


class EmotionResult(models.Model):
    user = models.ForeignKey('Recipient', models.DO_NOTHING)
    fear = models.CharField(max_length=20)
    surprise = models.CharField(max_length=45)
    anger = models.CharField(max_length=45)
    sadness = models.CharField(max_length=45)
    neutrality = models.CharField(max_length=45)
    happiness = models.CharField(max_length=45)
    anxiety = models.CharField(max_length=45)
    embarrassed = models.CharField(max_length=45)
    hurt = models.CharField(max_length=45)
    interest = models.CharField(max_length=45)
    boredom = models.CharField(max_length=45)
    date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'emotion_result'


class Recipient(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    contact = models.IntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=45)
    birth = models.DateField()
    status = models.CharField(max_length=8)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipient'


class AuthUser(models.Model):
    id = models.CharField(primary_key=True, max_length=12)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=150)
    relationship = models.CharField(max_length=8)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    recipient_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'

