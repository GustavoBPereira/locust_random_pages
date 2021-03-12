from decouple import config, Csv


class Settings:

    @property
    def verbose(self):
        return config("VERBOSE", default=False, cast=bool)

    @property
    def list_usernames(self):
        return config("LIST_USERNAMES", default="isadoracostela,mariana62,pedro-henrique80,ana-laura80,umoura",
                      cast=Csv())

    @property
    def login_enable(self):
        return config("LOGIN_ENABLE", default=True, cast=bool)

    @property
    def login_url(self):
        return config("LOGIN_URL", default="/login")

    @property
    def logout_url(self):
        return config("LOGOUT_URL", default="/logout")

    @property
    def username_parameter_name(self):
        return config("USERNAME_PARAMETER_NAME", default="username")

    @property
    def password_parameter_name(self):
        return config("PASSWORD_PARAMETER_NAME", default="password")

    @property
    def user_password_default(self):
        return config("USER_PASSWORD_DEFAULT", default="test")
