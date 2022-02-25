class Config:
    def __init__(self, env):
        self.base_url = {
            'dev': 'http://www.fidelitasplayground.xyz',
            'qa': 'http://www.fidelitasplayground.xyz/my-account'
        }[env]
