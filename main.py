from stats import get_book_text
from stats import letter
from stats import fmlsort
import sys

def main ():
    lenght = len(sys.argv)
    if lenght != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    location = sys.argv[1]
    mess = get_book_text(location)
    text = letter(location)
    lisst = fmlsort(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {location}...")
    print("----------- Word Count ----------")
    print(f"Found {mess} total words")
    print("--------- Character Count -------")
    for i in lisst: 
        
        print(f"{i["char"]}: {i["num"]}")
  
    print("============= END ===============")


main()