from django.db import models

class Orders(models.Model):

    customer = models.ForeignKey("customers.Customers", on_delete=models.CASCADE, related_name="orders_customer")
    description = models.TextField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.customer.name}"