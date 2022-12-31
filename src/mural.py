
import os
import requests
import json
import re
import random
import math

g_canvas_width  = 9216
g_canvas_height = 6237

g_mural_id            = os.environ[ "MURAL_ID" ]
g_mural_client_id     = os.environ[ "MURAL_CLIENTID" ]
g_mural_client_secret = os.environ[ "MURAL_CLIENTSECRET" ]
g_mural_refresh_token = os.environ[ "MURAL_REFRESHTOKEN" ]

def refreshToken():
    # https://developers.mural.co/public/docs/oauth#authenticate-users-access-token-request 
    url = "https://app.mural.co/api/public/v1/authorization/oauth2/refresh" 
    headers = { "Content-Type" : "application/json", 
                "Accept" : "application/json" } 
    data = json.dumps( { "client_id"     : g_mural_client_id, 
                         "client_secret" : g_mural_client_secret, 
                         "refresh_token" : g_mural_refresh_token, 
                         "grant_type" : "refresh_token" } ) 
    response = requests.request( "POST", url, headers=headers, data=data ) 
    response_json = response.json() 
    if "access_token" not in response_json: 
        print( "'access_token' not found in response from MURAL" ) 
        print( json.dumps( response_json, indent=3 ) ) 
        return None 
    access_token = response_json["access_token"] 
    if re.match( r"\S", access_token ) is None: 
        print( "'access_token' returned from MURAL is empty" ) 
        print( json.dumps( response_json, indent=3 ) ) 
        return None 
    return access_token


def getPositions( num_pos ):
    buffer = 1500
    num_rows = 3
    num_cols = 4
    zone_width = math.floor( g_canvas_width / num_cols )
    zone_height = math.floor( ( g_canvas_height - buffer ) / num_rows )
    zones_arr = []
    for row_num in range( num_rows ):
        top = ( row_num * zone_height ) + buffer
        for col_num in range( num_cols ):
            left = col_num * zone_width
            x = left + random.randint( 0, 400 )
            y = top + random.randint( 0, 400 )
            zones_arr.append( [ x, y ] )
    pos_arr = random.sample( zones_arr,  num_pos )
    return pos_arr


def titleJSON( reason_text, x, y ):
    widget_json = {
        "x"     : x,
        "y"     : y,
        "style" : { "fontSize" : 80 },
        "text"  : "<b>" + reason_text + "</b>"
    }
    return widget_json


def stickyJSON( reason_story, x, y ):
    color = randomColor()
    widget_json = {
        "x"      : x,
        "y"      : y,
        "height" : 500,
        "width"  : 1500,
        "style"  : { "backgroundColor" : color, "fontSize" : 60 },
        "text": reason_story
    }
    return widget_json


def randomColor():
    # Color palette: https://coolors.co/palette/ffc09f-ffee93-fcf5c7-a0ced9-adf7b6
    colors_arr = [ 
        "#FFC09FFF",
        "#FFEE93FF",
        "#FCF5C7FF",
        "#A0CED9FF",
        "#ADF7B6FF"
    ]
    color = random.choice( colors_arr )
    return color


def addWidgetToMural( mural_oauth_token, mural_id, widget_data, widget_type ):
    # https://developers.mural.co/public/reference/createtitle
    # https://developers.mural.co/public/reference/createstickynote
    url = "https://app.mural.co/api/public/v1/murals/" + mural_id + "/widgets/" + widget_type
    headers = { "Content-Type"  : "application/json", 
                "Accept"        : "application/json", 
                "Authorization" : "Bearer " + mural_oauth_token }
    data = json.dumps( widget_data )
    response = requests.request( "POST", url, headers=headers, data=data )
    response_json = json.loads( response.text )
    msg = ""
    if "code" in response_json:
        msg += response_json["code"] + " "
    if "message" in response_json:
        msg += response_json["message"]
    return msg


def addWidgetsToMural( reasons_arr ):
    mural_oauth_token = refreshToken()
    if mural_oauth_token is None:
        return
    pos_arr = getPositions( len( reasons_arr ) )
    for reason_json in reasons_arr:
        x, y = pos_arr.pop()
        title_json  = titleJSON( reason_json["reason"], x, y )
        sticky_json = stickyJSON( reason_json["story"], x, y + 160 )
        error_str1 = addWidgetToMural( mural_oauth_token, g_mural_id, title_json, "title" )
        error_str2 = addWidgetToMural( mural_oauth_token, g_mural_id, sticky_json, "textbox" )
        if error_str1 or error_str2:
            print( "Adding widgets failed" )
            print( "title_json:\n"  + json.dumps( title_json,  indent=2 ) )
            print( "sticky_json:\n" + json.dumps( sticky_json, indent=2 ) )
            print( "MURAL error message:" )
            print( "error_str1: " + error_str1 )
            print( "error_str2: " + error_str2 )
            return
    print( "Done" )
