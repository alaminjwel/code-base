# Write a function to find the length of the longest common subsequence between two sequences.
# E.g. Given the strings "serendipitous" and "precipitation", the longest common subsequence is "reipito" and its length is 7.
# A "subsequence" is a sequence obtained by deleting zero or more elements from another sequence.
# For example, "edpt" is a subsequence of "serendipitous".

def lcq_recursive(seq1, seq2, idx1=0, idx2=0):
    if len(seq1)==idx1 or len(seq2)==idx2:
        return 0
    elif seq1[idx1]==seq2[idx2]:
        return 1+lcq_recursive(seq1, seq2, idx1+1,idx2+1)
    else:
        return max(lcq_recursive(seq1, seq2, idx1+1,idx2),lcq_recursive(seq1, seq2, idx1,idx2+1))


def lcq_recursive_memo(seq1, seq2, idx1=0, idx2=0):
    memo = {}

    def helper(idx1=0,idx2=0):
        key = (idx1,idx2)
        if key in memo:
            return memo[key]
        elif len(seq1)==idx1 or len(seq2)==idx2:
            memo[key]=0
        elif seq1[idx1]==seq2[idx2]:
            memo[key] = 1+helper(idx1+1,idx2+1)
        else:
            memo[key] = max(helper(idx1+1,idx2),helper(idx1,idx2+1))
        return memo[key]
    return helper()


# https://medium.com/@kevinmavani/longest-common-subsequence-using-dynamic-programming-641eed90dab1
def lcq_dp(seq1, seq2):
    n1,n2=len(seq1),len(seq2)
    results = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for idx1 in range(n1):
        for idx2 in range(n2):
            if seq1[idx1] == seq2[idx2]:
                results[idx1+1][idx2+1] = 1 + results[idx1][idx2]
            else:
                results[idx1+1][idx2+1] = max(results[idx1][idx2+1],results[idx1+1][idx2])
    return results[-1][-1]



T0 = {
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': 7
}
T1 = {
    'input': {
        'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': 5
}
T2 = {
    'input': {
        'seq1': 'longest',
        'seq2': 'stone'
    },
    'output': 3
}
T3 = {
    'input': {
        'seq1': 'asdfwevad',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}
T4 = {
    'input': {
        'seq1': 'dense',
        'seq2': 'condensed'
    },
    'output': 5
}
T5 = {
    'input': {
        'seq1': '',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}
T6 = {
    'input': {
        'seq1': '',
        'seq2': ''
    },
    'output': 0
}
T7 = {
    'input': {
        'seq1': 'abcdef',
        'seq2': 'badcfe'
    },
    'output': 3
}
lcq_tests = [T0, T1, T2, T3, T4, T5, T6, T7]

i=1
for test in lcq_tests:
    input_data = test['input']
    expected_output = test['output']
    result = lcq_dp(input_data['seq1'], input_data['seq2'])
    passed = result == expected_output
    print("\nTest Case",i," -> ",input_data['seq1'],'*',input_data['seq2'],' = ',result," (",passed,")")
    i+=1