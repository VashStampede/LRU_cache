import random

QUOTES = [
"There's a huge amount of faith and confidence in the stunt team. ...",
"All of the stunt men - these are the unsung heroes. ...",
"Revenge is a caustic thing. ...",
"When I'm getting ready for a movie, let's just say my diet is 'The Antisocial Diet.'",
"High risk is high adrenaline",
"Without music, life would be a mistake.",
"It is not a lack of love, but a lack of friendship that makes unhappy marriages.",
"That which does not kill us makes us stronger.",
"I'm not upset that you lied to me, I'm upset that from now on I can't believe you.",
"And those who were seen dancing were thought to be insane by those who could not hear the music." ,
"There is always some madness in love. But there is also always some reason in madness." ,
]

def get_random_quote():
    return random.choice(QUOTES)

if __name__ == '__main__':
    print(get_random_quote())