prime_dict = {}
number_of_political_parties = int(input("Seçime Giren aday sayısını giriniz: "))

for n in range(number_of_political_parties):
    candidate_name = input("{}.Adayın adını giriniz: ".format(n + 1))
    candidate_vote = int(input("{}.Adayın adlığı oy sayısını giriniz: ".format(n + 1)))
    prime_dict[candidate_name] = candidate_vote
    
total_votes = sum(prime_dict.values())

percentage_dict = {}
for candidate, votes in prime_dict.items():
    percentage = (votes / total_votes) * 100
    percentage_dict[candidate] = percentage

print(percentage_dict)
