from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Implication(AKnave, Not(And(AKnight, AKnave))), Implication(
        AKnight, And(AKnight, AKnave)), Or(AKnight, AKnave)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Implication(AKnave, Not(And(AKnave, BKnave))), Implication(
        AKnight, And(AKnave, BKnave)), Or(AKnight, AKnave), Or(BKnave, BKnight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))), Implication(
        AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))), Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))), Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight)))), Or(AKnave, AKnight), Or(BKnave, BKnight)

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Implication(BKnight, And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))), Implication(
        BKnave, Not(And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnight))))),
    Implication(BKnight, CKnave), Implication(BKnave, Not(CKnave)), Implication(
        CKnight, AKnight), Implication(CKnave, Not(AKnight)), Or(AKnight, AKnave), Or(BKnave, BKnight), Or(CKnave, CKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
