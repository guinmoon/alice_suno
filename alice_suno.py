from aiohttp import web
import asyncio
from paho.mqtt import client as mqtt_client
from threading import Thread
from time import sleep

from aioalice import Dispatcher, get_new_configured_app
from translate import *
from config import *
from mqtt import *
from suno_gen import *


dp = Dispatcher()



@dp.request_handler()
async def handle_all_requests(alice_request):
    response = 'Привет я Суно, какую песню мне придумать?'
    if alice_request.request.command == '':
        return alice_request.response(response)
    for word in word_black_list:
        if word in alice_request.request.nlu.tokens:
            return alice_request.response(response)
    command = alice_request.request.command 
    for word in words_remove:
        command.replace(word,"")
    try:
        print(command)
        i18n_command = command
        if TRANSLATE:
            i18n_command = translate(command,to_language="en")
             
        th = Thread(target=suno_generate_song,args=[i18n_command],daemon=False)
        th.start()
        
        response = "Придумываю песню "+i18n_command
    except Exception as ee:
        print(ee)
    return alice_request.response(response)


def suno_gen_callbakc(message):
    print(message)
    mqtt_pub(message,mqtt_topic=MQTT_TOPIC_TELE)

def suno_generate_song(query):
    try:
        songs = suno_gen(query,suno_gen_callbakc)
        if songs is not None and len(songs)>0:
            upload_sound_sync(songs[0])
        else:
            print("Error generating songs")
    except Exception as ee:
        print(ee)
    

async def upload_some_sounds(sound_path):
    try:
        uploaded_sound = await dp.upload_sound(open(sound_path, 'rb'),skill_id=SKILL_ID, oauth_token=OAUTH_TOKEN)
        # origUrl will be `None`
        sleep(2)
        mqtt_pub(f'<speaker audio="dialogs-upload/{uploaded_sound.skillId}/{uploaded_sound.id}.opus">',mqtt_topic=MQTT_TOPIC_PLAY)
        print(uploaded_sound)
        await dp.close()
    except Exception as ee:
        print(f'Oops! Error uploading sound by bytes {ee}')                
    

def upload_sound_sync(sound_path):
    async def asyncfunc():
        await upload_some_sounds(sound_path)
        # tasks = [dp.loop.create_task(upload_some_sounds(sound_path))]    
        # wait_tasks = await asyncio.wait(tasks,dp.loop)    
    # asyncio.run(asyncfunc())
    asyncio.run_coroutine_threadsafe(asyncfunc(), dp.loop)
    # tasks = [dp.loop.create_task(upload_some_sounds(sound_path))]    
    # wait_tasks = asyncio.wait(tasks)

if __name__ == '__main__':    
    app = get_new_configured_app(dispatcher=dp, path=WEBHOOK_URL_PATH)
    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT, loop=dp.loop)
          

