def possible(u, v, w):
    occurences = [0] * 26

    for i in range(len(u)):
        occurences[ord(u[i]) - 97] += 1

    for i in range(len(v)):
        occurences[ord(v[i]) - 97] += 1

    for i in range(len(w)):
        occurences[ord(w[i]) - 97] -= 1

    for i in range(26):
        if occurences[i] < 0:
            return False

    return True