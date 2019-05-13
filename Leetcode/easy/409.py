s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattl" \
    "efiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesth" \
    "atthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotcon" \
    "secratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwerto" \
    "addordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusth" \
    "elivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforus" \
    "tobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforw" \
    "hichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnatio" \
    "nunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"


def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    from collections import Counter
    s = Counter(s)
    res1 = 0
    res2 = 0
    max_jishu = 0
    for item in s:
        if s[item] % 2 == 0:
            res1 += s[item]
        else:
            max_jishu += 1
            res2 += s[item]

    return res1 + res2 - max_jishu + 1

print(longestPalindrome(s))
