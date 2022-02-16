function gcd(p, q)
    if q == 0 then
        return p
    end
    r = p % q
    return gcd(q, r)
end

result = gcd(8, 10)
print(result)
