# TODO: Open "movies.txt" in write mode

        # TODO: Ask the user for a favourite movie THREE TIMES. Be efficient in your code.

        # TODO: Write the movie to the file with a newline

# TODO: Let the user know movies have been saved to file

# TODO: Check the file and ensure it worked!

with open("movies.txt", "w") as movies:
    inputlist = []
    for i in range(0, 3):
        inputlist.append(input(f"#{i + 1} Favourite Movie: "))
    movies.write(f"{inputlist[0]}\n{inputlist[1]}\n{inputlist[2]}")

print("Movie Saved\nFile Content:")

with open("movies.txt", "r") as movies:
    print(movies.read())
