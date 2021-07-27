from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models


# Create your models here.
class AbstractItem(core_models.TimeStampedModel):
    """AbstractItem Object Definition"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """Room Type Model Definition"""

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):
    """Amenity Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """HouseRule Model Definition"""

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):
    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(
        upload_to="room_photos",
    )
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):
    """Room Model Definifion"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    city = models.CharField(max_length=80)
    country = CountryField()
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_out = models.TimeField()
    check_in = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.CASCADE, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rule = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_rating = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_rating += review.rating_average()
            return round(all_rating / len(all_reviews), 2)
        else:
            return 0

    total_rating.short_description = "rating"

    def first_photo(self):
        (photo,) = self.photos.all()[:1]
        return photo.file.url
