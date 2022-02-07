def main():
    words = ["bob", "mike", "bill"]
    list_a = [word for word in words if word == word[::-1]]
    print(list_a)
if __name__ == "__main__":
    main()
