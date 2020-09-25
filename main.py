import json

def load_books():
    with open('books.json') as data_file:
        book_list=json.load(data_file)
    return book_list

def make_publication_year_list(publication_year_list,book_list):
    for i in range(len(book_list["books"])):
        publication_year_list.append(book_list["books"][i]["publication_year"])
    return publication_year_list

def bubble_sort(publication_year_list):
    for i in range(len(publication_year_list)-1):
        if publication_year_list[i]>publication_year_list[i+1]:
            publication_year_list[i], publication_year_list[i + 1] = swap(publication_year_list[i], publication_year_list[i+1])
            bubble_sort(publication_year_list)

def swap(element1, element2):
    temp = element2
    element2 = element1
    element1 = temp
    return element1, element2

def print_ordered_books(book_list, publication_year_list):
    for i in range(len(publication_year_list)):
        for j in range(len(book_list["books"])):
            if publication_year_list[i] == book_list["books"][j]["publication_year"]:
                print(str(book_list["books"][j]["publication_year"])+ "-" + str(book_list["books"][j]["name"])+" by "+str(book_list["books"][j]["author"]))

def main():
    publication_year_list = []

    book_list = load_books()
    publication_year_list=make_publication_year_list(publication_year_list,book_list)
    print(publication_year_list)

    bubble_sort(publication_year_list)
    print(publication_year_list)
    print_ordered_books(book_list, publication_year_list)

main()
