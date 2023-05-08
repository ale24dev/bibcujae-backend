def to_dict(self):
    return {
        'username': self.username,
        'first_name': self.first_name,
        'email': self.email,
        'last_login': self.last_login
    }
