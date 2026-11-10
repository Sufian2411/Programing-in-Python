def display_resources(resources):
    if len(resources) == 0:
        print("No resources available.")
        return

    for r in resources:
        print("ID:", r[0])
        print("Name:", r[1])
        print("Category:", r[2])
        print("Available Quantity:", r[3])
        print()


def search_by_category(resources, category):
    found = False

    for r in resources:
        if r[2].lower() == category.lower():
            print(r)
            found = True

    if not found:
        print("No resource found in this category.")


def find_unavailable(resources):
    found = False

    for r in resources:
        if r[3] == 0:
            print(r)
            found = True

    if not found:
        print("All resources are available.")


resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]

print("All Resources:")
display_resources(resources)

print("Electronics Resources:")
search_by_category(resources, "Electronics")

print("Unavailable Resources:")
find_unavailable(resources)