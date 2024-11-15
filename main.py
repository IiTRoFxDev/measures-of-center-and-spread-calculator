class measures_of_center_and_spread :
    def __init__(self , numbers=[]):
        self.numbers = numbers
        print("coded by Eyad. (iitrofxdev)")
    def mean(self):
        if len(self.numbers) == 0:
            raise ValueError
        return  sum(self.numbers) / len(self.numbers)
    def median(self):
        self.numbers.sort()
        if len(self.numbers) == 0:
            raise ValueError
        first_number = int((len(self.numbers)+1)/ 2)-1
        if (len(self.numbers)+1) % 2:
           return {sum(self.numbers[first_number:first_number+2]) / 2}
        return {self.numbers[first_number]}
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
        return  end
    def standered_deviation(self):
        sigma = 0
        x_dash = data.mean()
        for item in self.numbers:
            sigma+=((item - x_dash)**2)
        return [((sigma / (len(self.numbers)-1))**0.5) , ((sigma / (len(self.numbers)))**0.5)]
data = measures_of_center_and_spread()
data.numbers = [int(i)  for i in list(input().split(",")) if i !=" "]
print(data.mean())
print(data.median())
print(data.mode())
print(data.standered_deviation())
