def sequence(n):
    while n != 1:
        print(n),
        if n % 2 == 0:  # n is even
            n = n / 2
        else:  # n is odd
            n = n * 3 + 1
while True :
    line=raw_input('>')
    if line == 'done':
        break
        print(line)
        print('done!')
        import matheval

        var = ('math.sqrt(5)')
        2.26069774997898
        eval('type(mayh.pi)')
import math


def factorial(n):
    """computes factorial of n."""
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result

    def estimate_pi():
        """compute an estimate of pi."""
        total = 0
        k = 0
        factor = 2 * math.sqrt(2) / 9801
        while True:
            num = factorial * (4 * k) * (1103 + 26390 * k)
            den = factorial(k) ** 4 * 396 ** (4 * k)
            term = factor * num / den
            total += term
            if abs(term) < 1e-15: break
            k += 1
            return 1 / total
        print(estimate_pi())
        fruit = 'banana'
        letter = fruit[1]
        print(letter)
        preflixes = 'JKLMNOPQ'
        sufflix = 'ack'
        for letter in preflixes:
            print(letter + sufflix)

        word= "banana"
        count=0
        for letter in word:
            if letter=='a':
                count=count+1
                print(count)
        word='banana'
        new_word=word.upper()
        print(new_word)
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
        def any_lowercase2(s):
            for c in s:
                if 'c'.islower():
                    return 'True'
            else:
                return 'False'
            def any_lowercase3(s):
                for c in s:
                flag=c.islower()
                return flag
            def any_lowercase4(s):
                flag=false
                for c in s:
                    flag=flag or c.islower()
def is_abecedarian(word):
    previous=word[0]
    for c in word:
        if c <previous:
            return False
        previous=creturn True
def is_abecedarian(word):
    if len(word)<=1:
        return True
    if word[0]>word[1]:
        return False
    return is_abecedarian(word[1:])
def is_abecedarian(word):
    i=0
    j=len(word)-1
    while i<j:
        if word[i]!=word[j]:
            return False
        i=i+1
        j=j-1
        return True

