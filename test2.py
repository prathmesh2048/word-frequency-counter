import requests 
from bs4 import BeautifulSoup 
import operator 
from collections import Counter 

def start(url): 


	wordlist = [] 
	source_code = requests.get(url).content

	soup = BeautifulSoup(source_code, 'html.parser') 


	for each_text in soup.findAll('div'): 
		content = each_text.text 

		# use split() to break the sentence into 
		# words and convert them into lowercase 
		words = content.lower().split() 
		
		for each_word in words: 
			wordlist.append(each_word) 
	
	clean_list =[] 
	for word in wordlist: 
		symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
		
		for i in range (0, len(symbols)): 
			word = word.replace(symbols[i], '') 
			
		if len(word) > 0: 
			clean_list.append(word)

	word_count = {} 
	
	common_english_word = ['the','be','to','of','and','a','in','that','have','is','it','for','not','on','with','he','as','you','do','at','this','but','his','by','from','they','are','can','her','she',]

	for word in clean_list: 
		if word in word_count: 
			word_count[word] += 1
		else: 
			word_count[word] = 1

	for common in common_english_word:
		if common in word_count:
			del word_count[common]


	c = Counter(word_count) 

	top = c.most_common(10) 
	return top

result = start("https://xenneotech.com/blog/indication-upgrade.html") 
print(result[0][1])
