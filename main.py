class measures_of_center :
    def __init__(self , numbers=[]):
        self.numbers = numbers
        print("coded by Eyad. (iitrofxdev)")
    def mean(self):
        if len(self.numbers) == 0:
            return "there isnot any number"
        return f"the mean = {sum(self.numbers) / len(self.numbers)}"
    def median(self):
        self.numbers.sort()
        if len(self.numbers) == 0:
            return "there isnot any number"
        first_number = int((len(self.numbers)+1)/ 2)-1
        if (len(self.numbers)+1) % 2:
           return f"the median = {sum(self.numbers[first_number:first_number+2]) / 2}"
        return f"the median = {self.numbers[first_number]}"    
    def mode(self):
        frequency = {}
        for i in self.numbers:
            if i in frequency:
                frequency[i] = frequency[i] + 1
            else:
                frequency[i] = 1
        the_value = max(frequency.values())
        end = []
        for key , value in frequency.items():
            if frequency[key] == the_value:
                end.append(key)
        return f"the mode = {end}"

data = measures_of_center()
data.numbers = [int(i)  for i in list(input().split(",")) if i !=" "]
print(data.mean())
print(data.median())
print(data.mode())