import json

def load_books():
    # Loads json file and get the data
    with open('books.json') as data_file:
        book_list=json.load(data_file)
    return book_list

def make_publication_year_list(publication_year_list,book_list):
    # Makes the list of publication years
    for i in range(len(book_list["books"])):
        publication_year_list.append(book_list["books"][i]["publication_year"])
    return publication_year_list

def make_publication_year_linked_list(publication_year_list):
    # Makes the linked list of publication years
    Publication_Year_Linked_List = SLinkedList()
    for i in range(len(publication_year_list)):
        Publication_Year_Linked_List.AtEnd(publication_year_list[i])
    return Publication_Year_Linked_List

def selection_sort(publication_year_list):
    # Sorts the publication years using selection sort algorithm
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
    # Sorts the publication years using bubble sort algorithm
    num_of_passes=1
    while num_of_passes<len(publication_year_list):
        for i in range(len(publication_year_list)-num_of_passes):
            if publication_year_list[i]>publication_year_list[i+1]:
                publication_year_list[i], publication_year_list[i + 1] = swap(publication_year_list[i], publication_year_list[i+1])
                #print(publication_year_list)
        num_of_passes += 1

def insertion_sort(publication_year_list):
    # Sorts the publication years using insertion sort algorithm
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
    # Sorts the publication years using merge sort algorithm
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
    # Merges 2 arrays from merge sort algorithm
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
    # Sorts the publication years using quick sort algorithm
    pass

def swap(element1, element2):
    # Swaps 2 given elements
    temp = element2
    element2 = element1
    element1 = temp
    return element1, element2

def print_ordered_books(book_list, publication_year_list):
    # Prints publication year list in a readable format
    for i in range(len(publication_year_list)):
        for j in range(len(book_list["books"])):
            if publication_year_list[i] == book_list["books"][j]["publication_year"]:
                print(str(book_list["books"][j]["publication_year"])+ "-" + str(book_list["books"][j]["name"])+" by "+str(book_list["books"][j]["author"]))

class Node:
    # Class to create nodes for linked list
    def __init__(self,DataVal=None):
        self.DataVal = DataVal
        self.NextVal = None

class SLinkedList:
    #Class to create linked list
    def __init__(self):
        self.HeadVal = None

    def ListPrint(self):
        # Prints the linked list
        PrintVal = self.HeadVal
        while PrintVal is not None:
            print(PrintVal.DataVal)
            PrintVal = PrintVal.NextVal

    def AtBeginning(self,NewData):
        # Adds new elements at the beginning of the linked list
        NewNode = Node(NewData)
        NewNode.NextVal = self.HeadVal
        self.HeadVal = NewNode

    def AtEnd(self,NewData):
        # Adds new elements at the end of the linked list
        NewNode = Node(NewData)
        if self.HeadVal is None:
            self.HeadVal = NewNode
            return
        LastElem = self.HeadVal
        while(LastElem.NextVal is not None):
            LastElem = LastElem.NextVal
        LastElem.NextVal=NewNode

    def InBetween(self,middle_node,NewData):
        # Adds new elements in the middle of the linked list, given the middle node
        if middle_node is None:
            print("Error. Mentioned node is absent")
            return
        NewNode = Node(NewData)
        NewNode.NextVal = middle_node.NextVal
        middle_node.NextVal = NewNode

    def RemoveNode(self, RemoveKey):
        # Removes an elements from linked list using the provided remove key
        HeadVal = self.HeadVal

        if HeadVal is not None:
            if HeadVal.DataVal == RemoveKey:
                self.head = HeadVal.NextVal
                HeadVal = None
                return
        while HeadVal is not None:
            if HeadVal.DataVal == RemoveKey:
                break
            prev = HeadVal
            HeadVal = HeadVal.NextVal
        if HeadVal == None:
            return
        prev.NextVal = HeadVal.NextVal

        HeadVal = None

def main():
    # List of numbers to test the sorting algorithms
    # publication_year_list = [98,85,49,25,16,2,49,94,92,67,18,52,95,90,85,80,75,70]
    # print(publication_year_list)


    publication_year_list = []

    #       Load the json file
    book_list = load_books()

    #       Create the list with publication years
    publication_year_list=make_publication_year_list(publication_year_list,book_list)
    print(publication_year_list)

    #       Creates linked list from the given array(publication years)
    Publication_Year_Linked_List = make_publication_year_linked_list(publication_year_list)

    #       Prints the linked list with publication years
    Publication_Year_Linked_List.ListPrint()

    #       Conducts selection sort algorithm on publication year list
    # selection_sort(publication_year_list)
    # print(publication_year_list)
    # print_ordered_books(book_list, publication_year_list)

    #       Conducts bubble sort algorithm on publication year list
    # bubble_sort(publication_year_list)
    # print(publication_year_list)
    # print_ordered_books(book_list, publication_year_list)

    #       Conducts insertion sort algorithm on publication year list
    # insertion_sort(publication_year_list)
    # print(publication_year_list)
    # print_ordered_books(book_list, publication_year_list)

    #       Conducts merge sort algorithm on publication year list
    # publication_year_list = merge_sort(publication_year_list)
    # print(publication_year_list)
    # print_ordered_books(book_list, publication_year_list)

    #       Conducts quick sort algorithm on publication year list
    #       ---------------------IN PROGRESS----------------------
    # quick_sort(publication_year_list)
    # print(publication_year_list)
    # print_ordered_books(book_list, publication_year_list)

    #       Check how linked list works
    # List_L = SLinkedList()
    # List_L.AtBeginning("Mon")
    # List_L.AtBeginning("Tue")
    # List_L.AtBeginning("Wed")
    # List_L.AtBeginning("Thu")
    # List_L.AtBeginning("Fri")
    # List_L.RemoveNode("Wed")
    # List_L.ListPrint()

main()