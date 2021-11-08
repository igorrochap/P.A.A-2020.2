def highest_lenght_common_substring(string_1, string_2, n, m):
    highest_commom_suffixes = [[0 for i in range(m + 1)] for j in range(n+1)]
    
    highest_lenght = 0

    for i in range(n + 1):
        for j in range(m + 1):
            highest_commom_suffixes[i][j] = 0

            if(string_1[i - 1] == string_2[j - 1]):
                highest_commom_suffixes[i][j] = highest_commom_suffixes[i - 1][j - 1] + 1
                highest_lenght = max(highest_lenght, highest_commom_suffixes[i][j])
                

    return highest_lenght

string_1 = 'this is a:dummystring'
string_2 = 'this is another:dummystring'

print('The highest length of the bigger common substring between the strings is:', highest_lenght_common_substring(string_1, string_2, len(string_1), len(string_2)))