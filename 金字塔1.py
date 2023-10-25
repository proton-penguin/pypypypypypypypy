r = range(1,int(input("高度幾層？ "))+1);
for i in r:
    print((len(r)-i)*" "+"* "*i)
