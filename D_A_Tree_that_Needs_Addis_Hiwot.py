import sys
input = sys.stdin.read

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve():
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        q = int(data[index + 1])
        index += 2
        a = data[index]
        b = data[index + 1]
        index += 2

        # Initialize count arrays
        cntA = [[0] * (n + 1) for _ in range(26)]
        cntB = [[0] * (n + 1) for _ in range(26)]

        # Fill count arrays
        for i in range(n):
            for j in range(26):
                cntA[j][i + 1] = cntA[j][i]
                cntB[j][i + 1] = cntB[j][i]
            cntA[ord(a[i]) - ord('a')][i + 1] += 1
            cntB[ord(b[i]) - ord('a')][i + 1] += 1

        # Process queries
        for _ in range(q):
            l = int(data[index]) - 1
            r = int(data[index + 1])
            index += 2

            ans = 0
            for i in range(26):
                countA = cntA[i][r] - cntA[i][l]
                countB = cntB[i][r] - cntB[i][l]
                if countB > countA:
                    ans += countB - countA
            
            results.append(ans)

    # Output results
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    solve()
