import PPF2SExp
from nltk import Tree

def main():
    """
    textとparent pointer formatのtreeを渡すと、nltkで読めるS式を返す
    """
    text1 = "And|that|'s|a|big|part|of|why|we|go|to|the|movies|."
    tree1 = "27|26|24|22|21|21|20|19|18|17|16|15|15|25|16|17|18|19|20|23|22|23|24|25|26|27|0"

    sexp1 = PPF2SExp.convert(text1, tree1)
    print(sexp1)
    t = Tree.fromstring(sexp1)
    t.pretty_print()

    text2 = "The|Rock|is|destined|to|be|the|21st|Century|'s|new|``|Conan|''|and|that|he|'s|going|to|make|a|splash|even|greater|than|Arnold|Schwarzenegger|,|Jean-Claud|Van|Damme|or|Steven|Segal|."
    tree2 = "70|70|68|67|63|62|61|60|58|58|57|56|56|64|65|55|54|53|52|51|49|47|47|46|46|45|40|40|41|39|38|38|43|37|37|69|44|39|42|41|42|43|44|45|50|48|48|49|50|51|52|53|54|55|66|57|59|59|60|61|62|63|64|65|66|67|68|69|71|71|0"
    sexp2 = PPF2SExp.convert(text2, tree2)
    print(sexp2)
    t = Tree.fromstring(sexp2)
    t.pretty_print()

if __name__ == "__main__":
    main()