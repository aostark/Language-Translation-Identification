from ibm_watson import LanguageTranslatorV3, TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

api_key = "-EBxndnIM4Q2B0l99sgMXsi_hQ5sncktNwK8yX5gLcK3"
url = "https://api.us-south.language-translator.watson.cloud.ibm.com/instances/e0bdea00-e496-45c7-9e26-c891407c0b3c"

authenticator = IAMAuthenticator(api_key)
lt = LanguageTranslatorV3(version="2018-05-01", authenticator=authenticator)
lt.set_service_url(url)

# Translate ===>

translation = lt.translate(
    text="Wise men speak because they have something to say; fools because they have to say something",
    model_id="en-ru").get_result()
final_translation = (translation['translations'][0]['translation'])
# print(final_translation)

# Identify (19-24)===>

# language = lt.identify("We buy things we don't need, to impress people we don't like").get_result()
# for value in language:
#     for elem in language.keys():
#         print(language[elem][0])

##################################
# AI Travel Guide ===>

tts_api_key = "6EOfK8hFjc8uZzofSJh2Ya7ibDmJPIm_4yQASppae_MX"
tts_url = "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/0eafde27-27a9-4e8f-b92b-d064ee2a43db"

tts_authenticator = IAMAuthenticator(tts_api_key)
tts = TextToSpeechV1(authenticator=tts_authenticator)
tts.set_service_url(tts_url)

translation = lt.translate(text='Everything you can imagine is real', model_id="en-de").get_result()
text = translation["translations"][0]["translation"]
print(text)

with open("./help.mp3", "wb") as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice="de-DE_BirgitV3Voice").get_result()
    audio_file.write(res.content)