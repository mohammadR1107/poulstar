movie_name={"name":"breaking bad","director":"vins giligan","year of manufactor":"2008","chapter":"5"}
new_game = {}
key = input("enter the key")
value = input("enter the value")
new_game[key] = value
print(new_game)

del movie_name["name"]
movie_name.pop("director")
print(movie_name)

# ctrl + /    کامنت کردن همه


print(movie_name["name"])


movie_name["acter"] = "waltrer whait"

print("\n")
print(movie_name)


print("\n")
print(movie_name.keys())
print(movie_name.values())

print("\n")


acter2 = input("enter name the acter2:  ")
movie_name["acter2"]  = acter2
print(movie_name)