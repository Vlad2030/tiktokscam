from environs import Env

env = Env()
env.read_env()

TOKEN: str = env.str("API_TOKEN")
