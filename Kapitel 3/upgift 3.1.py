import math

minuter_per_månad = int(input("hur många minuter per månad ringer du?: "))
kostnad_per_minut = int(input("hur många kr per minut?: "))

total_kostnad = kostnad_per_minut*minuter_per_månad 

if total_kostnad >= 300:
    print(f'det kostar {total_kostnad * 0.90} per månad')
else:
    print(f'det kostar {total_kostnad} per månad')