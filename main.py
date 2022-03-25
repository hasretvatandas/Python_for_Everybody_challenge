# kitap ve yazarlarinin bulundugu dict
books = {
    "Suç ve Ceza": "Fyodor Dostoyevski", "Sefiller": "Victor Hugo",
    "Anna Karenina": "Lev Tolstoy", "Notre Dame'ın Kamburu": "Victor Hugo"
    }
# while dongusunun kontrolu, sonsuz donguyu kirmak icin
control = True

# butun kitap isimlerini liste olarak donduren fonksiyon
def get_all_book_names():
    book_names = []
    for name, _ in books.items():
        book_names.append(name)
    return book_names

# butun kitap yazarlarini set unique olarak donduren fonksiyon
def get_all_authors():
    authors = []
    for _, author in books.items():
        authors.append(author)
    return set(authors)

# aldigi name parametresine gore kitaplari veya yazarlarini donduren fonksiyon
def display(name):
    global control
    if name == "books":
        for item in get_all_book_names():
            print(item)
        control = False
    elif name == "authors":
        for item in get_all_authors():
            print(item)
        control = False
    else:
        print("Bir secim yapin... [books, authors]")


while True:
    # display fonksiyonuna gonderilen parametre books veya authors ise 
    # control flag false cekilir ve break ile sonsuz donguden cikilir
    if control:
        # display(name="books")
        display(name="authors")
    break
