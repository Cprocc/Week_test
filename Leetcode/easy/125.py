def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    import re
    if not s:
        return True

    # s = re.sub(r'[^\w]', '', s)

    s = re.sub(r'[\W]', "", s)
    p = s.lower()
    print(p)
    if p == p[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))

    import re
    ret = re.sub(r'^a', '', "areyouok;")
    print(ret)