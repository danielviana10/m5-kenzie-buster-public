from django.db import models


class MovieOrder(models.Model):
    purchased_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    movie = models.ForeignKey(
        "movies.Movie", related_name="order_movie", on_delete=models.CASCADE
    )
    purchased_by = models.EmailField()

    def create(self, validated_data, user):
        self.purchased_by_email = user.email
        return super(MovieOrder, self).create(**validated_data)
