article = "Musk poured $44 billion into Twitter. The global population is 8 billion people. He could have given $5 billion to each individual and still had money left over. Most people’s lives would be changed if they received a $5 billion check. But he squandered it all on Twitter."
subs = {
    "billion": "sheep",
    "check": "donation",
}
newArticle = article[:]
print(newArticle)
print("")
for w in subs:
    newArticle = newArticle.replace(w, subs[w])
print(newArticle)