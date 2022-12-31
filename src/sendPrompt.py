
import os
import requests
import json

g_openai_apikey = os.environ[ "OPENAI_APIKEY" ]

def sendPrompt( prompt_txt, max_tokens ):
    # https://beta.openai.com/docs/api-reference/completions/create
    url = "https://api.openai.com/v1/completions"
    headers = { "Content-Type"  : "application/json", 
                "Authorization" : "Bearer " + g_openai_apikey 
              }
    data = json.dumps( { "model"      : "text-davinci-003",
                         "prompt"     : prompt_txt,
                         "max_tokens" : max_tokens
                       } )
    response = requests.request( "POST", url, headers=headers, data=data )
    response_json = json.loads( response.text )
    print( json.dumps( response_json, indent=3 ) )
    if( "choices" not in response_json ):
        print( "Field 'choices' not found in results from GPT:" )
        print( json.dumps( response_json, indent=3 ) )
        return None
    if( len( response_json["choices"] ) < 1 ):
        print( "No results returned by GPT:" )
        print( json.dumps( response_json, indent=3 ) )
        return None
    if( "text" not in response_json["choices"][0] ):
        print( "Field 'text' not found in results from GPT:" )
        print( json.dumps( response_json, indent=3 ) )
    result_text = response_json["choices"][0]["text"]
    return result_text

