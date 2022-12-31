
<table>
<tr><th>File</th><th>Description</th></tr>
<tr>
<td valign="top"><code>test-GPT-list.py</code></td>
<td>Quick test of sending a prompt to GPT-3 using the OpenAI API to list possible reasons our lemonade stand might fail</td>
</tr>
<tr>
<td valign="top"><code>test-GPT-story.py</code></td>
<td>Quick test of sending a prompt to GPT-3 using the OpenAI API to tell a short story about how our lemonade stand failed because of "bad location"</td>
</tr>
<tr>
<td valign="top"><code>_main-seed-mural.py</code></td>
<td>Main file for generating a list of failure reasons, fleshing each reason out with a story, and then uploading widets to MURAL</td>
</tr>
<tr>
<td valign="top"><code>sendPrompt.py</code></td>
<td>Contains the routine used by _main to send a prompt to the GPT model using the OpenAI API</td>
</tr>
<tr>
<td valign="top"><code>processReasonList.py</code></td>
<td>Contains the function used by _main to post-process the list of failure reasons returned from the GPT model</td>
</tr>
<tr>
<td valign="top"><code>processFailStory.py</code></td>
<td>Contains the function used by _main to post-process the failure story returned from the GPT model</td>
</tr>
<tr>
<td valign="top"><code>mural.py</code></td>
<td>Contains the routine used by _main to upload widgets to MURAL using the MURAL API</td>
</tr>
</table>
