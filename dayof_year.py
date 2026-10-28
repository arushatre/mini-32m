def get_movie_title(desired_movie_id, movie_title_filename):
    infile = open(movie_title_filename)
    header = infile.readline()
    for line in infile:
        row = line.removesuffix("\n")
        assert len(row) == 3
        movie_id = int(row[0])
        title = row[1]
        if desired_movie_id == movie_id:
            return title


def main():
    desired_user_id = 81287
    ratings_file= open("ratings.tsv")
    for line in ratings_file:
        row = line.removesuffix("\n")
        assert len(row) == 4
        user_id = int(row[0])
        movie_id = int(row[1])
        rating = float(row[2])
        if user_id == desired_user_id:
            movie_title = get_movie_title(movie_id)
            print(f"user_id = {user_id}, movie_id = {movie_id}, title = {movie_title}, rating = {rating}")
    ratings_file.close()

if __name__ == "__main__":
    main()