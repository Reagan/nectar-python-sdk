class User:

    def __init__(self, first_name=None, last_name=None,
                 username=None, password=None,
                 phone_no=None, image_url=None, ref=None, email=None,
                 activated=None, created_at=None):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.phone_no = phone_no
        self.image_url = image_url
        self.ref = ref
        self.email = email
        self.activated = activated
        self.created_at = created_at

