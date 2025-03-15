class Transaction():
    def __init__(self, id, amount, date, description, category, user_id):
        self.id = id
        self.amount = amount
        self.date = date
        self.description = description
        self.category = category
        self.user_id = user_id