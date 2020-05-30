List = []
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)
List.remove(2)
print("\nList after Removal of two elements: ")
print(List)
List.pop(5)
print("\nList after popping a specific element: ")
print(List)
Sliced_List = List[1:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_List)