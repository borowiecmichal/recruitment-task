
Przygotowanie aplikacji, która na wejściu przyjmie dane w postaci JSON:
{
    "data_list": [
        {"first_name": "Stefan", "second_name": "Nowak", "birth_date":
            "1988-06-18"},
        {"first_name": "Jan", "second_name": "Kowalski", "birth_date":
            "1977-11-10"}
    ]
}


W odpowiedzi pownien zwrocić dane w postaci:


{
    "result": [
        {"first_name": "Jan", "second_name": "Kowalski", "birth_date":
            "1977-11-10", "hash":
             "d371d82da0bcb79c71d8a9d56a5272732f01ed3496887620c6f10ef9fa823e3a"},
        {"first_name": "Stefan", "second_name": "Nowak", "birth_date":
            "1988-06-18", "hash":
             "0720cd55b5faef8f5df5551c965ebf6872669f3aba38d9cf34ee225444f218bd"},
    ]
}


W odpowiedzi dane powinny być posortowane w taki sposób, aby lista 
result zawierała posortowane alfabetycznie rekordy. Sortowanie wg pól 
second_name, first_name. Każdy rekord powinien mieć dodaną daną hash, 
która jest skrótem sha256 z skonkatenowanych danych first_name, 
second_name, birth_date, np:

sha256("JanKowalski1977-11-10") = 
d371d82da0bcb79c71d8a9d56a5272732f01ed3496887620c6f10ef9fa823e3a