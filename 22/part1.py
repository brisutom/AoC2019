def deal_new(deck):
    deck.reverse()
    return deck


def cut_deck(deck, n):
    cut, rest = deck[:n], deck[n:]
    return rest + cut


def deal_inc(deck, n):
    new_deck = len(deck)*[-1]
    pos = 0
    while deck:
        card = deck.pop(0)
        new_deck[pos] = card
        pos = (pos + n) % len(new_deck)
    return new_deck


instructions = [str(x).strip("\n") for x in open("input.txt").readlines()]
deck = list(range(0, 10007))
for instr in instructions:
    instr = instr.split(" ")
    if instr[0] == "deal":
        if instr[1] == "with":
            deck = deal_inc(deck, int(instr[-1]))
        elif instr[1] == "into":
            deck = deal_new(deck)
    elif instr[0] == "cut":
        deck = cut_deck(deck, int(instr[-1]))
print(deck)
print(deck.index(2019))
