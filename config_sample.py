WEBHOOK_URL_PATH = '/'  # webhook endpoint
SKILL_ID = '37cbad04-a60fasdfasde-4a9b-833b-1easfasdfasd' # идентификатор навыка
OAUTH_TOKEN = 'OAuth y0_AgAAAAT7owAAAAEFJchFAACL53UQnAhJ_DA4BbRgyDFEnQ' # токен для загрузки музыки в навык как получить см тут 

WEBAPP_HOST = 'localhost' # отсавляем как есть
WEBAPP_PORT = 8080 # порт на который nginx пробрасывает запросы от yandex
TRANSLATE = False # указать True если хотите перед отправкой в Suno переводить свои запросы на английский

MQTT_BROKER = '127.0.0.1' # Адрес MQTT сервера
MQTT_PORT = 1883  # Порт MQTT сервера
MQTT_TOPIC_PLAY = "suno" # Топик для воспроизведения готовых треков
MQTT_TOPIC_TELE = "suno_tele" # Топик для статуса во время генерации
MQTT_CLIENT_ID = f'python-mqtt-suno' # Любой

MQTT_CLIENT = None # Оставляем как есть

# См Reamde.md
SUNO_COOKIE = '_cfuvid=dOhLoTi5iYnqidasb33e0WsejaXv_sX4B2F9_-1715786945876-0.0.1.1-604800000; __client=fsdsgsdfgs.eyJpZCI6ImNsaWVudF8yZ2RIdzhqVWVFSzJDMGdFZFpzbE5TUVZtOUwiLCJyb3RhdGluZ190b2tlbiI6InF3NmZxdDI0cmx1M2hlZzZpa3N1anRocDA0cW5meG44N3p1Y255azkifQ.wCzqVLA1kT-BgkVhoQjUifd0YjY16hDkuszFiW9FH4ufTcg61YSNlQK0tt4XWcYinGEitJlfcAoa1kiDteNQbsRSDptsojO2WK-vhZYk9m66m-SjfSnUSazVYWMO9kFp_4QP0UC4jUyr_ghJl_DRRY628m-SfuZwVU-5XDsNW7CdS3jZXQIfN9lMZ5Todh-HK6MroJ3GEIBq7PD7KAr3SbcH8osdqRkRJo830Cekn-f6VUHsqujTGwtXEc2GBfrgDyteuZeHCaiSlKI8MkXChHIp3GvT3aGYQfSr0ObXa4hLl-I8R8ChJzwiROA3gJsJ9kJ3FHmqE3xQbUbu2BlxgQ; __client_uat=1716020776; __stripe_mid=b77d46b4-9447-4028-8c01-801f3354abd8b505c6; mp_26ced217328f4737497bd6ba6641ca1c_mixpanel=%7B%22distinct_id%22%3A%20%228ef55490-cf15-4b39-94fc-a70e0c627415%22%2C%22%24device_id%22%3A%20%2218f7cdf11d949f-02fc68931e9655-1b525637-2a3000-18f7cdf11d949f%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22%24user_id%22%3A%20%228ef55490-cf15-4b39-94fc-a70e0c627415%22%7D; __cf_bm=c7uFsA0vehnpvsP3kz1fca1X9xeYBRPPWNMnqMzI6sc-1716058387-1.0.1.1-NWpo7LZmMZ20MDOiX8.DawwcwExG_wnaBLkvZ8xfFf7Uv5ao6GRpUDNWcLFhRPq4Z5n7myMZR8i3g'


word_black_list = ['навык','активируй'] 

words_remove = ['придумай песню']