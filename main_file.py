import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.upload import VkUpload
from my_token import TOKEN
import analys
import random



def get_message(text):
    return analys.response(text)

def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, '193289108')

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            upload = VkUpload(vk)
            text, user_id = event.obj.message['text'], event.obj.message['from_id']
            message = get_message(text)
            print(text)
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=message,
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
