import os

RULE_SATISFYING_STRING: str="aA123!?$"

def get_env_var(env_var):
    try:
        return os.environ[env_var]
    except KeyError:
        raise Exception(f"{env_var} does not exist")