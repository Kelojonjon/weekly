A very basic console "rehearser helper"

## What it does:
- Add topics to a weekly rotation.
- If you complete the assigned topic during a week you get points (hurray!).
- If the week changes and you havent completed your weekly topic, you will lose points from your score.
- After all the topics in the rotation have been cycled, shuffle the deck and start a new rotation. (Infinite loop!)
- After completing the weekly topic you can freely continue completing more topics adding up to your score!
- For each completed week you will also gather streak points to your "weekly streak" 🔥🔥



## Usage:
- Usage is trough pythons "argparser", install it in you PATH for easy use!
- Contains the following commands:

- show  #Shows a view of the current weeks progress, Also automaticly updates week, score, and your streak 🔥, depending on your "completion" status
- skip  #Skip a topic, doesnt affect your score
- done  #After completing a topic use this to mark it done(hurray!) You will get points, and your weekly progress is now safe!
- reset-score  #Reset your score down to 0
- reset-streak  #Reset your streak down to 0
- reset  #Reset the whole project, and start from a clean template (This is the only way to remove topics from a rotation)
- list  #Show ALL of the topics you have in your rotation
- add  #Add new topics to your rotation.

'show' command is the only command that updates the week, thus destroyuing your streak,
The basic "workflow" is supposed to be bacily a mix of 'show' and 'done'

'add' command allows you to add the topics in 1 batch --> add topic1:topic2:topic3:topic4
If you want to have spaces in your topic names use quotes around your 'add' argument --> add "topic1:the topic2: the topic3:topic of the week:topic4"


## Stuff

- This is a small quick project done in 1 day, for my personal use, except bugs!
- Have fun!
