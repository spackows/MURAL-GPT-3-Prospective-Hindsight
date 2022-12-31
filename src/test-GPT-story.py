
import os
import requests
import json

def sendPrompt( prompt_txt ):
    # https://beta.openai.com/docs/api-reference/completions/create
    url = "https://api.openai.com/v1/completions"
    headers = { "Content-Type" : "application/json", "Authorization" : "Bearer " + os.environ[ "OPENAI_APIKEY" ] }
    data = json.dumps( { "model" : "text-davinci-003", "prompt" : prompt_txt, "max_tokens" : 150 } )
    response = requests.request( "POST", url, headers=headers, data=data )
    print( json.dumps( response.json(), indent=3 ) )


g_prompt_txt = """
In 100 words or less, describe how our lemonade 
stand failed because of: bad location
"""

sendPrompt( g_prompt_txt )