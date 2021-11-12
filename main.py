import SExp2STree
import PPF2SExp

def main():
    text1 = "And that 's a big part of why we go to the movies ."
    tree1 = "27|26|24|22|21|21|20|19|18|17|16|15|15|25|16|17|18|19|20|23|22|23|24|25|26|27|0"

    sexp = PPF2SExp.convert(text1, tree1)
    SExp2STree.show(sexp)


if __name__ == "__main__":
    main()