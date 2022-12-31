
import re

def processReasonList( result_text_in ):
    try:
        result_text = re.sub( r"^[\s\.\:\d]*", "", result_text_in )
        result_arr = re.split( r"\n+\d+[\.\:]*\s*", result_text )
        result_arr = [ re.sub( "[^a-zA-Z]*$", "", result ).lower() for result in result_arr ]
        return result_arr
    except Exception as e:
        error_str = str( e )
        print( "Parsing list results from GPT failed" )
        print( "Raw result:\n" + result_text_in )
        return None
