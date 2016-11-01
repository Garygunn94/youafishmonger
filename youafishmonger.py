import tweepy
import random
import time

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "5h1z65waHOBHPpAQxsxuQmCuC",
    "consumer_secret"     : "6TgEeYkZ3iVqLs7LlF3vyjetYWveaxiYU4r3u1PrKl6Ut8pCi5",
    "access_token"        : "793395220415123456-KtBcwYqJAjQTlJ42A4PAtY0ee0hPcYS",
    "access_token_secret" : "B8yQGNjVPbJxjSD1EYPoGUJyYwSRWRI1WusyywhbyKdKq" 
    }

  api = get_api(cfg)
  tweet = "@Ross_le_Frost"+" "+generate_insult()
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing


def generate_insult(): 
	a = ['artless', 'bawdy', 'beslubbering', 'bootless', 'churlish', 'cockered', 'clouted', 'craven', 'currish', 'dankish', 'dissembling', 'droning', 'errant', 'fawning', 'fobbing', 'froward', 'frothy', 'gleeking', 'goatish', 'gorbellied', 'impertinent', 'infectious', 'jarring', 'loggerheaded', 'lumpish', 'mammering', 'mangled', 'mewling', 'paunchy', 'pribbling', 'puking', 'puny', 'quailing', 'rank', 'reeky', 'roguish', 'ruttish', 'saucy', 'spleeny', 'spongy', 'surly', 'tottering', 'unmuzzled', 'vain', 'venomed', 'villainous', 'warped', 'wayward', 'weedy', 'yeasty']
	b = ['base-court', 'bat-fowling', 'beef-witted', 'beetle-headed', 'boil-brained', 'clapper-clawed', 'clay-brained', 'common-kissing', 'crook-pated', 'dismal-dreaming', 'dizzy-eyed', 'doghearted', 'dread-bolted', 'earth-vexing', 'elf-skinned', 'fat-kidneyed', 'fen-sucked', 'flap-mouthed', 'fly-bitten', 'folly-fallen', 'fool-born', 'full-gorged', 'guts-griping', 'half-faced', 'hasty-witted', 'hedge-born', 'hell-hated', 'idle-headed', 'ill-breeding', 'ill-nurtured', 'knotty-pated', 'milk-livered', 'motley-minded', 'onion-eyed', 'plume-plucked', 'pottle-deep', 'pox-marked', 'reeling-ripe', 'rough-hewn', 'rude-growing', 'rump-fed', 'shard-borne', 'sheep-biting', 'spur-galled', 'swag-bellied', 'tardy-gaited', 'tickle-brained', 'toad-spotted', 'urchin-snouted', 'weather-bitten']
	c = ['apple-john.', 'baggage.', 'barnacle.', 'bladder.', 'boar-pig.', 'bugbear.', 'bum-bailey.', 'canker-blossom.', 'clack-dish.', 'clotpole.', 'coxcomb.', 'codpiece.', 'death-token.', 'dewberry.', 'flap-dragon.', 'flax-wench.', 'flirt-gill.', 'foot-licker.', 'fustilarian.', 'giglet.', 'gudgeon.', 'haggard.', 'harpy.', 'hedge-pig.', 'horn-beast.', 'hugger-mugger.', 'jolthead.', 'lewdster.', 'lout.', 'maggot-pie.', 'malt-worm.', 'mammet.', 'measle.', 'minnow.', 'miscreant.', 'moldwarp.', 'mumble-news.', 'nut-hook.', 'pigeon-egg.', 'pignut.', 'puttock.', 'pumpion.', 'ratsbane.', 'scut.', 'skainsmate.', 'strumpet.', 'varlet.', 'vassal.', 'whey-face.', 'wagtail.']
	 
	X = random.choice(a)
	Y = random.choice(b)
	Z = random.choice(c)
	 
	insult = X, Y, Z
	prefix1 = 'Thou art a '
	prefix2 = 'Thou art an '
	 
	first = X[0]
	true = ['Yes', 'Y', 'Ye', 'yes', 'y', 'ye', ' Yes', ' Y', ' Ye', ' yes', ' y', ' ye']
	 
	if first in "aeiou":
		returnstr = prefix2 + ', '.join(insult)
	else:
		returnstr = prefix1 + ', '.join(insult)
		
	return returnstr
  
if __name__ == "__main__":
  main()