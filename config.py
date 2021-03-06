from collections import namedtuple

# These 3 will go in environment variables later, this works with heroku:
#https://devcenter.heroku.com/articles/config-vars
appkey = '2c987384b72778026687'   
secret = '8440acd6ba1e0bfec3d4'
connected_channel = 'presence-moodies'

Server = namedtuple('Server', 'user sleeptime mood_decrease_rate')
server = Server(
    user = {
        'user_id': 'moodies-server',
        'user_info': {
            'name': 'Moodies Server'
        }
    },
    sleeptime = 30,
    mood_decrease_rate = 1
)


