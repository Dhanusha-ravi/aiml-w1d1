#VARIABLE & TYPES
name='Cynaris AI Intern'           #string
batch=2026                         #integer                                         
accuracy=0.947                     #float
print(f'Welcome,{name}|Batch:{batch}|Model Accuracy:{accuracy:.1%}')

#LISTS & SLICING
scores=[85,92,78,95,88,76,91]

print(f'All scores: {scores}')
print(f'Top 3: {sorted(scores,reverse=True)[:3]}')
print(f'Average:  {sum(scores)/len(scores):.2f}')

#DICTIONARY
student={
    'name':'priya',
    'week':1,
    'complete':True
}
for key,values in student.items():
    print(f'{key}:{values}')

#NORMALIZE A LIST(A CORE ML OPERATION)
def normalize(data):
    lo,hi=min(data),max(data)
    return[(x-lo)/(hi-lo)for x in data]
print('normalize scores:',[round(v,2)for v in normalize(scores)])