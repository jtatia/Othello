from django.db import models

class Game(models.Model):
    token = models.AutoField(primary_key=True)
    gameboard = models.CharField(max_length=64, default='0000000000000000000000000001200000021000000000000000000000000000')
    count = models.IntegerField(default=0)
    turn = models.IntegerField(default=2)
    player = models.IntegerField(default=1)
    timer = models.IntegerField(default=60)
    gameEnd = models.IntegerField(default=0)

    def __str__(self):
        return "Token : "+str(self.token)