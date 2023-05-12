party_dict = {}
number_of_political_parties = int(input("Seçime Giren parti sayısını giriniz: "))

for n in range(number_of_political_parties):
    party_name = input("{}.Partinin adını giriniz: ".format(n + 1))
    party_vote = int(input("{}.Partinin adlığı oy sayısını giriniz: ".format(n + 1)))
    party_dict[party_name] = party_vote

print(party_dict)


debuts = {}
while True:
    max_vote = max(party_dict.values())
    max_vote_party = max(party_dict, key=party_dict.get)
    max_vote_index = list(party_dict.keys()).index(max_vote_party)

    if max_vote_party not in debuts:
        debuts[max_vote_party] = 0

    debuts[max_vote_party] += 1

    if max_vote > 1:  
        party_dict[max_vote_party] //= 2
    else:
        break

print(debuts)


