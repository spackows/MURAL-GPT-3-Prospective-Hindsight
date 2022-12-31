
import re

def processFailStory( result_text_in ):
    try:
        result_text = re.sub( r"^\s*", "", result_text_in )
        result_text = re.sub( r"\s*$", "", result_text )
        result_text = re.sub( r"\s+", " ", result_text )
        return result_text
    except Exception as e:
        error_str = str( e )
        print( "Parsing results from GPT failed" )
        print( "Raw result:\n" + result_text_in )
        return None
