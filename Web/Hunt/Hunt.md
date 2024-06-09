First, I navigated to the provided website at https://uscybercombine-s4-hunt.chals.io.
Inspecting the HTML of this page reveals part of the flag in the comments. The comment also
tells us to "check in on the bots," which tells me that we need to look at this site's
robots.txt. Navigating to https://uscybercombine-s4-hunt.chals.io/robots.txt reveals the next
part of the flag. From there, we can see that https://uscybercombine-s4-hunt.chals.io/secret-bot-spot
is disallowed by "Humans." After navigating to that URL, we can check the JS source of the page.
At the end of the JS file is a comment with the last part of the flag.

flag: SIVBGR{r1s3_0f_th3_r0b0ts!}
