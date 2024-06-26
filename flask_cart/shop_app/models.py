from project.settings import DATABASE

class Product(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)

    name = DATABASE.Column(DATABASE.String(50), nullable = False)
    description = DATABASE.Column(DATABASE.Text, nullable = False)
    price = DATABASE.Column(DATABASE.Integer, nullable = False)
    discount = DATABASE.Column(DATABASE.Integer, nullable = False)
    count = DATABASE.Column(DATABASE.Integer, nullable = False)

    def __repr__(self):
        return f"id: {self.id}; name: {self.name}"