given_list = ['Python', 3, 2, 4, 5, 'version']
x= lambda x: isinstance(x, float)
max_value = max(filter(x, given_list))


print("Original list:", given_list)
print("Maximum value in the list using lambda:", max_value)
