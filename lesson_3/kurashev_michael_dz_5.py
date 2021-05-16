import random

def get_jokes(quantity, repeat):
    """
    get_jokes(quantity, repeat)
    Displays the number of jokes. The first argument is for the total number of jokes, and the second turns
    off the ability to repeat jokes
    """
    if repeat == True:
        list_finsh = []
        nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
        adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
        adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        i = 0
        while i < quantity:
            list_joke = [random.choice(nouns), random.choice(adverbs), random.choice(adjectives)]
            a = ' '.join(list_joke)
            list_joke.clear()
            list_finsh.append(a)
            i += 1
        print(list_finsh)
    else:
        list_finsh = []
        nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
        adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
        adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        i = 0
        while i < 5:
            list_joke = []
            nouns_random = random.choice(nouns)
            adverbs_random = random.choice(adverbs)
            adjectives_random = random.choice(adjectives)
            list_joke.append(nouns_random)
            list_joke.append(adverbs_random)
            list_joke.append(adjectives_random)
            itog_list = ' '.join(list_joke)
            list_joke.clear()
            list_finsh.append(itog_list)
            nouns.remove(nouns_random)
            adverbs.remove(adverbs_random)
            adjectives.remove(adjectives_random)
            i += 1
        print(list_finsh)

get_jokes(5, True)