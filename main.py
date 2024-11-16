class measures_of_center :
    def __init__(self , numbers=[]):
        self.numbers = numbers
        print("coded by Eyad. (iitrofxdev)")
    def mean(self):
        if len(self.numbers) == 0:
            raise "there is not enough numbers in the data"
        return  sum(self.numbers) / len(self.numbers)
    def median(self):
        self.numbers.sort()
        if len(self.numbers) == 0:
            raise "there is not enough numbers in the data"
        first_number = int((len(self.numbers)+1)/ 2)-1
        if (len(self.numbers)+1) % 2:
           return sum(self.numbers[first_number:first_number+2]) / 2
        return self.numbers[first_number]
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
        if len(list(set(frequency.values()))) == 1 and len(end) != 1:
            return "There is no mod"
        return end
    def standered_deviation(self):
        if len(self.numbers) == 0:
            raise "there is not enough numbers in the data"
        sigma = 0
        x_dash = self.mean()
        for item in self.numbers:
            sigma+=((item - x_dash)**2)
        return [((sigma / (len(self.numbers)-1))**0.5) , ((sigma / (len(self.numbers)))**0.5)]
    def five_number_summary(self):
        self.numbers.sort()
        q2 = self.median()
        q1 = int((len(self.numbers)+1)/ 4)-1
        if (len(self.numbers)+1) % 4:
           q1_f(sum(self.numbers[q1:q1+2]) / 2)
        else:
            q1_f = (self.numbers[q1])
        q3 = (int((len(self.numbers)+1)/2))+q1
        if (len(self.numbers)+1) % 4:
           q3_f = (sum(self.numbers[q3:q3+2]) / 2)
        else:
            q3_f = (self.numbers[q3])
        # min , q1 , q2 , q3 , max , range , interquartle range
        return [min(self.numbers) , q1_f , q2 , q3_f , max(self.numbers) , max(self.numbers) - min(self.numbers) , q3_f - q1_f]
data = measures_of_center()
data.numbers = [int(i)  for i in list(input().split(",")) if i !=" "]
print(f"mean => {data.mean()}")
print(f"median => {data.median()}")
print(f"mode => {data.mode()}")
print(f"Population standard deviation => {(data.standered_deviation()[0])} , Sample standard deviation => {(data.standered_deviation()[1])}")
# min , q1 , q2 , q3 , max , range , interquartle range
print(f"min => {data.five_number_summary()[0]} , q1 => {data.five_number_summary()[1]} , q2 => {data.five_number_summary()[2]} , q3 => {data.five_number_summary()[3]} , max => {data.five_number_summary()[4]} , range => {data.five_number_summary()[5]} , interquartle range => {data.five_number_summary()[6]}")
input("press enter to close the window......")
