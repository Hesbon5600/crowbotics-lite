import environ


class EnvNoDefaultException(Exception):
    pass


class CrowdboticsEnv(environ.Env):
    """
    Enforces the optional default param for Env() without modifying the entire class.
    """

    def get_value(
        self, var, cast=None, default=environ.Env.NOTSET, parse_default=False
    ):
        if default == self.NOTSET:
            raise EnvNoDefaultException(
                f"'{var}' does not have a default set, please set a default value"
            )
        return super().get_value(
            var, cast=cast, default=default, parse_default=parse_default
        )
