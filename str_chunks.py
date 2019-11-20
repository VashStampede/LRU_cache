def chunks_spit(s: str, n: int):
    """Produce `n`-character chunks from `s`."""
    res = []
    for start in range(0, len(s), n):
        chunk = s[start: start + n]
        while len(chunk) < n:
            chunk += '@'
        res.append(chunk)
    return res


def chunks_join(chunks: list):
    res = ''.join(chunks)
    tet = res.replace('@', '')
    return tet


if __name__ == '__main__':
    nums = "Mama myka ra"
    chunks = chunks_spit(nums, 5)
    print(chunks)
    print(chunks_join(chunks))






