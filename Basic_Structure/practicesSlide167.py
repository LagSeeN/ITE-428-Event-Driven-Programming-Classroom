flowers = ["Sun flower", "Ivy", "Jusmine", "Lily"]
search = input("Enter flower that you want to search : ")
print('{}'.format(search.lower() in (newList.lower() for newList in flowers)))
