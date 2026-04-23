class MockUser:
    def __init__(self):
        self.first = "Andrés"
        self.last = "Baños Lajusticia"
        self.email = "abanoslg@example.com"
        self.tlf = "+34 123 456 789"

db = MockUser()


def get_user():
    return db


def update_user(first, last, email, tlf):
    db.first = first
    db.last = last
    db.email = email
    db.tlf = tlf
    return db
