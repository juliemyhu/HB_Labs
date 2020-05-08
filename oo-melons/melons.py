"""Classes for melon orders."""

class AbstractMelonOrder():

    def __init__(self, species, qty, order_type, tax ):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.order_type = order_type 
        self.tax = tax # tax changes 
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""
        # christmas melons = 1.5 times as much as baseprice
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        #ordertype and tax is overwritten now
        super()__init__(species,qty,"domestic",0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super()__init__(species,qty, "international", 0.17)

    # own method for InternationalMelonOrder
    def get_country_code(self):
        """Return the country code."""

        return self.country_code
