reference = input("Enter a refrence: ")
pattern = input("Enter a pattern: ")
if pattern in reference:
    print(f'{pattern} is in {reference}')
else:
    print(f'{pattern} is not in {reference}')

sRef = set(reference.split())
sPat = set(pattern.split())
# print(sRef, sPat)

if(sPat <= sRef):
    print(f'{sPat} is a subeset of {sRef}')
else:
    print(f'{sPat} is not a subeset of {sRef}')