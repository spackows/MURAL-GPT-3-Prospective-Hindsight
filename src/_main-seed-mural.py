
from sendPrompt import sendPrompt
from processReasonList import processReasonList
from processFailStory import processFailStory
from mural import addWidgetsToMural

prompt_txt = "List 10 ways a lemonade stand might fail.  Be succinct."
result_txt = sendPrompt( prompt_txt, 100 )
reason_arr = processReasonList( result_txt )

reasons_arr = []
for reason_text in reason_arr:
    prompt_txt = "In 100 words or less, describe how our lemonade stand failed because of: " + reason_text
    result_txt = sendPrompt( prompt_txt, 160 )
    story_txt = processFailStory( result_txt )
    reasons_arr.append( { "reason" : reason_text.title(), "story" : story_txt } )

addWidgetsToMural( reasons_arr )




