movies = [
    {
            'name': 'Three idiots', 'director':'idk'
    },
    {
            'name': 'idiots', 'director':'Rajesh'
        },
    {
            'name': 'Extraction', 'director':'Ram'
        },
    {
            'name': 'Nepal', 'director':'Kp-oli'
        },
    {
            'name': 'India', 'director':'Modi-bhai'
        }
]


find_by= input("Enter the property we are searching the movie by = ")
looking_for = input("What are you looking for ? : ")

def find_movie(looking_for, finder):
    for movie in movies:
        if finder(movie)==looking_for:
            return movie


movie =find_movie(looking_for, lambda movie: movie[find_by])

print(movie or "The movie you search for doesn't exist in our database")


