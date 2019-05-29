start = int(input("시작값"))
end = int(input("끗값"))
baesu = int(input("배수"))


def calculate_sum(start,end):
    sum = 0
    for i in range(start,end+1):
        if i%baesu == 0:
            sum += i
    return sum
sumy = calculate_sum(start,end)

print(sumy)
