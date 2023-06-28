def get_powerset(input_set):
    powerset = set()
    elements = list(input_set)
    num_elements = len(elements)
    total_subsets = 2 ** num_elements

    for i in range(total_subsets):
        subset = tuple()
        for j in range(num_elements):
            if (i >> j) % 2 == 1:
                subset += (elements[j],)
        powerset.add(subset)

    return powerset

elements = set()
continue_input = True

while continue_input:
    choice = input("Enter one more element? [Y/N]: ").upper()

    if choice == "Y":
        element = input("Enter the new element in the set: ")
        elements.add(element)
    elif choice == "N":
        continue_input = False
    else:
        print("Invalid choice. Please enter either Y or N.")

powerset = get_powerset(elements)
print("Powerset:", powerset)
