from django.db import models

# Create your models here.

class BorrowFacility(models.Model):
    facilityName = models.CharField(max_length=100)
    startTime = models.DateTimeField()
    lengthOfTime = models.DurationField()
    
    def __str__(self):
        return "%s" % (self.facilityName)


class EntrustLaundryToWash(models.Model):
    washType_CHICES = (('1', 'damp washing'), ('2', 'dry cleaning'))

    washType = models.CharField(
       max_length=1,
       choices=washType_CHICES,
   )
    remark = models.CharField(max_length=100)
    returnClothesTime = models.DateTimeField()

class ParkingSpaceApplication(models.Model):
    parkingSpaceType_CHICES = (('1', 'Small car'), ('2', 'Heavy locomotive'), ('3', 'Scooter'))

    parkingSpaceType = models.CharField(
       max_length=1,
       choices=parkingSpaceType_CHICES,
   )
    desiredLocation = models.CharField(max_length=100)
