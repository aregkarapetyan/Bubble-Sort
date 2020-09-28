import json

def load_books():
    with open('books.json') as data_file:
        book_list=json.load(data_file)
    return book_list

def make_publication_year_list(publication_year_list,book_list):
    for i in range(len(book_list["books"])):
        publication_year_list.append(book_list["books"][i]["publication_year"])
    return publication_year_list

def selection_sort(publication_year_list):
    max_index=0
    curr_len = len(publication_year_list)
    while curr_len>1:
        for i in range(curr_len):
            if publication_year_list[i]>publication_year_list[max_index]:
                max_index = i
        publication_year_list[max_index], publication_year_list[curr_len - 1]=swap(publication_year_list[max_index],publication_year_list[curr_len - 1])
        curr_len-=1
        max_index=0

def bubble_sort(publication_year_list):
    num_of_passes=1
    while num_of_passes<len(publication_year_list):
        for i in range(len(publication_year_list)-num_of_passes):
            if publication_year_list[i]>publication_year_list[i+1]:
                publication_year_list[i], publication_year_list[i + 1] = swap(publication_year_list[i], publication_year_list[i+1])
                #print(publication_year_list)
        num_of_passes += 1

def insertion_sort(publication_year_list):
    unsort_index = 1 #index of first unsorted element
    for i in range(unsort_index, len(publication_year_list)): #i in unsorted
        if unsort_index != len(publication_year_list):
            for j in range(0,unsort_index):#j in sorted
                if publication_year_list[i]>publication_year_list[j] and publication_year_list[i]<publication_year_list[j+1] or publication_year_list[i]<publication_year_list[j] and publication_year_list[i]>publication_year_list[j-1] and j>0:
                    temp = publication_year_list[i]
                    for k in range(i-1,j,-1):
                        publication_year_list[k+1]=publication_year_list[k]
                    publication_year_list[j+1]=temp
                    unsort_index +=1
                elif publication_year_list[i]<publication_year_list[j]:
                    temp = publication_year_list[i]
                    for k in range(i-1,j-1,-1):
                        publication_year_list[k+1]=publication_year_list[k]
                    publication_year_list[j]=temp
                    unsort_index += 1


def merge_sort(array):
    n = len(array)
    if n==1:
        merged_array = array
        return merged_array
    else:
        array1=[]
        array2=[]
        for i in range(0,int(n/2)):
            array1.append(array[i])
        for i in range(int(n/2),int(n)):
            array2.append(array[i])
        merged_array1 = merge_sort(array1)
        merged_array2 = merge_sort(array2)
        merged_array = merge(merged_array1,merged_array2)
        return merged_array

def merge(array1,array2):
    temp_array=[]
    while len(array1)!=0 and len(array2)!=0:
        if array1[0]>array2[0]:
            temp_array.append(array2[0])
            array2.remove(array2[0])
        else:
            temp_array.append(array1[0])
            array1.remove(array1[0])
    while len(array1)>0:
        temp_array.append(array1[0])
        array1.remove(array1[0])
    while len(array2)>0:
        temp_array.append(array2[0])
        array2.remove(array2[0])
    return temp_array

def quick_sort(publication_year_list):
    pass

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

    publication_year_list = [98,85,49,25,16,2,49,94,92,67,18,52,95,90,85,80,75,70]
    print(publication_year_list)

    # publication_year_list = []
    # book_list = load_books()
    # publication_year_list=make_publication_year_list(publication_year_list,book_list)
    # print(publication_year_list)

    # selection_sort(publication_year_list)
    # print(publication_year_list)
    # print_ordered_books(book_list, publication_year_list)

    # bubble_sort(publication_year_list)
    # print(publication_year_list)
    # print_ordered_books(book_list, publication_year_list)

    # insertion_sort(publication_year_list)
    # print(publication_year_list)
    # print_ordered_books(book_list, publication_year_list)

    # publication_year_list = merge_sort(publication_year_list)
    # print(publication_year_list)
    # print_ordered_books(book_list, publication_year_list)

    quick_sort(publication_year_list)
    print(publication_year_list)
    # print_ordered_books(book_list, publication_year_list)

main()