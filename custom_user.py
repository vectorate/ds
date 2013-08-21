class UserManager(BaseUserManager):
"""
    create a new user

    @param username:  the name for the new user
    @param password:  the password for the new user. if none is provided a random password is generated
    @param person:    the corresponding person object for this user
"""
def create_user(self, username, person, password=None):
    if not username:
        raise ValueError('User must have a valid username')

    user = self.model(username=username, created=datetime.now(), must_change_password=True, deleted=False, person=person)

    user.set_password(password)
    user.save(using=self._db)
    return user

class User(AbstractBaseUser):
    ## the id of the user. unique through the application
    user_id     =   models.AutoField(primary_key=True)
    ## the name of the user. unique through the application
    username    =   models.CharField(max_length=32, unique=True)
    ## the date when the user was created
    created     =   models.DateTimeField()
    ## iff this is true the user must set a new password at next login
    must_change_password    =   models.BooleanField(default=True)
    ## iff true the user is marked as deleted and can not login
    deleted     =   models.BooleanField(default=False)
    ## iff true the user is admin and has all permissions. use with care!
    is_admin = models.BooleanField(default=False)
    ## reference to the person entity that is linked to this specific user
    person      =   models.ForeignKey(Person)
    ## indicates if the user is active or not
    active    =    models.BooleanField(default=True)

    ## define the user manager class for User
    objects     =   UserManager()

    # necessary to use the django authentication framework: this field is used as username
    USERNAME_FIELD  =   'username'