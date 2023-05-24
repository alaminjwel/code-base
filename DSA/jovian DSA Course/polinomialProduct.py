def multiply_basic(poly1, poly2):
    len1, len2 = len(poly1), len(poly2)
    if len1 == 0 or len2 == 0:
        return []
    elif poly1 == [0]*(len1) or poly2 == [0]*(len2):
        return [0]
    result = [0]*(len1 + len2 - 1)
    for i in range(len1):
        for j in range(len2):
            result[i+j] += poly1[i]*poly2[j] 

    for i in range(len(result)-1, -1, -1):
        if result[i] != 0:
            actlen = i
            break

    return result[0: actlen+1]


test0 = {
    'input': {
        'poly1': [2, 0, 5, 7],
        'poly2': [3, 4, 2]
    },
    'output': [6, 8, 19, 41, 38, 14]
}
test1 = {
    'input': {
        'poly1': [],
        'poly2': []
    },
    'output': []
}
test2 = {
    'input': {
        'poly1': [0],
        'poly2': [1, 7, 2]
    },
    'output': [0]
}
test3 = {
    'input': {
        'poly1': [3],
        'poly2': [7]
    },
    'output': [21]
}
test4 = {
    'input': {
        'poly1': [0, 0, 4],
        'poly2': [4, 0, 0]
    },
    'output': [0, 0, 16]
}
test5 = {
    'input': {
        'poly1': [1],
        'poly2': [2, 3, 7, 9]
    },
    'output': [2, 3, 7, 9]
}
test6 = {
    'input': {
        'poly1': [],
        'poly2': [2, 3, 7, 9]
    },
    'output': []
}
test7 = {
    'input': {
        'poly1': [7],
        'poly2': [2, 3]
    },
    'output': [14, 21]
}
test8 = {
    'input': {
        'poly1': [2, 3],
        'poly2': [7]
    },
    'output': [14, 21]
}
test9 = {
    'input': {
        'poly1': [7],
        'poly2': [2, 3, 4]
    },
    'output': [14, 21, 28]
}
test10 = {
    'input': {
        'poly1': [7, 3, 4],
        'poly2': [2, 3]
    },
    'output': [14, 27, 17, 12]
}
test11 = {
    'input': {
        'poly1': [7, 3, 4, 5],
        'poly2': [2]
    },
    'output': [14, 6, 8, 10]
}

tests = [test0, test1, test2, test3, test4, test5,test6,test7,test8,test9,test10,test11]
i=1
for test in tests:
    input_data = test['input']
    expected_output = test['output']
    result = multiply_basic(input_data['poly1'], input_data['poly2'])
    passed = result == expected_output
    print("\nTest Case",i," -> ",input_data['poly1'],'*',input_data['poly2'],' = ',result," (",passed,")")
    i+=1