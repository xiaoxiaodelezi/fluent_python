# alex与charles比较的结果是相等，但alex不是charles
charles = {
    'name': 'Charles L. Dodgson',
    'born': 1832,
    'balance': 950,
}

alex = {
    'name': 'Charles L. Dodgson',
    'born': 1832,
    'balance': 950,
}

print(alex == charles)
print(alex is not charles)