def is_match(s: str, p: str) -> bool:
    len_s = len(s)
    len_p = len(p)
    s_index = p_index = 0
    prev = None

    if len_s != len_p and p.isalpha():
        return False

    while s_index < len_s and p_index < len_p:
        if s[s_index] == p[p_index] or "." == p[p_index]:
            s_index += 1
            p_index += 1
        elif p[p_index] == "*":
            pass



if __name__ == "__main__":
    assert is_match("a", "ab*a") is False
    assert is_match("a", "aaaa") is False
    assert is_match("asf", ".*") is True
    assert is_match("abcd", "d*") is False
    assert is_match("ab", ".*c") is False
    assert is_match("mississippi", "mis*is*p*.") is False
    assert is_match("aab", "c*a*b") is True
    assert is_match("aa", "a") is False
    assert is_match("aa", "a*") is True
    assert is_match("ab", ".*") is True
