from django.db import models
import jwt
import datetime
import hashlib


class Access(models.Model):
    name = models.CharField(max_length=25, default='new',
                            verbose_name="Доступ")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Доступ"
        verbose_name_plural = "Доступы"


class Token(models.Model):
    token = models.CharField(max_length=255, unique=True, blank=True, null=True, verbose_name="Токен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    access = models.ManyToManyField(Access, related_name='access', verbose_name="Доступы")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = self.created_at or datetime.datetime.now()
            payload = {
                'date': self.created_at.isoformat()
            }
            jwt_token = jwt.encode(payload, 'my_secret_key', algorithm='HS256')
            if isinstance(jwt_token, bytes):  # В случае, если токен возвращается как байты, конвертируем его в строку
                jwt_token = jwt_token.decode('utf-8')
            # Используем hashlib для создания хэша и берем первые 12 символов
            self.token = hashlib.sha256(jwt_token.encode('utf-8')).hexdigest()[:12]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.created_at} - {self.token}"

    class Meta:
        verbose_name = "Токен"
        verbose_name_plural = "Токены"

class Client(models.Model):
    tokens = models.ManyToManyField(Token, related_name='tokens', verbose_name="Токены")
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Имя клиента")
    description = models.TextField(blank=True, null=True, verbose_name="Описание", default='')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
