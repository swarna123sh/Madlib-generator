print(" ***** MadLib *****")
import emoji
import random

# list of emojis
emojis=[":monkey_face:",":koala:",":horse:",":elephant:",":turtle:",":tropical_fish:",":camel:",":leopard:",":tiger:"]

# list of adjectives
adj=["adventurous","happy","sad","clever","clumsy","adorable","corageous","excited","jolly"]

# list of verbs
verb=["jumping","dancing","singing","playing","crawling","chasing","crying","juggling","cooking"]
tree=[":palm_tree:",":evergreen_tree:"]
# take name as input and randomly select emoji,verb and adjective
# build a random funny story
for i in range(1,3):
 noun=input("Enter a name: ") 
 emo=random.choice(emojis)
 if i==1:
   part1 = "Today I went to the zoo. I saw  " + random.choice(adj) +" "+ noun + " the " + emoji.emojize(emo) + " , walking around the trees "+emoji.emojize(tree[0]) +emoji.emojize(tree[1]) +" He was "+ random.choice(verb) + " the birds " +emoji.emojize(":bird:") +emoji.emojize(":bird:") +" away."
 if i==2:
   part2= "He suddenly saw a kid feeding peanuts to his best friend  "+ noun+ ",the " +emoji.emojize(emo) +" . "+noun+ " was " + random.choice(adj) +" and kept " + random.choice(verb) +  " the entire day."
print(part1)
print()
print(part2) 


