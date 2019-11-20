def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    for start in range(0, len(s), n):
        chunk = s[start: start + n]
        while len(chunk) < n:
            chunk += '@'
        yield chunk
nums = "1.012345e0070.123414e-004-0.1234567891.214235846758946718yu8934u534057892340u59234 58923745892 y3540 34y750 7236 54293"

LList = list(chunks(nums, 6))

print (LList)