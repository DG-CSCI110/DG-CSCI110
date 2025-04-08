#-------------------------------------------------------------------------------
# Name:        Chapter 8
# Purpose:     Section 8.19 Problem 5
#
# Author:      DylanG
#
# Created:     04/05/2025
# Copyright:   (c) DylanG 2025
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import string

cuil_theory = """
Let cuil be a unit of measurement

One Cuil = One level of abstraction away from the reality of a situation.

Example: You ask me for a Hamburger.

1 Cuil: if you asked me for a hamburger, and I gave you a raccoon.

2 Cuils: If you asked me for a hamburger, but it turns out I don't really exist. Where I was originally standing, a picture of a hamburger rests on the ground.

3 Cuils: You awake as a hamburger. You start screaming only to have special sauce fly from your lips. The world is in sepia.

4 Cuils: Why are we speaking German? A mime cries softly as he cradles a young cow. Your grandfather stares at you as the cow falls apart into patties. You look
down only to see me with pickles for eyes, I am singing the song that gives birth to the universe.

And so on.

5 Cuils: You ask for a hamburger, I give you a hamburger. You raise it to your lips and take a bite. Your eye twitches involuntarily. Across the street a father of
three falls down the stairs. You swallow and look down at the hamburger in your hands. I give you a hamburger. You swallow and look down at the hamburger in your
hands. You cannot swallow. There are children at the top of the stairs. A pickle shifts uneasily under the bun. I give you a hamburger. You look at my face, and I
am pleading with you. The children are crying now. You raise the hamburger to your lips, tears stream down your face as you take a bite. I give you a hamburger. You
are on your knees. You plead with me to go across the street. I hear only children's laughter. I give you a hamburger. You are screaming as you fall down the stairs.
I am your child. You cannot see anything. You take a bite of the hamburger. The concrete rushes up to meet you. You awake with a start in your own bed. Your eye
twitches involuntarily. I give you a hamburger. As you kill me, I do not make a sound. I give you a hamburger.

6 Cuils: You ask me for a hamburger. My attempt to reciprocate is cut brutally short as my body experiences a sudden lack of electrons. Across a variety of
hidden dimensions you are dismayed. John Lennon hands me an apple, but it slips through my fingers. I am reborn as an ocelot. You disapprove. A crack echoes
through the universe in defiance of conventional physics as cosmological background noise shifts from randomness to a perfect A Flat. Children everywhere stop what
they are doing and hum along in perfect pitch with the background radiation. Birds fall from the sky as the sun engulfs the earth. You hesitate momentarily before
allowing yourself to assume the locus of all knowledge. Entropy crumbles as you peruse the information contained within the universe. A small library in Phoenix
ceases to exist. You stumble under the weight of everythingness, Your mouth opens up to cry out, and collapses around your body before blinking you out of the
spatial plane. You exist only within the fourth dimension. The fountainhead of all knowledge rolls along the ground and collides with a small dog. My head tastes
sideways as spacetime is reestablished, you blink back into the corporeal world disoriented, only for me to hand you a hamburger as my body collapses under the
strain of reconstitution. The universe has reasserted itself. A particular small dog is fed steak for the rest of its natural life. You die in a freak accident
moments later, and you soul works at the returns desk for the Phoenix library. You disapprove. Your disapproval sends ripples through the inter-dimensional void
between life and death. A small child begins to cry as he walks toward the stairway where his father stands.

7 Cuils: I give you a hamburger. The universe is engulfed within itself. A bus advertising hotdogs drives by a papillon. It disapproves. An unnatural force reverses
Earth's gravity. You ask for a hamburger. I reciprocate with a mildly convulsing potato. You disapprove. Your disapproval releases a cosmic shift in the void
between birth and life. You ask for a hamburger. A certain small dog feasts on hamburger patties for the rest of its unnatural, eternal endurance. Your constant
disapproval sends silence through everything. A contrived beast becomes omnipotent. You ask for a hamburger. I give you a hamburger your body becomes an unsettled
blob of nothingness, then divides by three. The papillon barks. The universe realigns itself. You, the papillon, and the hamburger disapprove. This condemnation
stops the realignment. Hades freezes over. A pig is launched into the unoccupied existence between space and time with a specific hamburger. You ask for a hamburger.
I give you a hamburger. It screams as you lift it to your face. You laugh maniacally as I plead with you. You devour the hamburger as it pleads for mercy. I
disapprove and condemn you to an eternity in a certain void where a certain pig and its specific hamburger are located. The Universal Space-time Continuum Committee
disapproves of my irrational decision. You are locked away and are fed hamburgers for the rest of your natural existence. A pickle refuses to break down during the
process of digestion. You die in a freak accident. A certain pickle lives the rest of its life in a comatose state. Your soul disapproves. Down the street a child
cries as a hamburger gets stuck in, and climbs back up, her esophagus. You ask again for a hamburger. I refuse to reciprocate. You demand a lawyer. I remind you
harshly that this is the new world order. Lawyers no longer exist. Only papillons. Your name is written on a list of sins. Blasphemy. You ask for a hamburger. The
comatose pickle vanquishes your soul from this universe. Realignment occurs. You beg for a hamburger. A certain papillon's name is written on an obelisk in Egypt.
Mumble. Peasants worship the obelisk. Your soulless corpse partakes in the festivity. Hamburgers are banned universally. The sun implodes. All planets cease to have
ever existed. Mercury. Venus. Earth. Mars. Jupiter. Saturn. Uranus. Neptune. Pluto is the only mass in existence. Conveniently, you are on vacation here. Your need
for hamburgers re-establishes space-time. Earth is recreated under your intergalactic rule. Hamburgers are your army. You wake up. Clowns. Clowns everywhere. Your
dream rushes to meet you. You are kidnapped. You ask for a hamburger. They hand you a hotdog. """

def count_e(text):
    count = 0
    for c in text:
        if c.lower() == "e":
            count += 1
    return count

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

def main():
    cleaned_text = remove_punctuation(cuil_theory)
    word_list = cleaned_text.split()
    total_words = len(word_list)
    e_count = count_e(cleaned_text)
    percent = (e_count / total_words) * 100 if total_words else 0

    print(f"Your text contains {total_words} words, of which {e_count} ({percent:.2f}%) contain an 'e'.")

if __name__ == '__main__':
    main()